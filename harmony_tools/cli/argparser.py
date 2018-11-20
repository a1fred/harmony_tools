import argparse
from .categories import CATEGORIES

__all__ = [
    'parser',
]

parser = argparse.ArgumentParser(prog="harmony_tools")
section = parser.add_subparsers(title="Category", dest='category')


for category in CATEGORIES:
    subparser = section.add_parser(category.name, help=category.help)
    subparsers = subparser.add_subparsers(title="Command", dest='command')

    for command in category.commands:
        command_parser = subparsers.add_parser(command.command, help=command.help)
        command.add_arguments(parser=command_parser)
