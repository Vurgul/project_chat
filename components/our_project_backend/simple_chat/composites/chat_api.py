from sqlalchemy import create_engine # почитать

from classic.sql_storage import TransactionContext

from simple_chat.adapters import database, chat_api
from simple_chat.application import services


class Settings:
    db = database.Settings()
    chat_api = chat_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    users_repo = database.repositories.UsersRepo(context=context)
    chats_repo = database.repositories.ChatsRepo(context=context)
    chat_messages_repo = database.repositories.ChatMessagesRepo(context=context)
    chat_members_repo = database.repositories.ChatMembersRepo(context=context)


class Application:
    chat_user_service = services.ChatUserService(
        chat_repo=DB.chats_repo,
    )
    user_service = services.UserService(
        user_repo=DB.users_repo,
    )


app = chat_api.create_app(
    chat=Application.chat_user_service,
    user=Application.user_service,
)

if __name__ == '__main__':
    from wsgiref import simple_server
    with simple_server.make_server('localhost', 8000, app=app) as server:
        print(f'Server running on http://localhost:{server.server_port} ...')
        server.serve_forever()
