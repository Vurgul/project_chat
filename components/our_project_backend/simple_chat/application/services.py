from typing import List, Optional, Tuple

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import conint, validate_arguments

from . import errors, interfaces
from .dataclasses import Chat, ChatMember, ChatMessage, User

# Тут наши сервисы
join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: Optional[int]
    login: str
    password: str


class ChatInfo(DTO):
    title: str
    id: Optional[int] = None
    user_id: Optional[int] = None


class ChatCreateInfo(DTO):
    user_id: int
    title: str
    id: Optional[int]


class ChatUpdateInfo(DTO):
    user_id: int
    chat_id: int
    title: str
    id: Optional[int]


class ChatValidate(DTO):
    user_id: int
    chat_id: int


class MemberInfo(DTO):
    user_id: int
    chat_id: int

@component
class Authorization:
    user_repo: interfaces.UsersRepo

    @join_point
    @validate_with_dto
    def add_user(self, user_info: UserInfo):
        user = user_info.create_obj(User)
        self.user_repo.add(user)

    @join_point
    def get_user_info(self, user_id) -> User:
        user = self.user_repo.get_by_id(user_id)
        if user in None:
            raise errors.NoUser(id=user_id)
        return user


@component
class ChatManager:
    user_repo: interfaces.UsersRepo
    chat_repo: interfaces.ChatsRepo
    chat_member_repo: interfaces.ChatMembersRepo
    chat_message_repo: interfaces.ChatMessagesRepo

    @validate_arguments
    def get_chat(self, chat_id: int) -> Chat:
        chat = self.chat_repo.get_by_id(chat_id)
        if chat is None:
            raise errors.NoChat(id=chat_id)
        return chat

    @validate_arguments
    def get_user(self, user_id: int) -> User:
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise errors.NoUser(id=user_id)
        return user

    @join_point
    @validate_arguments
    def get_chat_info(self, chat_id: int) -> Tuple[Chat, User]:
        chat = self.chat_repo.get_by_id(chat_id)
        user = self.user_repo.get_by_id(chat.user_id)
        if chat is None:
            raise errors.NoChat(id=chat_id)
        return chat, user

    @join_point
    @validate_arguments
    def delete_chat(self, chat_id: int, user_id: int) -> None:
        chat = self._validate_owner_chat(chat_id, user_id)
        self.chat_repo.remove(chat)

    @join_point
    @validate_with_dto
    def add_chat(self, chat_info: ChatInfo):
        user = chat_info.create_obj(Chat)
        self.chat_repo.add(user)

    @join_point
    @validate_arguments
    def get_users_info(self, chat_id: int):
        chat = self.get_chat(chat_id)
        temp_user_list = []
        for user in chat.members:
            print(user)
            temp_user_list.append(user)
        return temp_user_list

    @join_point
    @validate_arguments
    def update_chat_info(self, chat_id: int, user_id: int, **kwargs):
        chat = self._validate_owner_chat(chat_id, user_id)
        modern_chat = ChatInfo(id=chat_id, user_id=user_id, **kwargs)
        modern_chat.populate_obj(chat)

    @join_point
    @validate_arguments
    def leave_chat(self, chat_id: int):
        # TODO: Если останется время
        pass

    @join_point
    @validate_with_dto
    def create_chat(self, chat_info: ChatCreateInfo):
        chat = chat_info.create_obj(Chat)
        self.user_repo.add(chat)

    @validate_with_dto
    def create_member(self, member_info: MemberInfo) -> ChatMember:
        print(member_info)
        member = member_info.create_obj(ChatMember)
        print(member)
        self.chat_member_repo.add(member)
        return member

    @join_point
    @validate_arguments
    def add_user_to_chat(self, chat_id: int, user_id: int, add_user_id: int):
        chat = self._validate_owner_chat(chat_id, user_id)
        member_info = MemberInfo(user_id=add_user_id, chat_id=chat_id)
        member = self.create_member(**member_info.dict())
        chat.add_members(member)

    @validate_arguments
    def _validate_owner_chat(self, chat_id: int, user_id: int) -> Chat:
        chat = self.get_chat(chat_id)
        user = self.get_user(user_id)
        if chat.user_id != user.id:
            raise errors.UserNotOwnerChat(user_id=user.id, chat_id=chat.user_id)
        return chat


@component
class Message:
    user_repo: interfaces.UsersRepo
    chat_repo: interfaces.ChatsRepo
    chat_message_repo: interfaces.ChatMessagesRepo

    pass

