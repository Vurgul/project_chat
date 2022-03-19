import pytest
from pydantic import ValidationError

from simple_chat.application import errors
from simple_chat.application.services import Authorization

data_user = {
    'id': 4,
    'login': 'test4',
    'password': 'password'
}


@pytest.fixture(scope='function')
def service(user_repo):
    return Authorization(user_repo=user_repo)


def test_add_user(service):
    service.add_user(**data_user)
    service.user_repo.add.assert_called_once()


def test_get_user_info(service, user_1):
    user = service.get_user_info(user_id=1)
    assert user == user_1
