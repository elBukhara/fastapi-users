from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from fastapi_users.authentication import CookieTransport

SECRET = ":E\x10X\xef\xc1!\xf6daZ\xdc\x9e\xfb\xd7x"

# :E\x10X\xef\xc1!\xf6daZ\xdc\x9e\xfb\xd7x

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="auth_cookie")

# Define JWT strategy
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# Set up authentication backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
