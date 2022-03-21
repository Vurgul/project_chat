from unittest.mock import Mock

import pytest
from simple_chat.application import interfaces


@pytest.fixture(scope='function')
def user_repo(user_1, user_2):
    user_repo = Mock(interfaces.UsersRepo)
    user_repo.get_by_id = Mock(return_value=user_1)
    user_repo.get_by_user_data = Mock(return_value=user_1)
    return user_repo


@pytest.fixture(scope='function')
def user_repo_none_user(user_1, user_2):
    user_repo = Mock(interfaces.UsersRepo)
    user_repo.get_by_id = Mock(return_value=None)
    return user_repo


@pytest.fixture(scope='function')
def chat_repo(chat_1):
    chat_repo = Mock(interfaces.ChatsRepo)
    chat_repo.get_by_id = Mock(return_value=chat_1)
    return chat_repo


@pytest.fixture(scope='function')
def chat_repo_none_chat(chat_1):
    chat_repo = Mock(interfaces.ChatsRepo)
    chat_repo.get_by_id = Mock(return_value=None)
    return chat_repo


@pytest.fixture(scope='function')
def message_repo(chat_message_1, chat_message_2):
    message_repo = Mock(interfaces.ChatMessagesRepo)
    message_repo.get_by_message_id = Mock(
        return_value=[chat_message_1, chat_message_2]
    )
    return message_repo


@pytest.fixture(scope='function')
def member_repo(chat_member_1):
    member_repo = Mock(interfaces.ChatMembersRepo)
    member_repo.get_by_member_id = Mock(
        return_value=chat_member_1,
    )
    member_repo.get_by_fields = Mock(
        return_value=chat_member_1,
    )
    return member_repo


@pytest.fixture(scope='function')
def member_repo_none(chat_member_1):
    member_repo = Mock(interfaces.ChatMembersRepo)
    member_repo.get_by_member_id = Mock(
        return_value=chat_member_1
    )
    member_repo.get_by_fields = Mock(
        return_value=None
    )
    return member_repo
