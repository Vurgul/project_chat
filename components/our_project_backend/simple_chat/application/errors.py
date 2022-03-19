from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = 'No user with id {id}'
    code = 'chat.no_user'


class NoChat(AppError):
    msg_template = 'No chat with id {id}'
    code = 'chat.no_chat'


class UserNotOwnerChat(AppError):
    msg_template = 'User with id {user_id} not owner chat with id {chat_id}'
    code = 'chat.not_user_owner'


class NoUserInChat(AppError):
    msg_template = 'User with id {user_id} not in chat with id {chat_id}'
    code = 'chat.no_user_in_chat'
