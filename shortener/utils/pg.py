from pathlib import Path
from aiopg.sa import create_engine

DEFAULT_PG_URL = 'postgresql://shortener:shortener@localhost/'
BASE_DIR = Path(__file__).parent.parent.resolve()
ALEMBIC_INI = BASE_DIR.joinpath('alembic.ini')
ALEMBIC_SCRIPT_LOCATION = BASE_DIR.joinpath('db', 'alembic')
CONFIG_PATH = BASE_DIR.joinpath('config.yml')


async def setup_pg(app):
    conf = app['config']['postgres']
    engine = await create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()
