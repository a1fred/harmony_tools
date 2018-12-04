import unittest

from harmony_tools.cli import run


class TestGammas(unittest.TestCase):
    def setUp(self):
        print()

    def test_guitar(self):
        run(['guitar', 'show_gamma', "A_major"])
        run(['guitar', 'show_pentatonic', "A_major"])
        run(['guitar', 'show_neck'])

    def test_notes(self):
        run(['notes', 'random'])

    def test_gammas(self):
        run(['gammas', 'show', 'A_major'])
        run(['gammas', 'detect', 'A', 'B', 'C'])

    def test_pentatonics(self):
        run(['pentatonics', 'show', 'A_major'])
        run(['pentatonics', 'detect', 'A', 'B', 'C'])
