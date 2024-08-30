from typing import List

from fastapi import APIRouter, Depends

from database import get_async_session
from notes.schemas import NoteFull, NoteShort
from notes.models import Note
from dependencies import fastapi_users
from notes.utils import Speller

router = APIRouter()
current_user = fastapi_users.current_user()


@router.post("/note/create", response_model=NoteFull)
async def create_note(
        note: NoteShort,
        user: current_user = Depends(),
        session: get_async_session = Depends()
) -> NoteFull:
    """ Функция для создания новой заметки пользователем """
    data: dict = note.dict()
    data["user"] = user.id

    errors: list = await Speller.check_text(data["text"])
    fixed_text: str = await Speller.fix_errors(data["text"], errors)

    data["text"] = fixed_text
    new_note = await Note.create_note(data, session)
    return new_note.to_json()


@router.get("/notes/get", response_model=List[NoteFull])
async def get_notes(
        user: current_user = Depends(), session: get_async_session = Depends()
) -> List[NoteFull]:
    """ Функция для получения списка заметок пользователя """
    all_notes = await Note.get_notes(user.id, session)
    result = [note.to_json() for note in all_notes]  # noqa
    return result
