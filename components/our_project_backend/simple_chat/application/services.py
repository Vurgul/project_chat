from typing import List, Optional, Tuple

from pydantic import conint, validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher

from . import errors, interfaces
from .dataclasses import User, Chat, ChatMessage, ChatMember

# Тут наши сервисы
join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: int
    login: str
    password: str



