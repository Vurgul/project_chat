from classic.app.errors import AppError

# Наши исключения/ошибки


class NoUser(AppError):
    msg_template = "No user with id '{id}'"
    code = 'chat.no_user'


class NoChat(AppError):
    msg_template = "No chat with {field} '{id}'"
    code = 'chat.no_chat'
