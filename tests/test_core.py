import unittest

from harmony_tools.core import note_operations
from harmony_tools import notes as n


class TestCore(unittest.TestCase):
    def test_note_operations(self):
        self.assertEqual(note_operations.half_tone(n.A), n.A_sharp)
        self.assertEqual(note_operations.tone(n.A), n.B)
        self.assertEqual(note_operations.tone_and_half(n.C), n.D_sharp)
