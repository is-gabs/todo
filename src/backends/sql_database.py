from typing import List

from sqlalchemy import Boolean, Column, Integer, Text, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from src.exceptions import AppCoreError
from src.settings import config

Base = declarative_base()


if config.is_development:
    db_url = 'sqlite:///tmp/db.db'
else:
    db_url = 'sqlite://~/.todo/config/db.db'


def _get_engine():
    return create_engine(db_url)


class TaskModel(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(Text, nullable=False)
    is_done = Column(Boolean, default=False, index=True)

    def save(self) -> None:
        try:
            with Session(create_engine(db_url)) as session:
                session.add(self)
                session.commit()
        except SQLAlchemyError:
            raise AppCoreError()

    def delete(self) -> None:
        try:
            with Session(create_engine(db_url)) as session:
                session.delete(self)
                session.commit()
        except SQLAlchemyError:
            raise AppCoreError()

    def toggle_done(self) -> None:
        self.is_done = not self.is_done
        self.save()


def get_tasks() -> List[TaskModel]:
    try:
        with Session(_get_engine()) as session:
            tasks = session.query(TaskModel).all()
        return tasks
    except SQLAlchemyError:
        raise AppCoreError()


def build_task(message: str) -> TaskModel:
    return TaskModel(message=message)
