Quick way to see gamma layout on guitar

# Installation
Clone this repository and run
```sh
$ python3 setup.py install
```

Because i'm too lazy to upload to pypi

# Usage
     guitar_gammas
         [ -t  <string_note> <string_note> ... ]
         [ -s fret start ]
         [ -e fret end ]
         <gamma name>

## Example
Lets see 0-12 fret f-major gamma on dropped-e tuning

```
$ python3 main.py F_major -e12 -t D A D G B E
    |   0|   1|   2|   3|   4|   5|   6|   7|   8|   9|  10|  11|  12|
____|____|____|____|____|____|____|____|____|____|____|____|____|____|
   1|D   |    |E   |F   |    |G   |    |A   |A#  |    |C   |    |D   |
   2|E   |F   |    |G   |    |A   |A#  |    |C   |    |D   |    |E   |
   3|A   |A#  |    |C   |    |D   |    |E   |F   |    |G   |    |A   |
   4|D   |    |E   |F   |    |G   |    |A   |A#  |    |C   |    |D   |
   5|G   |    |A   |A#  |    |C   |    |D   |    |E   |F   |    |G   |
   6|    |C   |    |D   |    |E   |F   |    |G   |    |A   |A#  |    |
   7|E   |F   |    |G   |    |A   |A#  |    |C   |    |D   |    |E   |
```


# CONTRIBUTING
Feel free to create PR
