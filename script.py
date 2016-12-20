from __future__ import unicode_literals, print_function

import os

import click
from PIL import Image

FRAME_PX = 16

click.disable_unicode_literals_warning = True


def crop_frame(img):
    xsize, ysize = img.size
    box = (FRAME_PX, FRAME_PX, xsize - FRAME_PX, ysize - FRAME_PX)
    return img.crop(box)


def resize(img, scale=2):
    power = scale - 1
    ratio = 2 ** power
    xsize, ysize = img.size
    newsize = xsize * ratio, ysize * ratio
    return img.resize(newsize, Image.NEAREST)


@click.command()
@click.argument('infile', type=click.Path(exists=True, dir_okay=False))
def cli(infile):
    filename, _ = os.path.splitext(infile)
    outfile = filename + '.jpg'
    img = Image.open(infile)
    img = crop_frame(img)
    img = resize(img, scale=4)
    img.save(outfile, format='JPEG')
