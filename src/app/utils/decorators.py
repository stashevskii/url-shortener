from functools import wraps
from typing import Callable, Any
from src.app.api.errors import HTTPAliasNotFound
from src.app.core.exceptions import AliasNotFoundError

BUSINESS2HTTP = {
    AliasNotFoundError: HTTPAliasNotFound,
}


def handle_business_errors(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            try:
                raise BUSINESS2HTTP[e.__class__]()
            except KeyError:
                return await func(*args, **kwargs)

    return wrapper
