from typing import List

from sqlalchemy.exc import SQLAlchemyError

from src.database import Session, get_engine
from src.exceptions import AppCoreError
from src.task.model import TaskModel


def build_task(message: str) -> TaskModel:
    return TaskModel(message=message)


def get_tasks() -> List[TaskModel]:
    try:
        with Session(get_engine()) as session:
            tasks = session.query(TaskModel).all()
        return tasks
    except SQLAlchemyError:
        raise AppCoreError()
