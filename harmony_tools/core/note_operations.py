from harmony_tools import notes as n

notes_seq = (
    n.C, n.C_sharp,
    n.D, n.D_sharp,
    n.E,
    n.F, n.F_sharp,
    n.G, n.G_sharp,
    n.A, n.A_sharp,
    n.B,
)


def half_tone(note):
    if note not in notes_seq:
        raise ValueError("This is not note!")

    noteindex = notes_seq.index(note)
    noteindex += 1

    try:
        return notes_seq[noteindex]
    except IndexError:
        # Index overflow
        return notes_seq[0]


def tone(note):
    return half_tone(
        half_tone(note)
    )


def tone_and_half(note):
    return half_tone(
        half_tone(
            half_tone(note)
        )
    )
