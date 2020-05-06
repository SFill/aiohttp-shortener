from typing import Optional
from shortener.api.handlers.base import BaseView
from aiohttp.web_response import json_response
from http import HTTPStatus
from shortener.api.shema import CreateShortSchema, CreateShortResponseShema
from shortener.db.shema import shorts_table
from aiohttp_apispec import request_schema, response_schema
from sqlalchemy import select

from hashlib import md5


class ShortenerView(BaseView):
    URL_PATH: str = '/short/'

    def generate_short_link(self, url: str):
        digest = md5(url.encode()).hexdigest()
        return digest[:7]

    async def check_short_exists(self, original: str) -> Optional[str]:
        query = select([shorts_table]).where(
            shorts_table.c.original == original)
        result = await self.fetch_one(query)
        return result[1] if result is not None else None

    @request_schema(CreateShortSchema())
    @response_schema(CreateShortResponseShema(), code=201)
    async def post(self):
        url = self.request['data']['url']
        short = await self.check_short_exists(url)
        if not short:
            short = self.generate_short_link(url)
            payload = {
                'original': url,
                'short': short
            }
            query = shorts_table.insert()  # noqa pylint: disable=no-value-for-parameter
            await self.execute_query(query.values(payload))
        return json_response(
            {'short': f'/short/{short}/'},
            status=HTTPStatus.CREATED
        )
