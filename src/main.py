from fastapi import FastAPI

from auth.auth_configs import auth_backend
from auth.schemas import UserRead, UserCreate
from notes.router import router as note_router
from dependencies import fastapi_users
from database import Base, engine

app: FastAPI = FastAPI(title="Note service")


@app.on_event("startup")
async def startup() -> None:
    """ Функция создает таблицы для тестирования """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# @app.on_event("shutdown")
# async def shutdown() -> None:
#     """ Функция удаляет таблицы после тестирования """
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    note_router,
    tags=["Notes"]
)
