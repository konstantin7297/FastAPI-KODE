from typing import AsyncGenerator, Any

from fastapi import Depends
from fastapi_users import IntegerIDMixin, BaseUserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from database import get_async_session
from configs import USER_SECRET


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """ Класс отвечает за взаимодействие с пользователем: создание, логин... """
    reset_password_token_secret: str = USER_SECRET
    verification_token_secret: str = USER_SECRET


async def get_user_db(
        session: AsyncSession = Depends(get_async_session)
) -> AsyncGenerator[User, None]:
    """ Функция аутентифицирует пользователя """
    yield SQLAlchemyUserDatabase(session, User)  # noqa


async def get_user_manager(
        user_db=Depends(get_user_db)
) -> AsyncGenerator[UserManager, Any]:
    """ Функция отдает класс для работы с конкретным пользователем """
    yield UserManager(user_db)
