COLOR_BLUE = '\033[0;34m'
COLOR_GREEN = '\033[0;32m'
COLOR_CYAN = '\033[0;36m'
COLOR_RED = '\033[0;31m'
COLOR_PURPLE = '\033[0;35m'
COLOR_BROWN = '\033[0;33m'
COLOR_YELLOW = '\033[1;33m'
COLOR_GRAY = '\033[1;30m'

COLOR_RESET = '\033[0m'


FG_COLORS = [
    # COLOR_BLUE,
    COLOR_GREEN,
    # COLOR_CYAN,
    # COLOR_RED,
    # COLOR_PURPLE,
    # COLOR_BROWN,
    # COLOR_YELLOW,
]


def next_color(color):
    assert color in FG_COLORS

    index = FG_COLORS.index(color)
    index += 1

    try:
        return FG_COLORS[index]
    except IndexError:
        index = 0
        return FG_COLORS[index]


def c(string, color):
    global COLOR_RESET
    return f"{color}{string}{COLOR_RESET}"
