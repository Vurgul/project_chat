from typing import List, Optional, Tuple

from pydantic import conint, validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher

from . import errors, interfaces
from .dataclasses import User, Chat, ChatMessage, ChatMember

# Тут наши сервисы
join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: Optional[int]
    login: str
    password: str


@component
class ChatUserService:
    chat_repo: interfaces.ChatsRepo

    @join_point
    def get_chat_info(self, chat_id) -> Chat:
        chat = self.chat_repo.get_by_id(chat_id)
        if chat is None:
            raise Exception
        return chat


@component
class UserService:
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
            raise Exception
        return user


@component
class ChatMemberService:
    chat_member: interfaces.ChatMembersRepo
    pass


@component
class ChatMessageService:
    chat_message: interfaces.ChatMessagesRepo
    pass
