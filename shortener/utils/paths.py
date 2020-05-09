from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
ALEMBIC_INI = BASE_DIR.joinpath('alembic.ini')
ALEMBIC_SCRIPT_LOCATION = BASE_DIR.joinpath('db', 'alembic')
CONFIG_PATH = BASE_DIR.joinpath('config.yml')