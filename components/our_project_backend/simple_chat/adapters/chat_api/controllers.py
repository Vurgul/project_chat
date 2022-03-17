from classic.components import component
from classic.http_auth import (
    authenticate,
    authenticator_needed,
    authorize,
)

from simple_chat.application import services

from .auth import Groups, Permissions  # Для декоратора @authorize
from .join_points import join_point


@component
class Authorization:
    user_service: services.UserService

    @join_point
    def on_post_registration(self, request, response):
        self.user_service.add_user(**request.media)
        response.media = {
            "message": "Successful registration",
        }

    @join_point
    def on_post_authentication(self, request, response):
        """ Прохождение аутентификации -> авторизация"""
        pass


@component
class Chat:
    chat_user_service: services.ChatUserService

    @join_point
    def on_get_info(self, request, response):
        """Получить информацию о чате"""

        chat = self.chat_user_service.get_chat_info(**request.params)
        response.media = {
                'admin': chat.admin
            }

    @join_point
    def on_get_user_info(self, request, response):
        """ Получить список участников чата"""

        pass

    @join_point
    def on_get_leave(self, request, response):
        """ Покинуть чат"""

        pass

    @join_point
    def on_post_create(self, request, response):
        """Создать чат"""

        pass

    @join_point
    def on_post_uprate_info(self, request, response):
        """ Обновить информацию о чате"""

        pass

    @join_point
    def on_post_add_user(self, request, response):
        """ Добавить участника"""

        pass

    @join_point
    def on_delete_kick_user(self, request, response):
        """ Удалить участника """

        pass

    @join_point
    def on_delete_delete_chat(self, request, response):
        """ Удалить чат"""


@component
class Message:

    @join_point
    def on_get_chat_message(self, request, response):
        """ Получить список сообщений чата"""

        pass

    @join_point
    def on_post_send(self, request, response):
        """ Отправка сообщения в чат"""

        pass
