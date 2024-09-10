from fastapi_users.authentication import AuthenticationBackend

from .bearer import bearer_transport
from .strategy import get_database_strategy

SECRET = "SECRET"

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)