from classic.components import component
from classic.http_auth import authenticate, authenticator_needed, authorize
from simple_chat.application import services

from .auth import Groups, Permissions  # Для декоратора @authorize
from .join_points import join_point


@component
class Authorization:
    authorization: services.Authorization

    @join_point
    def on_post_registration(self, request, response):
        self.authorization.add_user(**request.media)

    @join_point
    def on_post_authentication(self, request, response):
        """ Прохождение аутентификации -> авторизация"""

        # TODO: Реализовать логику аутентификации
        response.media = {'user_id': ''}
        pass


@component
class ChatManager:
    chat: services.ChatManager

    @join_point
    def on_get_info(self, request, response):
        """Получить информацию о чате"""
        chat, user = self.chat.get_chat_info(**request.params)
        response.media = {
                'title': chat.title,
                'user_id': user.login
        }

    @join_point
    def on_get_users_info(self, request, response):
        """ Получить список участников чата"""
        users = self.chat.get_users_info(**request.params)
        response.media = {
            'users': users
        }

    @join_point
    def on_post_leave(self, request, response):
        """ Покинуть чат"""
        self.chat.leave_chat(
            **request.media
        )

    @join_point
    def on_post_create(self, request, response):
        """Создать чат"""
        self.chat.create_chat(
            **request.media,
        )

    @join_point
    def on_post_update_info(self, request, response):
        """ Обновить информацию о чате"""
        self.chat.update_chat_info(
            **request.media
        )

    @join_point
    def on_post_add_user(self, request, response):
        """ Добавить участника"""
        self.chat.add_user_to_chat(
            **request.media
        )

    @join_point
    def on_post_kick_user(self, request, response):
        """ Удалить / Выгнать участника чата"""
        # TODO: Если останется время
        pass

    @join_point
    def on_post_delete_chat(self, request, response):
        """ Удалить чат"""
        self.chat.delete_chat(
            **request.media
        )


@component
class Message:
    message: services.Message

    @join_point
    def on_get_messages(self, request, response):
        """ Получить список сообщений чата"""
        messages = self.message.get_chat_messages(**request.params)
        response.media = {
            'messages': messages
        }

    @join_point
    def on_post_send(self, request, response):
        """ Отправка сообщения в чат"""
        self.message.add_massage_to_chat(**request.media)
