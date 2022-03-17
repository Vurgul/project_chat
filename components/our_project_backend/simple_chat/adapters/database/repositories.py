from typing import List, Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from simple_chat.application import interfaces
from simple_chat.application.dataclasses import User, Chat
from simple_chat.application.dataclasses import ChatMessage, ChatMember

@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):

    def get_by_id(self, id_: int) -> Optional[User]:
        query = select(User).where(User.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, user: User):
        self.session.add(user)
        self.session.flush()

    def get_by_login(self, login_: int) -> Optional[User]:
        query = select(User).where(User.login == login_)
        return self.session.execute(query).scalars().one_or_none()


@component
class ChatsRepo(BaseRepository, interfaces.ChatsRepo):

    def add(self, chat: Chat):
        pass

    def get_or_create(self, id_: Optional[int]) -> Chat:
        pass

    def remove(self, chat: Chat):
        self.session.delete(chat)

    def update(self, chat, data):
        # Работы с логикой БД
        pass

    def get_by_id(self, id_) -> Optional[Chat]:
        query = select(Chat).where(Chat.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def get_by_title(self, title_: int) -> Optional[Chat]:
        query = select(Chat).where(Chat.title == title_)
        return self.session.execute(query).scalars().one_or_none()

@component
class ChatMessagesRepo(BaseRepository, interfaces.ChatMessagesRepo):

    def get_by_id(self, id_: int) -> Optional[ChatMessage]:
        query = select(ChatMessage).where(ChatMessage.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, chat_message: ChatMessage):
        pass

    def get_or_create(self, id_: Optional[int]) -> ChatMessage:
        pass


@component
class ChatMembersRepo(BaseRepository, interfaces.ChatMembersRepo):

    def get_by_id(self, id_: int) -> Optional[ChatMember]:
        query = select(ChatMember).where(ChatMember.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, chat_member: ChatMember):
        pass

    def get_or_create(self, id_: Optional[int]) -> ChatMessage:
        pass
