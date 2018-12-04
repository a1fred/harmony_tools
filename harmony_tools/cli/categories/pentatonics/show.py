from typing import List

from harmony_tools import pentatonics
from harmony_tools.cli.abc.command import BaseCommand
from harmony_tools.cli.categories.gammas import detect

PENTS = [x for x in dir(pentatonics) if isinstance(getattr(pentatonics, x), tuple) and not x.startswith("__")]


class Command(BaseCommand):
    command = 'show'
    help = 'show pentatonic'

    def add_arguments(self, parser):
        parser.add_argument('gamma_names', nargs="+", choices=PENTS)

    def handle(self, gamma_names: List[str]):  # type: ignore
        for gamma_name in gamma_names:
            detect.Command.show_gamma(gamma_name, getattr(pentatonics, gamma_name), [])
