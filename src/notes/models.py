from typing import Dict, Any

from sqlalchemy import ForeignKey, select, insert, Row, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column


from database import Base


class Note(Base):
    """ Модель заметки """
    __tablename__ = "notes"
    __allow_unmapped__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(nullable=False)
    user: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    @staticmethod
    async def get_notes(user_id: int, session: AsyncSession) -> Sequence[Row]:
        """ Функция возвращает все заметки пользователя """
        stmt = select(Note).where(Note.user == user_id)  # noqa
        result = await session.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def create_note(data: dict, session: AsyncSession) -> Row | None:
        """ Функция создает новую заметку пользователя """
        stmt = insert(Note).values(**data).returning(Note)
        result = await session.execute(stmt)
        await session.commit()
        return result.scalars().first()

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}  # noqa
