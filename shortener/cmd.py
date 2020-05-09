import os
import logging

from shortener.utils.paths import ALEMBIC_INI, ALEMBIC_SCRIPT_LOCATION
from shortener.utils.pg import  DEFAULT_PG_URL
from aiohttp.web import run_app as _run_app
from shortener.main import create_app
from alembic.config import CommandLine, Config


def alembic_command():
    logging.basicConfig(level=logging.DEBUG)
    alembic = CommandLine()
    options = alembic.parser.parse_args()
    if 'cmd' not in options:
        alembic.parser.error('too few arguments')
        exit(128)

    config = Config(ALEMBIC_INI)
    config.set_main_option('script_location', str(ALEMBIC_SCRIPT_LOCATION))
    config.set_main_option('sqlalchemy.url', os.getenv(
        'SHORTENER_PG_URL', DEFAULT_PG_URL))
    exit(alembic.run_cmd(config, options))


def run_app():
    _run_app(create_app())
