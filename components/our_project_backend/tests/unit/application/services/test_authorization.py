import pytest
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


@pytest.fixture(scope='function')
def service_none_user(user_repo_none_user):
    return Authorization(user_repo=user_repo_none_user)


def test_add_user(service):
    service.add_user(**data_user)
    service.user_repo.add.assert_called_once()


def test_get_user_info(service, user_repo, user_1):
    user = service.get_user_info(user_id=1)
    assert user == user_1


def test_authentication(service, user_repo, user_1):
    user_repo = service.authentication(user_1.login, user_1.password)
    assert user_repo == user_1


def test_no_user_in_database(service_none_user, user_1):
    with pytest.raises(errors.NoUser):
        service_none_user.get_user_info(user_id=1)
