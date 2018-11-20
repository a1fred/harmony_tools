from typing import List
from harmony_tools.cli.abc.command import BaseCommand


class BaseCategory:
    name: str
    help: str

    def __init__(self) -> None:
        self.commands = self.get_commands()

    def get_commands(self) -> List[BaseCommand]:
        raise NotImplementedError

    @classmethod
    def supported(self) -> bool:
        return True

    def handle_command(self, command: str, **kwargs):
        for c in self.commands:
            if c.command == command:
                return c.handle(**kwargs)

        raise ValueError((command, kwargs))
