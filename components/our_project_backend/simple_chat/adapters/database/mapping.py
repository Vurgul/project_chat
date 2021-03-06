from simple_chat.application import dataclasses
from sqlalchemy.orm import registry, relationship

from . import tables

mapper = registry()

mapper.map_imperatively(dataclasses.User, tables.users)

mapper.map_imperatively(
    dataclasses.ChatMessage,
    tables.chats_message,
    properties={
        'chat': relationship(
            dataclasses.Chat, uselist=False, lazy='joined'
        ),
        'user': relationship(
            dataclasses.User, uselist=False, lazy='joined'
        ),
    }
)

mapper.map_imperatively(
    dataclasses.ChatMember,
    tables.chats_member,
    properties={
        'chat': relationship(
            dataclasses.Chat, uselist=False, lazy='joined'
        ),
        'user': relationship(
            dataclasses.User, uselist=False, lazy='joined'
        ),
    }
)

mapper.map_imperatively(
    dataclasses.Chat,
    tables.chats,
    properties={
        'admin': relationship(
            dataclasses.User, uselist=False, lazy='joined'
        ),
        'members': relationship(dataclasses.ChatMember, lazy='subquery'),
        'messages': relationship(dataclasses.ChatMessage, lazy='subquery'),
    }
)
