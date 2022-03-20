from classic.http_api import App
from classic.http_auth import Authenticator
from simple_chat.application import services

from . import auth, controllers


def create_app(
    chat: services.ChatManager,
    authorization: services.Authorization,
    message: services.Message,
) -> App:

    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)
    authenticator.set_strategies(auth.jwt_strategy)

    app = App()
    app.register(controllers.ChatManager(
        authenticator=authenticator,
        chat=chat
        )
    )
    app.register(controllers.Authorization(
        authorization=authorization
        )
    )
    app.register(controllers.Message(
        authenticator=authenticator,
        message=message,
        )
    )

    return app
