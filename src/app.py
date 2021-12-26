import click

from src.task.helpers import build_task, get_tasks


@click.command()
@click.option('-n', '--new-task', 'message', default='')
@click.option('-l', '--list', 'list_', is_flag=True)
def todo(message, list_):
    if message:
        task = build_task(message)
        task.save()

    elif list_:

        tasks = get_tasks()
        for task in tasks:
            print(
                f'{"="*20}\n'
                f'Id: {task.id}\n'
                f'Task: {task.message}\n'
                f'{"="*20}'
            )
