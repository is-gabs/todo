from datetime import datetime

from sqlalchemy import Boolean, Column, Date, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

from src.database import add_object, update_object

Base = declarative_base()


class TaskModel(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)

    message = Column(Text, nullable=False)
    created_at = Column(Date, default=datetime.utcnow().date)
    is_done = Column(Boolean, default=False, index=True)
    work_day = Column(Date, default=datetime.utcnow().date, index=True)

    def save(self) -> None:
        add_object(self)

    def update(self) -> None:
        update_object(self)
