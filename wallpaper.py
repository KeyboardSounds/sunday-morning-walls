"""
Sunday Morning Walls

Usage:
    wallpaper.py [COOLORS_URL] [--x=<x> --y=<y>] [--outdir DIR]
    wallpaper.py [--c=<c>] [--x=<x> --y=<y>] [--outdir DIR]
    wallpaper.py (-h | --help)
    wallpaper.py (-v | --version)


Options:
    -h --help            Show this screen
    -v --version         Print version information
    --x=<x>              Specify the width of the output image [default: 1800]
    --y=<y>              Specify the height of the output image [default: 1200]
    -o DIR --outdir DIR  The path of the output folder [default: out]
    --c=<c>               How many wallpapers to generate [default: 1]
"""
from PIL import Image, ImageDraw
from collections import namedtuple
from docopt import docopt
from time import sleep
import sys
import colourtools

Xy = namedtuple('Xy', ['x', 'y'])

def hexToDec(hex):
    return int(hex, 16)

def parseCoolorsUrl(url):
    start = url.rfind('/')
    hexes = url[start+1:].split('-')

    colours = []
    for hex in hexes:
        rgb = []
        # convert each 2 character chunk in hex code to decimal
        for i in range(0, len(hex), 2):
            rgb.append(hexToDec(hex[i:i+2]))
        colours.append(tuple(rgb))

    return colours

def generate(arguments):
    SIZE = Xy(int(arguments['--x']), int(arguments['--y']))
    OUTFILE_EXT = 'PNG'
    OUTDIR = arguments['--outdir']
    COOLORS_URL = arguments['COOLORS_URL']
    NUM_COLOURS = 5

    im = Image.new('RGB', SIZE)
    draw = ImageDraw.Draw(im)

    if COOLORS_URL == None:
        colours = colourtools.generatePalette(NUM_COLOURS)
        TAG = '_'.join(['{}-{}-{}'.format(col.r, col.g, col.b) for col in colours])
    else:
        colours = parseCoolorsUrl(COOLORS_URL)
        TAG = COOLORS_URL[COOLORS_URL.rfind('/')+1:]

    OUTFILE = '{}/wallpaper-{}.{}'.format(OUTDIR, TAG, OUTFILE_EXT)

    stripeWidth = SIZE.x / len(colours)

    for i, colour in enumerate(colours):
        topLeft = Xy(stripeWidth * i, 0)
        bottomRight = Xy(topLeft.x + stripeWidth, SIZE.y)
        rect = (topLeft, bottomRight)

        draw.rectangle(rect, fill=colour)

    im.save(OUTFILE, 'PNG')

if __name__ == '__main__':
    print(sys.argv)
    arguments = docopt(__doc__, version='Walls 2.0')

    for c in range(int(arguments['--c'])):
        print("Generating a new wallpaper...")
        generate(arguments)

    print('Done!')
