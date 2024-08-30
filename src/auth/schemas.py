from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """ Схема для валидации данных при чтении пользователя """
    id: int
    email: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    """ Схема для валидации данных при регистрации пользователя """
    email: str
    password: str
