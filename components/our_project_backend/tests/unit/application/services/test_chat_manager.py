import pytest
from pydantic import ValidationError

from simple_chat.application import errors
from simple_chat.application.services import ChatManager

data_user = {
    'id': 4,
    'login': 'test4',
    'password': 'password'
}


@pytest.fixture(scope='function')
def service(user_repo, chat_repo, message_repo, member_repo):
    return ChatManager(
        user_repo=user_repo,
        chat_repo=chat_repo,
        message_repo=message_repo,
        member_repo=member_repo
    )


def test_get_chat(service):
    pass


def test_get_user(service):
    pass


def test_get_chat_info(service):
    pass


def test_delete_chat(service):
    pass


def test_add_chat(service):
    pass


def test_get_users_info(service):
    pass


def test_update_chat_info(service):
    pass


def test_leave_chat(service):
    pass


def test_create_chat(service):
    pass


def test_add_user_to_chat(service):
    pass


