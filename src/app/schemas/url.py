from pydantic import HttpUrl
from src.app.core.base import BaseSchema


class ExternalLink(BaseSchema):
    url: HttpUrl
