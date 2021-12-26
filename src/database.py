from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.settings import config

if config.is_development:
    db_url = 'sqlite:///tmp/db.db'
else:
    db_url = 'sqlite://~/.todo/config/db.db'


def get_engine():
    return create_engine(db_url)


def add_object(obj) -> None:
    with Session(create_engine(db_url)) as session:
        session.add(obj)
        session.commit()


def update_object(obj) -> None:
    session = Session.object_session(obj)

    with session.begin() as session:
        session.commit()
