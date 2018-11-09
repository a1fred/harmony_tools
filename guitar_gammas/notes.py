import sys

C = "C"
C_sharp = 'C#'
D = "D"
D_sharp = 'D#'

E = "E"

F = "F"
F_sharp = "F#"

G = "G"
G_sharp = "G#"

A = 'A'
A_sharp = "A#"

B = H = "B"


Cb = B
Db = C_sharp
Eb = D_sharp
Fb = E
Gb = F_sharp
Ab = G_sharp
Bb = A_sharp

F_sharp_sharp = G

NOTES = [x for x in dir() if isinstance(getattr(sys.modules[__name__], x), str)]


notes_seq = (
    C, C_sharp,
    D, D_sharp,
    E,
    F, F_sharp,
    G, G_sharp,
    A, A_sharp,
    B,
)


def get_seq_next(note):
    if note not in notes_seq:
        raise ValueError("This is not note!")

    noteindex = notes_seq.index(note)
    noteindex += 1

    try:
        return notes_seq[noteindex]
    except IndexError:
        # Index overflow
        return notes_seq[0]
