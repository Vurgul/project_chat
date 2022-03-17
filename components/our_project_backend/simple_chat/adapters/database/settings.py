from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = 'sqlite:////tmp/simple_chat.db'
    # DB_NAME
    # DB_HOST
    pass
