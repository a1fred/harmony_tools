from typing import List

from harmony_tools.core import colors
from harmony_tools import notes, gammas
from harmony_tools.cli.abc.command import BaseCommand

NOTES = [x for x in dir(notes) if isinstance(getattr(notes, x), str) and not x.startswith("__")]
GAMMAS = [x for x in dir(gammas) if isinstance(getattr(gammas, x), list) and not x.startswith("__")]


class Command(BaseCommand):
    command = 'detect'
    help = 'detect gamma from note set'

    def add_arguments(self, parser):
        parser.add_argument('note', nargs='+', choices=NOTES)

    def handle(self, note: List[str]):  # type: ignore
        note_vals = [getattr(notes, x) for x in note]
        for gamma_name in GAMMAS:
            gamma = getattr(gammas, gamma_name)
            if all([x in gamma for x in note_vals]):
                self.show_gamma(gamma_name=gamma_name, gamma=gamma, hilight=note_vals)

    @staticmethod
    def show_gamma(gamma_name, gamma, hilight):
        print(f"{gamma_name:15}", end=" ")
        for n in gamma:
            if n in hilight:
                print(colors.c(n.ljust(2), colors.COLOR_YELLOW), end=' ')
            else:
                print(n.ljust(2), end=' ')
        print()
