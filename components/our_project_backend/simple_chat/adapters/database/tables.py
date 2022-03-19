from sqlalchemy import (Boolean, Column, ForeignKey, Integer, MetaData, String,
                        Table, UniqueConstraint)

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=naming_convention)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('login', String, nullable=False, unique=True),
    Column('password', String, nullable=False),
)

chats = Table(
    'chats',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id'), nullable=False),
    Column('title', String, nullable=False),
)

chats_message = Table(
    'chats_message',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('chat_id', ForeignKey('chats.id'), nullable=False),
    Column('user_id', ForeignKey('users.id'), nullable=False),
    Column('text', String, nullable=False)
)

chats_member = Table(
    'chats_member',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('chat_id', ForeignKey('chats.id'), nullable=False),
    Column('user_id', ForeignKey('users.id'), nullable=False),
    Column('former_members', Boolean, default=False),
    Column('black_list', Boolean, default=False),
    UniqueConstraint('chat_id', 'user_id')
)
