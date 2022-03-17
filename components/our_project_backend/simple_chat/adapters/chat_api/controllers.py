from classic.components import component
from classic.http_auth import (
    authenticate,
    authenticator_needed,
    authorize,
)

from simple_chat.application import services

from .auth import Groups, Permissions # Для декоратора @authorize
from .join_points import join_point

# Тут наши контроллера (on_get / on_post)

@component
class Login:
    #users: services.Users

    @join_point
    def on_post_login(self, request, response):
        pass
