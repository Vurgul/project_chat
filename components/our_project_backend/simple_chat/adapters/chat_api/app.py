from typing import Tuple, Union

import falcon
from classic.http_api import App
from classic.http_auth import Authenticator
from classic.http_auth import strategies as auth_strategies
from simple_chat.application import services

from . import auth, controllers


def create_app(
    chat: services.ChatManager,
    authorization: services.Authorization,
    message: services.Message,
) -> App:

    app = App()
    app.register(controllers.ChatManager(chat=chat))
    app.register(controllers.Authorization(authorization=authorization))
    app.register(controllers.Message(message=message))

    return app

# Тут регистрация наших контроллеров, объявление миллваров, создание url
# создание основного приложения

