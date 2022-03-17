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
    messages: List['ChatMessage'] = attr.ib(factory=list)

    def find_member(self, chat_member: 'ChatMember') -> Optional['ChatMember']:
        for member in self.members:
            if chat_member == member:
                return member

    def add_members(self, chat_member: 'ChatMember'):
        member = self.find_member(chat_member)
        if member is not None:
            self.members.append(member)

    def remove_members(self, chat_member: 'ChatMember'):
        member = self.find_member(chat_member)
        if member is not None:
            self.members.remove(member)

    def find_message(self,
                     chat_message: 'ChatMessage'
    ) -> Optional['ChatMessage']:
        for message in self.messages:
            if chat_message == message:
                return message

    def add_message(self, chat_message: 'ChatMessage'):
        message = self.find_message(chat_message)
        if message is not None:
            self.messages.append(message)

    def remove_message(self, chat_message: 'ChatMessage'):
        message = self.find_message(chat_message)
        if message is not None:
            self.messages.remove(message)


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
