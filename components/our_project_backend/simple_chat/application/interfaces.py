from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import Chat, ChatMember, ChatMessage, User


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[User]: ...

    @abstractmethod
    def get_by_user_data(self, login: str, password: str): ...

    @abstractmethod
    def add(self, user: User): ...


class ChatsRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Chat]: ...

    @abstractmethod
    def remove(self, chat: Chat): ...

    @abstractmethod
    def add(self, chat: Chat): ...


class ChatMessagesRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[ChatMessage]: ...

    @abstractmethod
    def add(self, chat_message: ChatMessage): ...

    @abstractmethod
    def remove(self, message: ChatMessage): ...


class ChatMembersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[ChatMember]: ...

    @abstractmethod
    def add(self, chat_member: ChatMember): ...

    @abstractmethod
    def get_by_fields(self, chat_id: int, user_id: int) -> Optional[ChatMember]:
        ...

    @abstractmethod
    def remove(self, member: ChatMember): ...
