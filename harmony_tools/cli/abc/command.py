class BaseCommand:
    command: str
    help: str

    def __init__(self, category):
        self.category = category

    def add_arguments(self, parser):
        pass

    def handle(self, **kwargs):
        raise NotImplementedError
