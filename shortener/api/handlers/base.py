from aiohttp.web_urldispatcher import View
from aiopg.sa import Engine


class BaseView(View):
    URL_PATH: str

    @property
    def db(self) -> Engine:
        return self.request.app['db']

    async def execute_query(self, query):
        async with self.db.acquire() as conn:
            return await conn.execute(query)

    async def fetch_one(self, query):
        async with self.db.acquire() as conn:
            result = await conn.execute(query)
            return await result.fetchone()
