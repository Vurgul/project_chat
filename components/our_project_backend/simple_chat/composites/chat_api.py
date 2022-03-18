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
    authorization = services.Authorization(
        user_repo=DB.users_repo,
    )
    chat = services.Chat(
        user_repo=DB.users_repo,
        chat_repo=DB.chats_repo,
        chat_member_repo=DB.chat_members_repo,
        chat_message_repo=DB.chat_messages_repo
    )
    message = services.Message(
        user_repo=DB.users_repo,
        chat_repo=DB.chats_repo,
        chat_message_repo=DB.chat_messages_repo
    )


app = chat_api.create_app(
    authorization=Application.authorization,
    chat=Application.chat,
    message=Application.message,
)

if __name__ == '__main__':
    from wsgiref import simple_server
    with simple_server.make_server('localhost', 8000, app=app) as server:
        print(f'Server running on http://localhost:{server.server_port} ...')
        server.serve_forever()

