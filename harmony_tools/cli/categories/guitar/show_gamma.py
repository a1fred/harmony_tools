from typing import List

from harmony_tools.core import colors
from harmony_tools import notes
from harmony_tools.core.note_operations import half_tone
from harmony_tools import gammas
from harmony_tools.cli.abc.command import BaseCommand


ljust = 4
row = "%s|"
fgcolor = colors.FG_COLORS[0]

NOTES = [x for x in dir(notes) if isinstance(getattr(notes, x), str) and not x.startswith("__")]
GAMMAS = [x for x in dir(gammas) if isinstance(getattr(gammas, x), list) and not x.startswith("__")]


class Command(BaseCommand):
    command = 'show_gamma'
    help = 'show gamma'

    def add_arguments(self, parser):
        parser.add_argument('gamma', choices=GAMMAS)
        parser.add_argument('-t', '--string_tunings', nargs='+', choices=NOTES, required=False)
        parser.add_argument('-s', '--start-fret', type=int, default=0)
        parser.add_argument('-e', '--end-fret', type=int, default=24)

    def handle(self, gamma: str, string_tunings: List[str], start_fret: int, end_fret):  # type: ignore
        gamma_obj = getattr(gammas, gamma)

        if string_tunings is None:
            string_tunings = ('E', 'A', 'D', 'G', 'B', 'E')

        strings = (getattr(notes, x) for x in string_tunings)
        end_fret += 1

        self.show_heading(end_fret, start_fret)
        for index, note in enumerate(strings):
            self.show_string(index, note, end_fret, gamma_obj, start_fret)

    def show_heading(self, frets, start_fret):
        print(row % "".ljust(ljust, ' '), end='')
        for fret in range(frets):
            if fret >= start_fret:
                print(row % colors.c(str(fret).rjust(ljust), colors.COLOR_GRAY), end='')
        print()

        print(row % colors.c("_" * ljust, colors.COLOR_GRAY), end='')
        for fret in range(frets):
            if fret >= start_fret:
                print(row % colors.c("_" * ljust, colors.COLOR_GRAY), end='')
        print()

    def show_string(self, index, startnote, frets: int, gamma: List[str], start_fret):
        global fgcolor
        print(row % colors.c(str(index + 1).rjust(ljust), colors.COLOR_GRAY), end='')

        for fret in range(frets):
            if gamma == 'all':
                if fret >= start_fret:
                    print(row % colors.c(startnote.ljust(ljust), fgcolor), end="")
            else:
                if startnote in gamma:
                    if fret >= start_fret:
                        print(row % colors.c(startnote.ljust(ljust), fgcolor), end="")
                else:
                    if fret >= start_fret:
                        print(row % ''.ljust(ljust), end="")
            if startnote == notes.B:
                fgcolor = colors.next_color(fgcolor)
            startnote = half_tone(startnote)

        print()
