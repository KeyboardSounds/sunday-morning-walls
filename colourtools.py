from random import randint
from collections import namedtuple

CHANNEL_MAX = 255
Rgb = namedtuple('RGB', ['r', 'g', 'b'])


def generatePalette(numColours=5):
    palette = []
    for i in range(numColours):
        rgb = Rgb(randint(0,CHANNEL_MAX), randint(0,CHANNEL_MAX), randint(0,CHANNEL_MAX))
        palette.append(rgb)

    return palette
