from typing import List, Optional

import attr

# Датаклассы наших сущностей
# Допускается указание методов


@attr.dataclass
class User:
    login: str
    password: str
    id: Optional[int] = None


@attr.dataclass
class Chat:
    admin: User
    title: str
    id: Optional[int] = None
    members: List['ChatMember'] = attr.ib(factory=list)
    message: List['ChatMessage'] = attr.ib(factory=list)


@attr.dataclass
class ChatMessage:
    chat: Chat
    user: User
    text: str
    id: Optional[int] = None


@attr.dataclass
class ChatMember:
    chat: Chat
    user: User
    former_members: bool
    black_list: bool
    id: Optional[int] = None
