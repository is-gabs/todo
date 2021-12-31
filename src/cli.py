from typing import List

from rich.console import Console
from rich.table import Table

from src.utils import TaskProtocol, get_index_and_command


def draw_task_list(tasks: List[TaskProtocol]) -> None:
    table = Table(title='')
    table.add_column('I', justify='center')
    table.add_column('Task', justify='left')
    table.add_column('Done', justify='center')

    for index, task in zip(range(len(tasks)), tasks):
        table.add_row(
            str(index),
            task.message.lower(),
            '✓' if task.is_done else '☐'
        )

    Console().print(table)


def view_task_list(tasks: List[TaskProtocol]):
    draw_task_list(tasks)
    index, command = get_index_and_command(tasks)
    if command == 'del':
        tasks[index].delete()
    elif command == 'done':
        tasks[index].toggle_done()
