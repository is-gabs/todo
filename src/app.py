from typing import List, Tuple

import click

from src.task.helpers import build_task, get_tasks
from src.task.model import TaskModel

COMMANDS = (
    'del',
    'done'
)


def show_task_list(tasks: List[TaskModel]) -> None:
    for index, task in zip(range(len(tasks)), tasks):
        click.echo(
            f'Index: {index} | Task: {task.message} | Done: {task.is_done}'
        )


def get_index_and_command(tasks: List[TaskModel]) -> Tuple[int, str]:
    try:
        index, command = click.prompt('Command').split(' ')
        index = int(index)
        assert command in COMMANDS
    except ValueError:
        click.echo(
            message='Invalid sixtax, use "[index] [command]" format.',
            err=True
        )
    except AssertionError:
        click.echo(
            message=(
                f'Command not found: {command}.\n'
                f'Use one of then: {list(COMMANDS)}.'
            ),
            err=True
        )
    try:
        assert index < len(tasks) and index >= 0
    except AssertionError:
        click.echo(
            message='Index out of range.',
            err=True
        )
    return index, command


@click.command()
@click.option('-n', '--new-task', 'message', default='')
@click.option('-l', '--list', 'list_', is_flag=True)
def todo(message, list_):
    if message:
        task = build_task(message)
        task.save()

    elif list_:
        tasks = get_tasks()
        show_task_list(tasks)
        index, command = get_index_and_command(tasks)
        if command == 'del':
            tasks[index].delete()
