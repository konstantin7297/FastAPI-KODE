from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Integer, Boolean, select, Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """ Модель пользователя """
    __tablename__ = "users"
    __allow_unmapped__ = True

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = Column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = Column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = Column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = Column(Boolean, default=False, nullable=False)

    @staticmethod
    async def get_user(user_id: int, session: AsyncSession) -> Row:
        """ Функция для получения объекта пользователя """
        stmt = select(User).where(User.id == user_id)  # noqa
        result = await session.execute(stmt)
        return result.scalars().first()
