from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

from src.settings import config

if config.is_development:
    db_url = 'sqlite:///tmp/db.db'
else:
    db_url = 'sqlite://~/.todo/config/db.db'


def _get_engine():
    return create_engine(db_url)


def get_session():
    return Session(_get_engine())
