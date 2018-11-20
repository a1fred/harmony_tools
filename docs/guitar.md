# Usage
     $ python3 main.py guitar -h
        usage: harmony_tools guitar [-h] {show_gamma,show_pentatonic,show_neck} ...

        optional arguments:
        -h, --help            show this help message and exit

        Command:
        {show_gamma,show_pentatonic,show_neck}
            show_gamma          show gamma
            show_pentatonic     show pentatonic neck layout
            show_neck           show neck notes
# Example
## Lets see 0-12 fret F-major gamma on dropped-e tuning
```
$ python3 main.py guitar show_gamma F_major -e12 -t D A D G B E
    |   0|   1|   2|   3|   4|   5|   6|   7|   8|   9|  10|  11|  12|
____|____|____|____|____|____|____|____|____|____|____|____|____|____|
   1|D   |    |E   |F   |    |G   |    |A   |A#  |    |C   |    |D   |
   2|A   |A#  |    |C   |    |D   |    |E   |F   |    |G   |    |A   |
   3|D   |    |E   |F   |    |G   |    |A   |A#  |    |C   |    |D   |
   4|G   |    |A   |A#  |    |C   |    |D   |    |E   |F   |    |G   |
   5|    |C   |    |D   |    |E   |F   |    |G   |    |A   |A#  |    |
   6|E   |F   |    |G   |    |A   |A#  |    |C   |    |D   |    |E   |
```

## Lets see all notes on bass guitar standart tuning
```
$ python3 main.py guitar show_neck -t E A D G -e20
    |   0|   1|   2|   3|   4|   5|   6|   7|   8|   9|  10|  11|  12|  13|  14|  15|  16|  17|  18|  19|  20|
____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
   1|E   |F   |F#  |G   |G#  |A   |A#  |B   |C   |C#  |D   |D#  |E   |F   |F#  |G   |G#  |A   |A#  |B   |C   |
   2|A   |A#  |B   |C   |C#  |D   |D#  |E   |F   |F#  |G   |G#  |A   |A#  |B   |C   |C#  |D   |D#  |E   |F   |
   3|D   |D#  |E   |F   |F#  |G   |G#  |A   |A#  |B   |C   |C#  |D   |D#  |E   |F   |F#  |G   |G#  |A   |A#  |
   4|G   |G#  |A   |A#  |B   |C   |C#  |D   |D#  |E   |F   |F#  |G   |G#  |A   |A#  |B   |C   |C#  |D   |D#  |
```

