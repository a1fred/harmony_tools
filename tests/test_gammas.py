import unittest

from harmony_tools import gammas as g
from harmony_tools import notes as n


class TestGammas(unittest.TestCase):
    def test_gammas(self):
        self.assertEqual(g.C_major, [n.C, n.D, n.E, n.F, n.G, n.A, n.B])
        self.assertEqual([n.C_sharp, n.D_sharp, n.F, n.F_sharp, n.G_sharp, n.A_sharp, n.C], g.C_sharp_major)
        self.assertEqual([n.D, n.E, n.F_sharp, n.G, n.A, n.B, n.C_sharp], g.D_major)
        self.assertEqual([n.D_sharp, n.F, n.G, n.G_sharp, n.A_sharp, n.C, n.D], g.D_sharp_major)
        self.assertEqual([n.E, n.F_sharp, n.G_sharp, n.A, n.B, n.C_sharp, n.D_sharp, ], g.E_major)
        self.assertEqual([n.F, n.G, n.A, n.A_sharp, n.C, n.D, n.E], g.F_major)
        self.assertEqual([n.F_sharp, n.G_sharp, n.A_sharp, n.B, n.C_sharp, n.D_sharp, n.F], g.F_sharp_major)
        self.assertEqual([n.G, n.A, n.B, n.C, n.D, n.E, n.F_sharp], g.G_major)
        self.assertEqual([n.G_sharp, n.A_sharp, n.C, n.C_sharp, n.D_sharp, n.F, n.G], g.G_sharp_major)
        self.assertEqual([n.A, n.B, n.C_sharp, n.D, n.E, n.F_sharp, n.G_sharp], g.A_major)
        self.assertEqual([n.A_sharp, n.C, n.D, n.D_sharp, n.F, n.G, n.A], g.A_sharp_major)
        self.assertEqual([n.B, n.C_sharp, n.D_sharp, n.E, n.F_sharp, n.G_sharp, n.A_sharp], g.B_major)
        self.assertEqual([n.F, n.G, n.G_sharp, n.A_sharp, n.C, n.C_sharp, n.D_sharp], g.F_minor)
