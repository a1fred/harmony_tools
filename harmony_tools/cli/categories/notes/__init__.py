from harmony_tools.cli.abc.category import BaseCategory

from harmony_tools.cli.categories.notes import (
    random,
)


class Category(BaseCategory):
    name = 'notes'
    help = 'note tools'

    def get_commands(self):
        return [
            random.Command(self),
        ]
