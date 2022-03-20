import pytest
from simple_chat.application import dataclasses


@pytest.fixture(scope='function')
def user_1():
    return dataclasses.User(
        id=1,
        login='test1',
        password='password1'
    )


@pytest.fixture(scope='function')
def user_2():
    return dataclasses.User(
        id=2,
        login='test2',
        password='password2'
    )


@pytest.fixture(scope='function')
def user_3():
    return dataclasses.User(
        id=3,
        login='test3',
        password='password3'
    )


@pytest.fixture(scope='function')
def chat_message_1():
    return dataclasses.ChatMessage(
        id=1,
        user_id=1,
        chat_id=1,
        text='text'
    )


@pytest.fixture(scope='function')
def chat_message_2():
    return dataclasses.ChatMessage(
        id=2,
        user_id=1,
        chat_id=1,
        text='text2'
    )


@pytest.fixture(scope='function')
def chat_member_1():
    return dataclasses.ChatMember(
        id=1,
        user_id=1,
        chat_id=1,
    )


@pytest.fixture(scope='function')
def chat_member_2():
    return dataclasses.ChatMember(
        id=2,
        user_id=2,
        chat_id=1,
    )


@pytest.fixture(scope='function')
def chat_member_3():
    return dataclasses.ChatMember(
        id=2,
        user_id=5,
        chat_id=4,
    )


@pytest.fixture(scope='function')
def chat_1(chat_member_1, chat_member_2, chat_member_3, chat_message_1,
           chat_message_2
    ):
    return dataclasses.Chat(
        id=1,
        user_id=1,
        title='TestTitle_owner_1',
        members=[chat_member_1, chat_member_2],
        messages=[chat_message_1, chat_message_2],
    )


@pytest.fixture(scope='function')
def chat_2():
    return dataclasses.Chat(
        id=2,
        user_id=2,
        title='TestTitle_owner_2',
        members=[chat_member_2()],
        messages=[chat_message_1, chat_message_2]
    )
