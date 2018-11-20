import sys

from harmony_tools.cli.argparser import parser
from harmony_tools.cli import categories


def main():
    args = parser.parse_args(sys.argv[1:])
    kwargs = vars(args)

    if kwargs['category'] is None or kwargs['command'] is None:
        parser.parse_args(['-h', ])

    category = kwargs.pop('category')
    command = kwargs.pop('command')

    for c in categories.CATEGORIES:
        if c.name == category:
            return c.handle_command(command, **kwargs)
    raise ValueError(category, **kwargs)
