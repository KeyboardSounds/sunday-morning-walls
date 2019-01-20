import random
from collections import namedtuple
import colorsys

CHANNEL_MAX = 255
Hsv = namedtuple('Hsv', ['h', 's', 'v'])
Rgb = namedtuple('Rgb', ['r', 'g', 'b'])


def generateHSV():
    return Hsv(random.random(), random.random(), random.uniform(0.5, 0.8))

def hsvToRgb(hsv):
    rgb = Rgb(*colorsys.hsv_to_rgb(hsv.h, hsv.s, hsv.v))
    rgb = Rgb(int(rgb.r*255), int(rgb.g*255), int(rgb.b*255))
    return rgb

def calcHueShift(h, degrees):
    shifted = h + (degrees/360)
    if shifted > 0:
        shifted -= 1
    return shifted

def calcTriad(primary):
    secondary = Hsv(calcHueShift(primary.h, 120), random.random(), primary.v)
    tertiary = Hsv(calcHueShift(primary.h, 240), random.random(), primary.v)
    return [primary, secondary, tertiary]

def calcTriad(primary):
    secondary = Hsv(calcHueShift(primary.h, 120), random.random(), primary.v)
    tertiary = Hsv(calcHueShift(primary.h, 240), random.random(), primary.v)
    return [primary, secondary, tertiary]

def generatePalette(numColours=3):
    palette = []

    primary = generateHSV()

    for col in calcTriad(primary):
        palette.append(hsvToRgb(col))

    return palette
