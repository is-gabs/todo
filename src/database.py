from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.exceptions import AppCoreError
from src.settings import config

if config.is_development:
    db_url = 'sqlite:///tmp/db.db'
else:
    db_url = 'sqlite://~/.todo/config/db.db'


def get_engine():
    return create_engine(db_url)


def add_object(obj) -> None:
    try:
        with Session(create_engine(db_url)) as session:
            session.add(obj)
            session.commit()
    except SQLAlchemyError:
        raise AppCoreError()


def delete_object(obj) -> None:
    try:
        with Session(create_engine(db_url)) as session:
            session.delete(obj)
            session.commit()
    except SQLAlchemyError:
        raise AppCoreError()
