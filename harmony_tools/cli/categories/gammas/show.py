from harmony_tools import gammas
from harmony_tools.cli.abc.command import BaseCommand
from harmony_tools.cli.categories.gammas import detect

GAMMAS = [x for x in dir(gammas) if isinstance(getattr(gammas, x), tuple) and not x.startswith("__")]


class Command(BaseCommand):
    command = 'show'
    help = 'show gamma'

    def add_arguments(self, parser):
        parser.add_argument('gamma_names', nargs="+", choices=GAMMAS)

    def handle(self, gamma_names: str):  # type: ignore
        for gamma_name in gamma_names:
            detect.Command.show_gamma(gamma_name, getattr(gammas, gamma_name), [])
