from aiohttp.test_utils import TestClient
from aiohttp.web import HTTPException
from shortener.api import ShortenerView
from shortener.db.shema import shorts_table
from aiopg import Cursor
from aiopg.sa import Engine
from yarl import URL


async def select_shorts(db: Engine):
    async with db.acquire() as conn:
        conn: Cursor
        result = await conn.execute(shorts_table.select())
        data = await result.fetchall()
        return data


async def create_short(client: TestClient, data: dict, expected_status: int):
    response = await client.post(ShortenerView.URL_PATH, json=data)
    assert response.status == expected_status
    return await response.json()


class MockedHttpFound(HTTPException):
    status_code = 302

    def __init__(
        self,
        location,
        *,
        headers=None,
        reason=None,
        body=None,
        text=None,
        content_type=None
    ) -> None:
        super().__init__(headers=headers, reason=reason,
                         body=body, text=text, content_type=content_type)
        self.headers['_Location'] = str(URL(location))
        self.location = location
