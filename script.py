from __future__ import unicode_literals, print_function

import os
from glob import glob

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


def process(infile):
    filename, _ = os.path.splitext(infile)
    outfile = filename + '.jpg'
    click.echo("  {} -> {}".format(infile, outfile))
    img = Image.open(infile)
    img = crop_frame(img)
    img = resize(img, scale=4)
    img.save(outfile, format='JPEG')


@click.command()
@click.argument('path', type=click.Path(exists=True))
def cli(path):
    if not os.path.isdir(path):
        process(path)
    else:
        filenames = glob('{}/*.BMP'.format(path))
        click.echo("{} GameBoy Camera pics found!".format(len(filenames)))
        for filename in filenames:
            process(filename)
