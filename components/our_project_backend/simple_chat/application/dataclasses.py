from typing import List, Optional

import attr

# Датаклассы наших сущностей
# Допускается указание методов


@attr.dataclass
class User:
    id: int
    login: str
    password: str


@attr.dataclass
class Chat:
    id: int
    admin: User
    title: str
    members: List['ChatMember'] = attr.ib(factory=list)
    message: List['ChatMessage'] = attr.ib(factory=list)


@attr.dataclass
class ChatMessage:
    id: int
    chat: Chat
    user: User
    text: str


@attr.dataclass
class ChatMember:
    id: int
    chat: Chat
    user: User
    former_members: bool
    black_list: bool
