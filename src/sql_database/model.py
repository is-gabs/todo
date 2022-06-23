from sqlalchemy import Boolean, Column, Integer, Text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

from src.exceptions import AppCoreError

from .database import get_session

Base = declarative_base()


class TaskModel(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(Text, nullable=False)
    is_done = Column(Boolean, default=False, index=True)

    def save(self) -> None:
        try:
            with get_session() as session:
                session.add(self)
                session.commit()
        except SQLAlchemyError:
            raise AppCoreError()

    def delete(self) -> None:
        try:
            with get_session() as session:
                session.delete(self)
                session.commit()
        except SQLAlchemyError:
            raise AppCoreError()

    def toggle_done(self) -> None:
        self.is_done = not self.is_done
        self.save()
