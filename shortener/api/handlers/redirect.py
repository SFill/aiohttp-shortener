from shortener.api.handlers.base import BaseView
from shortener.db.shema import shorts_table
from sqlalchemy import select
from aiohttp.web import HTTPFound
from aiohttp.web_exceptions import HTTPNotFound
from aiohttp_apispec import docs


class RedirectLinkView(BaseView):
    URL_PATH: str = '/short/{short}/'

    @docs(
        tags=["shorts"],
        summary="Redirect",
        description="Redirect with short link",
        responses={
            302: {"description": "Ok. Redirect"},
            404: {"description": "Not Found"},
            500: {"description": "Server error"},
        }
    )
    async def get(self):
        short = self.request.match_info['short']
        query = select([shorts_table]).where(shorts_table.c.short == short)
        url = await self.fetch_one(query)
        if not url:
            raise HTTPNotFound()
        raise HTTPFound(url[2])
