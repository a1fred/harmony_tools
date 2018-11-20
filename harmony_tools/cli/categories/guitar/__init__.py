from harmony_tools.cli.abc.category import BaseCategory

from harmony_tools.cli.categories.guitar import (
    show_gamma,
    show_pentatonic,
    show_neck,
)


class Category(BaseCategory):
    name = 'guitar'
    help = 'guitar tools'

    def get_commands(self):
        return [
            show_gamma.Command(self),
            show_pentatonic.Command(self),
            show_neck.Command(self),
        ]
