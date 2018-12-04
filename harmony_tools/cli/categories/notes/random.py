from random import choice

from harmony_tools import notes
from harmony_tools.cli.abc.command import BaseCommand

NOTES = [x for x in dir(notes) if isinstance(getattr(notes, x), str) and not x.startswith("__")]


class Command(BaseCommand):
    command = 'random'
    help = 'show random note'

    def handle(self):
        print(getattr(notes, choice(NOTES)))
