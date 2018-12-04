from typing import Tuple

from harmony_tools.core import note_operations

MAJOR_PENTATONIC = (
    note_operations.tone,
    note_operations.tone,
    note_operations.tone_and_half,
    note_operations.tone,
    note_operations.tone_and_half,
)

MINOR_PENTATONIC = (
    note_operations.tone_and_half,
    note_operations.tone,
    note_operations.tone,
    note_operations.tone_and_half,
    note_operations.tone,
)


def create_pentatonic(pentatonic_structure, note: str) -> Tuple[str, ...]:
    assert note in note_operations.notes_seq, f"'{note}' is not note"
    assert pentatonic_structure in [
        MINOR_PENTATONIC,
        MAJOR_PENTATONIC,
    ]

    pentatonic: Tuple[str, ...] = ()

    note_step = note

    for step in pentatonic_structure:
        pentatonic += (note_step, )
        note_step = step(note_step)

    return pentatonic
