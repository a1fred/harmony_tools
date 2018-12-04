from typing import List

from harmony_tools import notes, pentatonics
from harmony_tools.cli.categories.gammas.detect import Command as GDCommand

PENTS = [x for x in dir(pentatonics) if isinstance(getattr(pentatonics, x), list) and not x.startswith("__")]


class Command(GDCommand):
    command = 'detect'
    help = 'detect pentatonics from note set'

    def handle(self, note: List[str]):  # type: ignore
        note_vals = [getattr(notes, x) for x in note]
        for gamma_name in PENTS:
            gamma = getattr(pentatonics, gamma_name)
            if all([x in gamma for x in note_vals]):
                GDCommand.show_gamma(gamma_name=gamma_name, gamma=gamma, hilight=note_vals)
