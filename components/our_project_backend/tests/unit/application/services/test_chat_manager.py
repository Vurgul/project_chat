import pytest
from simple_chat.application import errors
from simple_chat.application.services import ChatManager

data_chat = {
    'user_id': 5,
    'title': 'title',
    'id': 4,
}

data_chat_update = {
    'chat_id': 1,
    'user_id': 1,
    'title': 'NewTittle'
}


@pytest.fixture(scope='function')
def service(user_repo, chat_repo, message_repo, member_repo):
    return ChatManager(
        user_repo=user_repo,
        chat_repo=chat_repo,
        chat_message_repo=message_repo,
        chat_member_repo=member_repo,
    )


@pytest.fixture(scope='function')
def service_none(user_repo, chat_repo, message_repo, member_repo_none):
    return ChatManager(
        user_repo=user_repo,
        chat_repo=chat_repo,
        chat_message_repo=message_repo,
        chat_member_repo=member_repo_none,
    )


@pytest.fixture(scope='function')
def service_no_chat(
    user_repo,
    chat_repo_none_chat,
    message_repo,
    member_repo_none
):
    return ChatManager(
        user_repo=user_repo,
        chat_repo=chat_repo_none_chat,
        chat_message_repo=message_repo,
        chat_member_repo=member_repo_none,
    )


def test_get_chat(service, chat_repo, chat_1):
    chat = service.get_chat(chat_id=chat_1.id)
    assert chat == chat_1


def test_get_user(service, user_1):
    user = service.get_user(user_id=user_1.id)
    assert user == user_1


def test_get_chat_info(service, user_1, chat_1):
    chat, user = service.get_chat_info(chat_id=chat_1.id, user_id=user_1.id)
    assert chat == chat_1
    assert user == user_1


def test_delete_chat(service, chat_1, user_1):
    service.delete_chat(chat_id=chat_1.id, user_id=user_1.id)
    service.chat_repo.remove.assert_called_once()


def test_get_users_info(service, chat_1, user_1):
    chat = service.get_users_info(chat_id=chat_1.id, user_id=user_1.id)
    assert isinstance(chat, list)
    assert user_1.login in chat
    assert len(chat) == 2


def test_update_chat_info(service, chat_1):
    service.update_chat_info(**data_chat_update)
    assert chat_1.title == 'NewTittle'


def test_leave_chat(service, chat_1, user_1):
    service.leave_chat(chat_id=chat_1.id, user_id=user_1.id)
    service.chat_member_repo.remove.assert_called()


def test_create_chat(service_none, member_repo):
    service_none.create_chat(**data_chat)
    service_none.chat_repo.add.assert_called_once()
    service_none.chat_member_repo.add.assert_called_once()


def test_add_user_to_chat(service_none, chat_1, user_1, user_2):
    service_none.add_user_to_chat(
        chat_id=chat_1.id,
        user_id=user_1.id,
        add_user_id=user_2.id
    )
    service_none.chat_member_repo.add.assert_called_once()


def test_no_chat_in_database(service_no_chat, chat_1, user_1):
    with pytest.raises(errors.NoChat):
        service_no_chat.get_chat(chat_id=chat_1.id)
        service.delete_chat(chat_id=chat_1.id, user_id=user_1.id)
        service.get_users_info(chat_id=chat_1.id, user_id=user_1.id)
        service.update_chat_info(**data_chat_update)


def test_no_user_in_chat(service_none, chat_1, user_1):
    with pytest.raises(errors.NoUserInChat):
        service_none.get_users_info(chat_id=chat_1.id, user_id=user_1.id)
        service_none.update_chat_info(**data_chat_update)
        service_none.leave_chat(chat_id=chat_1.id, user_id=user_1.id)
