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

    chats_repo = database.repositories.ChatsRepo(context=context)


class Application:
    chat_user_service = services.ChatUserService(
        chat_repo=DB.chats_repo,
    )


app = chat_api.create_app(
    chat=Application.chat_user_service,
)

if __name__ == '__main__':
    from wsgiref import simple_server

    with simple_server.make_server('', 8000, app=app) as server:
        server.serve_forever()
