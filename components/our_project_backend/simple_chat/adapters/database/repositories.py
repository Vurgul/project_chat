from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from simple_chat.application import interfaces
from simple_chat.application.dataclasses import (Chat, ChatMember, ChatMessage,
                                                 User)
from sqlalchemy import select


@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):

    def get_by_id(self, id: int) -> Optional[User]:
        query = select(User).where(User.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def get_by_user_data(self, login: str, password: str) -> Optional[User]:
        query = select(User).where(
            User.login == login,
            User.password == password,
        )
        return self.session.execute(query).scalars().one_or_none()

    def add(self, user: User):
        self.session.add(user)
        self.session.flush()


@component
class ChatsRepo(BaseRepository, interfaces.ChatsRepo):

    def get_by_id(self, id) -> Optional[Chat]:
        query = select(Chat).where(Chat.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def remove(self, chat: Chat):
        self.session.delete(chat)

    def add(self, chat: Chat):
        self.session.add(chat)
        self.session.flush()


@component
class ChatMessagesRepo(BaseRepository, interfaces.ChatMessagesRepo):

    def get_by_id(self, id: int) -> Optional[ChatMessage]:
        query = select(ChatMessage).where(ChatMessage.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, chat_message: ChatMessage):
        self.session.add(chat_message)
        self.session.flush()

    def remove(self, message: ChatMessage):
        self.session.delete(message)


@component
class ChatMembersRepo(BaseRepository, interfaces.ChatMembersRepo):

    def get_by_id(self, id: int) -> Optional[ChatMember]:
        query = select(ChatMember).where(ChatMember.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, chat_member: ChatMember):

        self.session.add(chat_member)
        self.session.flush()

    def get_by_fields(self, chat_id: int, user_id: int) -> Optional[ChatMember]:
        query = select(ChatMember).where(
            ChatMember.chat_id == chat_id,
            ChatMember.user_id == user_id
        )
        return self.session.execute(query).scalars().one_or_none()

    def remove(self, member: ChatMember):
        self.session.delete(member)
