import sys
from guitar_gammas.notes import *


C_major =       [C,       D,       E,       F,       G,       A,       B]
C_sharp_major =   [C_sharp, D_sharp, F,       F_sharp, G_sharp, A_sharp, C]

D_major =       [D,       E,       F_sharp, G,       A,       B,       C_sharp]
D_sharp_major = [D_sharp, F,       G,       G_sharp, A_sharp, C,       D ]

E_major =       [E,       F_sharp, G_sharp, A,       B,       C_sharp, D_sharp, ]

F_major =       [F,       G,       A,       A_sharp, C,       D,       E]
F_sharp_major = [F_sharp, G_sharp, A_sharp, B,       C_sharp, D_sharp, F]

G_major =       [G,       A,       B,       C,       D,       E,       F_sharp]
G_sharp_major = [G_sharp, A_sharp, C,       C_sharp, D_sharp, F,       D_sharp]

A_major =       [A,       B,       C_sharp, D,       E,       F_sharp, G_sharp]
A_sharp_major = [A_sharp, C,       D,       D_sharp, F,       G,       A]

B_major =       [B,       C_sharp, D_sharp, E,       F_sharp, G_sharp, A_sharp]


C_minor = D_sharp_major
C_sharp_minor = E_major

D_minor = F_major
D_sharp_minor = F_sharp_major

E_minor = G_major

F_minor =       [F,       G,       G_sharp, A_sharp, C,      C_sharp, D_sharp]
F_sharp_minor = A_major

G_minor = A_sharp_major
G_sharp_minor = B_major

A_minor = C_major
A_sharp_minor = C_sharp_major

B_minor = D_major

GAMMAS = [x for x in dir() if isinstance(getattr(sys.modules[__name__], x), list)]
