from typing import List
import argparse

from . import colors
from . import notes
from . import gammas


ljust = 4
row = "%s|"
fgcolor = colors.FG_COLORS[0]


def show_heading(frets, start_fret):
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


def show_string(index, startnote, frets: int, gamma: List[str], start_fret):
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
        startnote = notes.get_seq_next(startnote)

    print()


def show(gamma: str, string_tunings: List[str], start_fret: int, end_fret):
    if gamma != 'all':
        gamma_obj = getattr(gammas, gamma)
    else:
        gamma_obj = 'all'

    if string_tunings is None:
        string_tunings = ('E', 'A', 'D', 'G', 'B', 'E')

    strings = (getattr(notes, x) for x in string_tunings)
    end_fret += 1

    show_heading(end_fret, start_fret)
    for index, note in enumerate(strings):
        show_string(index, note, end_fret, gamma_obj, start_fret)


def main():
    GAMMAS = gammas.GAMMAS + ['all', ]

    parser = argparse.ArgumentParser()
    parser.add_argument('gamma', choices=GAMMAS)
    parser.add_argument('-t', '--string_tunings', nargs='+', 
                        choices=notes.NOTES, required=False)
    parser.add_argument('-s', '--start-fret', type=int, default=0)
    parser.add_argument('-e', '--end-fret', type=int, default=24)

    args = parser.parse_args()

    show(**vars(args))
