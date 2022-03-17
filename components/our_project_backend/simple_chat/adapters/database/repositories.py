from typing import List, Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from simple_chat.application import interfaces
from simple_chat.application.dataclasses import User, Chat  # нужно реализовать

#@component
#class UsersRepo(BaseRepository, interfaces.UserRepo):
#    pass


@component
class ChatsRepo(BaseRepository, interfaces.ChatsRepo):

    def add(self, chat: Chat):
        pass

    def get_or_create(self, id_: Optional[int]) -> Chat:
        pass

    def remove(self, chat: Chat):
        pass

    def update(self, chat, data):
        # Работы с логикой БД
        pass

    def get_by_id(self, id_) -> Optional[Chat]:
        query = select(Chat).where(Chat.id == id_)
        return self.session.execute(query).scalars().one_or_none()
