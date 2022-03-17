from typing import Tuple, Union

import falcon

from classic.http_api import App
from classic.http_auth import Authenticator
from classic.http_auth import strategies as auth_strategies

from simple_chat.application import services

from . import auth, controllers


def create_app(
    chat: services.ChatUserService,
    user: services.UserService,
    message: services.ChatMessageService,
    member: services.ChatMemberService
) -> App:

    app = App()
    app.register(controllers.Chat(chat_user_service=chat))
    app.register(controllers.Authorization(user_service=user))

    return app

# Тут регистрация наших контроллеров, объявление миллваров, создание url
# создание основного приложения

