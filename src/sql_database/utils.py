from typing import List

from sqlalchemy.exc import SQLAlchemyError

from src.exceptions import AppCoreError

from .database import get_session
from .model import TaskModel


def build_task(message: str) -> TaskModel:
    return TaskModel(message=message)


def get_tasks() -> List[TaskModel]:
    try:
        with get_session() as session:
            tasks = session.query(TaskModel).all()
        return tasks
    except SQLAlchemyError:
        raise AppCoreError()
