from abc import abstractclassmethod
from typing import List, Protocol, Tuple

import click
from click import Abort

from src.constants import COMMANDS


class TaskProtocol(Protocol):
    id: str
    message: str
    is_done: bool

    @abstractclassmethod
    def save(self) -> None:
        raise NotImplementedError

    @abstractclassmethod
    def delete(self) -> None:
        raise NotImplementedError

    @abstractclassmethod
    def toggle_done(self) -> None:
        raise NotImplementedError


def get_index_and_command(tasks: List[TaskProtocol]) -> Tuple[int, str]:
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
