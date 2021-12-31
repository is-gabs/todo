import click
from click import Abort

from src.backends import backend
from src.cli import view_task_list
from src.exceptions import AppCoreError


@click.command()
@click.option('-n', '--new-task', 'message', default='')
@click.option('-l', '--list', 'list_', is_flag=True)
def todo(message, list_):
    if message:
        task = backend.build_task(message)
        try:
            task.save()
        except AppCoreError:
            click.echo('Error while saving task.', err=True)
            raise Abort()

    elif list_:
        try:
            tasks = backend.get_tasks()
        except AppCoreError:
            click.echo('Error while getting tasks from base.', err=True)
            raise Abort()

        if tasks:
            view_task_list(tasks)
        else:
            click.echo('Everything clean here, good job!')
