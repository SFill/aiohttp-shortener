from unittest.mock import patch
from aiohttp.test_utils import TestClient
from shortener.utils.testing import select_shorts, create_short, MockedHttpFound


async def test_shortener(api_client: TestClient):
    db = api_client.app['db']

    # запрос на создание короткой ссылки
    test_url = 'http://python.org/'
    data = await create_short(
        client=api_client,
        data={'url': test_url},
        expected_status=201
    )
    assert data['short'] == '/short/ff4faae/'
    short = list(await select_shorts(db))[0]
    assert short[2] == test_url
    assert short[1] == 'ff4faae'

    # проверяем валидность данных, при таких обращениях записи не должны создаваться
    data = await create_short(
        client=api_client,
        data={},
        expected_status=400
    )
    assert data['url'][0] == 'Missing data for required field.'
    shorts = await select_shorts(db)
    assert len(shorts) == 1

    data = await create_short(
        client=api_client,
        data={'url': 'qwerty'},
        expected_status=400
    )
    assert data['url'][0] == 'Not a valid URL.'
    shorts = await select_shorts(db)
    assert len(shorts) == 1

    # востановление ссылки после укорачивания
    with patch('shortener.api.handlers.redirect.HTTPFound', new=MockedHttpFound):
        response = await api_client.get('/short/ff4faae/')
        assert response.status == 302
        assert response.headers['_Location'] == test_url

    response = await api_client.get('/short/qwerty/')
    assert response.status == 404
