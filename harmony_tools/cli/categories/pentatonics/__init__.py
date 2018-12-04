from harmony_tools.cli.abc.category import BaseCategory

from harmony_tools.cli.categories.pentatonics import (
    detect,
    show,
)


class Category(BaseCategory):
    name = 'pentatonics'
    help = 'pentatonics tools'

    def get_commands(self):
        return [
            detect.Command(self),
            show.Command(self),
        ]
