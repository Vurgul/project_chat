import pytest
from pydantic import ValidationError

from simple_chat.application import errors
from simple_chat.application.services import Message

data_message = {
    'user_id': 1,
    'chat_id': 1,
    'text': 'please work'
}


@pytest.fixture(scope='function')
def service(user_repo, chat_repo, message_repo, member_repo):
    return Message(
        user_repo=user_repo,
        chat_repo=chat_repo,
        chat_message_repo=message_repo,
        chat_member_repo=member_repo,
    )


def test_get_chat_messages(service, chat_1, user_1, chat_message_1):
    message = service.get_chat_messages(chat_id=chat_1.id, user_id=user_1.id)
    assert isinstance(message, list)
    assert chat_message_1.text in message
    assert len(message) == 2


def test_create_massage(service):
    service.create_massage(**data_message)
    service.chat_message_repo.add.assert_called_once()


def test_add_massage_to_chat(service, chat_1, user_1):
    service.add_massage_to_chat(chat_id=chat_1.id, user_id=user_1.id, text='!')
    service.chat_message_repo.add.assert_called_once()
