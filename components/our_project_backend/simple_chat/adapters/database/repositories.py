from typing import List, Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from simple_chat.application import interfaces
from simple_chat.application.dataclasses import User # нужно реализовать

@component
class UsersRepo(BaseRepository, interfaces.UserRepo):
    pass
