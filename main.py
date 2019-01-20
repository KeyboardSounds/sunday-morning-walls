from PIL import Image, ImageDraw
from collections import namedtuple

Xy = namedtuple('Xy', ['x', 'y'])

# Screen Resolution
SIZE = Xy(1800, 1200)
OUTFILE_EXT = 'PNG'
OUTDIR = 'out'
COOLORS_URL = 'https://coolors.co/533a71-6184d8-50c5b7-9cec5b-f0f465'
TAG = COOLORS_URL[COOLORS_URL.rfind('/')+1:] # just the color code part of the url
OUTFILE = '{}/wallpaper-{}.{}'.format(OUTDIR, TAG, OUTFILE_EXT)

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

im = Image.new('RGB', SIZE)
draw = ImageDraw.Draw(im)

colours = parseCoolorsUrl(COOLORS_URL)

stripeWidth = SIZE.x / len(colours)

for i, colour in enumerate(colours):
    topLeft = Xy(stripeWidth * i, 0)
    bottomRight = Xy(topLeft.x + stripeWidth, SIZE.y)
    rect = (topLeft, bottomRight)

    draw.rectangle(rect, fill=colour)

im.save(OUTFILE, 'PNG')
print('Done!')
