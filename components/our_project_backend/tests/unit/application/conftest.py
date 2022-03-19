from unittest.mock import Mock

import pytest

from simple_chat.application import interfaces


@pytest.fixture(scope='function')
def users_repo(user_1, user_2, user_3):
    users_repo = Mock(interfaces.UsersRepo)
    users_repo.get_by_user_id = Mock(return_value=[user_1, user_2, user_3])
    return users_repo


@pytest.fixture(scope='function')
def chats_repo(chat_1, chat_2):
    chats_repo = Mock(interfaces.ChatsRepo)
    chats_repo.get_by_chat_id = Mock(return_value=[chat_1, chat_2])
    return chats_repo


@pytest.fixture(scope='function')
def messages_repo(chat_message_1, chat_message_2):
    messages_repo = Mock(interfaces.ChatMessagesRepo)
    messages_repo.get_by_message_id = Mock(
        return_value=[chat_message_1, chat_message_2]
    )
    return messages_repo


@pytest.fixture(scope='function')
def members_repo(chat_member_1, chat_member_2, chat_member_3):
    members_repo = Mock(interfaces.ChatMembersRepo)
    members_repo.get_by_member_id = Mock(
        return_value=[chat_member_1, chat_member_2, chat_member_3]
    )
    return members_repo
