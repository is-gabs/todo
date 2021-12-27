from typing import List, Tuple

import click
from click import Abort
from rich.console import Console
from rich.table import Table

from src.exceptions import AppCoreError
from src.task.helpers import build_task, get_tasks
from src.task.model import TaskModel

COMMANDS = (
    'del',
    'done'
)


def draw_task_list(tasks: List[TaskModel]) -> None:
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


def get_index_and_command(tasks: List[TaskModel]) -> Tuple[int, str]:
    try:
        _input = click.prompt('Command')
        if _input == 'exit':
            raise Abort()
        index, command = _input.split(' ')
        index = int(index)
        assert command in COMMANDS
    except ValueError:
        click.echo(
            message='Invalid sixtax, use "[index] [command]" format.',
            err=True
        )
        raise Abort()
    except AssertionError:
        click.echo(
            message=(
                f'Command not found: {command}.\n'
                f'Use one of then: {list(COMMANDS)}.'
            ),
            err=True
        )
        raise Abort()
    try:
        assert index < len(tasks) and index >= 0
    except AssertionError:
        click.echo(
            message='Index out of range.',
            err=True
        )
        raise Abort()
    return index, command


def view_task_list(tasks: List[TaskModel]):
    draw_task_list(tasks)
    index, command = get_index_and_command(tasks)
    if command == 'del':
        tasks[index].delete()
    elif command == 'done':
        tasks[index].toggle_done()


@click.command()
@click.option('-n', '--new-task', 'message', default='')
@click.option('-l', '--list', 'list_', is_flag=True)
def todo(message, list_):
    if message:
        task = build_task(message)
        try:
            task.save()
        except AppCoreError:
            click.echo('Error while saving task.', err=True)
            raise Abort()

    elif list_:
        try:
            tasks = get_tasks()
        except AppCoreError:
            click.echo('Error while getting tasks from base.', err=True)
            raise Abort()

        if tasks:
            view_task_list(tasks)
        else:
            click.echo('Everything clean here, good job!')
