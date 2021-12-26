from typing import List

from src.database import Session, get_engine
from src.task.model import TaskModel


def build_task(message: str) -> TaskModel:
    return TaskModel(message=message)


def get_tasks() -> List[TaskModel]:
    with Session(get_engine()) as session:
        tasks = session.query(TaskModel).all()
    return tasks
