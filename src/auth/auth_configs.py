from fastapi_users.authentication import CookieTransport, JWTStrategy, \
    AuthenticationBackend

from configs import JWT_SECRET

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_secure=False)


def get_jwt_strategy() -> JWTStrategy:
    """ Функция отвечает за корректную работу с JWT token'ом """
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
