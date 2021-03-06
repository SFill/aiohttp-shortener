import pytest
import uuid
from yarl import URL
from sqlalchemy_utils import create_database, drop_database
from shortener.utils.paths import ALEMBIC_INI, CONFIG_PATH, ALEMBIC_SCRIPT_LOCATION
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from shortener.utils.parse_config import get_config
from shortener.main import create_app


@pytest.fixture
def db():
    from shortener.utils.pg import DEFAULT_PG_URL
    tmp_name = '.'.join([uuid.uuid4().hex, 'pytest'])
    tmp_url = str(URL(DEFAULT_PG_URL).with_path(tmp_name))
    create_database(tmp_url)
    alembic_config = AlembicConfig(ALEMBIC_INI)
    alembic_config.set_main_option('sqlalchemy.url', tmp_url)
    alembic_config.set_main_option(
        'script_location', str(ALEMBIC_SCRIPT_LOCATION))
    alembic_upgrade(alembic_config, 'head')
    try:
        yield tmp_name
    finally:
        drop_database(tmp_url)


@pytest.fixture
async def api_client(aiohttp_client, db):
    config = get_config(CONFIG_PATH)
    config['postgres']['database'] = db
    app = create_app(config)
    client = await aiohttp_client(app)
    try:
        yield client
    finally:
        await client.close()
