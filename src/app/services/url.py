import string
import random
from fastapi.responses import RedirectResponse
from src.app.core.base import Service
from src.app.core.exceptions import AliasNotFoundError
from src.app.models import Url
from src.app.schemas import ExternalLink


class UrlService(Service):
    async def __get(self, alias: str) -> Url:
        url = await self.repository.get(alias)
        if not url:
            raise AliasNotFoundError
        return url

    async def get(self, alias: str) -> RedirectResponse:
        url = await self.__get(alias)
        await self.repository.add_click(url)
        return RedirectResponse(url=url.url, status_code=301)

    async def get_info(self, alias: str) -> Url:
        return await self.__get(alias)

    @staticmethod
    def __generate_hash():
        while True:
            code = "".join(random.choices(string.digits + string.ascii_letters, k=6))
            if any(c.isalpha() for c in code):
                return code

    async def add(self, schema: ExternalLink) -> Url:
        all_aliases = await self.repository.get_all_aliases()
        alias = self.__generate_hash()
        while alias in all_aliases:
            alias = self.__generate_hash()

        return await self.repository.add(str(schema.url), alias)
