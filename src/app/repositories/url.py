from sqlalchemy import select
from src.app.core.base import Repository
from src.app.models import Url


class UrlRepository(Repository[Url]):
    async def get(self, alias: str) -> Url:
        res = await self.session.execute(select(self.table).where(Url.alias == alias))
        return res.scalars().first()

    async def get_all_aliases(self):
        res = await self.session.execute(select(self.table))
        return [url.alias for url in res.scalars().all()]

    async def add_click(self, url: Url) -> None:
        url.clicks += 1
        await self.commit()

    async def add(self, url: str, alias: str) -> Url:
        url = Url(alias=alias, url=url)
        self.session.add(url)
        await self.commit()
        return url
