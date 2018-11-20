from harmony_tools.core import note_operations


MAJOR_GAMMA = NATURAL_MAJOR_GAMMA = (
    note_operations.tone,
    note_operations.tone,
    note_operations.half_tone,
    note_operations.tone,
    note_operations.tone,
    note_operations.tone,
    note_operations.half_tone,
)


MINOR_GAMMA = NATURAL_MINOR_GAMMA = (
    note_operations.tone,
    note_operations.half_tone,
    note_operations.tone,
    note_operations.tone,
    note_operations.half_tone,
    note_operations.tone,
    note_operations.tone,
)


def create_gamma(gamma_structure, note: str):
    assert note in note_operations.notes_seq, f"'{note}' is not note"
    assert gamma_structure in [
        NATURAL_MAJOR_GAMMA,
        NATURAL_MINOR_GAMMA,
    ]

    gamma = []

    note_step = note

    for step in gamma_structure:
        gamma.append(note_step)
        note_step = step(note_step)

    return gamma
