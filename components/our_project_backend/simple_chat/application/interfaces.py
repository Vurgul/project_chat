from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import User, Chat, ChatMessage, ChatMember

# наши интерфейсы,  которые реализуем в адаптерах


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, user: User):
        ...

    @abstractmethod
    def get_or_create(self, id_: Optional[int]) -> User:
        ...


class ChatsRepo(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def add(self, chat: Chat):
        ...

    @abstractmethod
    def get_or_create(self, id_: Optional[int]) -> Chat:
        ...

    @abstractmethod
    def remove(self, chat: Chat):
        ...

    @abstractmethod
    def update(self, chat: Chat, date) -> Chat:
        ...


class ChatMessages(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[ChatMessage]:
        ...

    @abstractmethod
    def add(self, chat_message: ChatMessage):
        ...

    @abstractmethod
    def get_or_create(self, id_: Optional[int]) -> ChatMessage:
        ...


class ChatMembers(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[ChatMember]:
        ...

    @abstractmethod
    def add(self, chat_member: ChatMember):
        ...

    @abstractmethod
    def edit(self):  # Вопросики
        ...

