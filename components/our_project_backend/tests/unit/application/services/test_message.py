import pytest
from pydantic import ValidationError

from simple_chat.application import errors
from simple_chat.application.services import Message

data_user = {
    'id': 4,
    'login': 'test4',
    'password': 'password'
}


@pytest.fixture(scope='function')
def service(user_repo, chat_repo, message_repo, member_repo):
    return Message(
        user_repo=user_repo,
        chat_repo=chat_repo,
        message_repo=message_repo,
        member_repo=member_repo
    )


def test_get_chat_messages(service):
    pass


def test_create_massage(service):
    pass


def test_add_massage_to_chat(service):
    pass
