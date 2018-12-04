from harmony_tools.cli.abc.category import BaseCategory

from harmony_tools.cli.categories.gammas import (
    detect,
    show,
)


class Category(BaseCategory):
    name = 'gammas'
    help = 'gammas tools'

    def get_commands(self):
        return [
            detect.Command(self),
            show.Command(self),
        ]
