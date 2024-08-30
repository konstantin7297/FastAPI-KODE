from pydantic import BaseModel


class NoteShort(BaseModel):
    """ Схема для валидации полученной заметки от пользователя """
    text: str


class NoteFull(NoteShort):
    """ Схема для валидации возвращаемой модели заметки пользователя """
    id: int
    user: int
