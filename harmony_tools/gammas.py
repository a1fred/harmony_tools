from harmony_tools import notes as n
from harmony_tools.core import gamma_structure as gs


C_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.C)

C_sharp_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.C_sharp)
D_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.D)
D_sharp_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.D_sharp)
E_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.E)
F_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.F)
F_sharp_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.F_sharp)
G_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.G)
G_sharp_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.G_sharp)
A_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.A)
A_sharp_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.A_sharp)
B_major = gs.create_gamma(gs.NATURAL_MAJOR_GAMMA, n.B)


C_minor = gs.create_gamma(gs.NATURAL_MINOR_GAMMA, n.C)
C_sharp_minor = E_major
D_minor = F_major
D_sharp_minor = F_sharp_major
E_minor = G_major
F_minor = gs.create_gamma(gs.NATURAL_MINOR_GAMMA, n.F)
F_sharp_minor = A_major
G_minor = A_sharp_major
G_sharp_minor = B_major
A_minor = C_major
A_sharp_minor = C_sharp_major
B_minor = D_major

A_minor_pentetonic = [n.C, n.D, n.E, n.G,       n.A]

C_major_pentetonic = [n.C, n.D, n.E, n.F_sharp, n.G, n.A]
