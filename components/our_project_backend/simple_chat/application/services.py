from typing import List, Optional, Tuple

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Chat, ChatMember, ChatMessage, User

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    login: str
    password: str
    id: Optional[int]


class ChatInfo(DTO):
    title: str
    id: Optional[int] = None
    user_id: Optional[int] = None


class MemberInfo(DTO):
    user_id: int
    chat_id: int


class MessageInfo(DTO):
    user_id: int
    chat_id: int
    text: str


class ChatCreateInfo(DTO):
    user_id: int
    title: str
    id: Optional[int]


@component
class Authorization:
    user_repo: interfaces.UsersRepo

    @join_point
    @validate_with_dto
    def add_user(self, user_info: UserInfo):
        user = user_info.create_obj(User)
        self.user_repo.add(user)

    @join_point
    @validate_arguments
    def get_user_info(self, user_id: int) -> User:
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise errors.NoUser(id=user_id)
        return user

    @join_point
    @validate_arguments
    def authentication(self, login: str, password: str) -> User:
        user = self.user_repo.get_by_user_data(login, password)
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
    def get_chat_info(self, chat_id: int, user_id: int) -> Tuple[Chat, User]:
        self._validate_user_in_chat(chat_id, user_id)
        chat = self.chat_repo.get_by_id(chat_id)
        user = self.user_repo.get_by_id(chat.user_id)
        if chat is None:
            raise errors.NoChat(id=chat_id)
        return chat, user

    @join_point
    @validate_arguments
    def delete_chat(self, chat_id: int, user_id: int) -> None:
        chat = self._validate_owner_chat(chat_id, user_id)
        for members in chat.members:
            self.chat_member_repo.remove(members)
        for message in chat.messages:
            self.chat_message_repo.remove(message)
        self.chat_repo.remove(chat)

    @join_point
    @validate_arguments
    def get_users_info(self, chat_id: int, user_id: int) -> List:
        self._validate_user_in_chat(chat_id, user_id)
        chat = self.get_chat(chat_id)
        users = []
        for member in chat.members:
            user_login = self.get_user(member.user_id).login
            users.append(user_login)
        return users

    @join_point
    @validate_arguments
    def update_chat_info(self, chat_id: int, user_id: int, **kwargs):
        chat = self._validate_owner_chat(chat_id, user_id)
        modern_chat = ChatInfo(id=chat_id, user_id=user_id, **kwargs)
        modern_chat.populate_obj(chat)

    @join_point
    @validate_arguments
    def leave_chat(self, chat_id: int, user_id: int):
        chat = self.get_chat(chat_id)
        user = self.get_user(user_id)
        member = self._validate_user_in_chat(chat_id, user_id)
        if chat.user_id == user.id:
            self.delete_chat(chat_id, user_id)
        else:
            self.chat_member_repo.remove(member)

    @join_point
    @validate_with_dto
    def create_chat(self, chat_info: ChatCreateInfo) -> Chat:
        chat = chat_info.create_obj(Chat)
        self.chat_repo.add(chat)
        self.add_user_to_chat(chat.id, chat.user_id, chat.user_id)
        return chat

    @validate_with_dto
    def create_member(self, member_info: MemberInfo) -> ChatMember:
        member = member_info.create_obj(ChatMember)
        find_member = self.chat_member_repo.get_by_fields(
            chat_id=member.chat_id,
            user_id=member.user_id
        )
        if find_member is not None:
            raise errors.UserAlreadyInChat(
                user_id=member.user_id,
                chat_id=member.chat_id
            )

        self.chat_member_repo.add(member)
        return member

    @join_point
    @validate_arguments
    def add_user_to_chat(self, chat_id: int, user_id: int, add_user_id: int):
        chat = self._validate_owner_chat(chat_id, user_id)
        member_info = MemberInfo(user_id=add_user_id, chat_id=chat_id)
        member = self.create_member(**member_info.dict())
        chat.add_members(member)

    def _validate_owner_chat(self, chat_id: int, user_id: int) -> Chat:
        chat = self.get_chat(chat_id)
        user = self.get_user(user_id)
        if chat.user_id != user.id:
            raise errors.UserNotOwnerChat(user_id=user.id, chat_id=chat.user_id)
        return chat

    def _validate_user_in_chat(self, chat_id: int, user_id: int) -> ChatMember:
        member = self.chat_member_repo.get_by_fields(chat_id, user_id)
        if member is None:
            raise errors.NoUserInChat(user_id=user_id, chat_id=chat_id)
        return member


@component
class Message:
    user_repo: interfaces.UsersRepo
    chat_repo: interfaces.ChatsRepo
    chat_message_repo: interfaces.ChatMessagesRepo
    chat_member_repo: interfaces.ChatMembersRepo

    @validate_arguments
    def _validate_user_in_chat(self, chat_id: int, user_id: int) -> Chat:
        chat = self.chat_repo.get_by_id(chat_id)
        if chat is None:
            raise errors.NoChat(id=chat_id)
        member = self.chat_member_repo.get_by_fields(chat_id, user_id)
        if member is None:
            raise errors.NoUserInChat(user_id=user_id, chat_id=chat_id)
        return chat

    @validate_arguments
    def get_chat_messages(self, chat_id: int, user_id: int) -> List:
        chat = self._validate_user_in_chat(chat_id, user_id)
        massages = []
        for message in chat.messages:
            massages.append(message.text)
        return massages

    @validate_with_dto
    def create_message(self, message_info: MessageInfo) -> ChatMessage:
        message = message_info.create_obj(ChatMessage)
        self.chat_message_repo.add(message)
        return message

    @validate_arguments
    def add_message_to_chat(self, chat_id: int, user_id: int, text: str):
        chat = self._validate_user_in_chat(chat_id, user_id)
        message_info = MessageInfo(chat_id=chat_id, user_id=user_id, text=text)
        message = self.create_message(**message_info.dict())
        chat.add_message(message)
