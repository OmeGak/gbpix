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


def ensure_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def archive(infile, archivedir, force=False):
    basename = os.path.basename(infile)
    archivefile = os.path.join(archivedir, basename)
    if os.path.exists(archivedir) and not force:
        click.echo("  original couldn't be archived ({} already exists)".format(archivedir))
        return
    ensure_dir(archivedir)
    os.rename(infile, archivefile)
    click.echo("  original archived as {}".format(archivefile))


def process(infile, force=False, archivedir=None, outdir=None):
    dirname, basename = os.path.split(infile)
    filename, _ = os.path.splitext(basename)
    if outdir:
        ensure_dir(outdir)
        dirname = outdir
    outfile = os.path.join(dirname, filename + '.jpg')
    if os.path.exists(outfile) and not force:
        click.echo("  {} skipped! ({} already exists)".format(infile, outfile))
        return
    click.echo("  {} -> {}".format(infile, outfile))
    img = Image.open(infile)
    img = crop_frame(img)
    img = resize(img, scale=4)
    img.save(outfile, format='JPEG')
    if archivedir:
        archive(infile, archivedir, force=force)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--force', '-f', is_flag=True)
@click.option('--archivedir', '-a', default=None)
@click.option('--outdir', '-o', default=None)
def cli(path, force, archivedir, outdir):
    if not os.path.isdir(path):
        process(path, force=force, archivedir=archivedir, outdir=outdir)
    else:
        filenames = glob('{}/*.BMP'.format(path))
        click.echo("{} GameBoy Camera pics found!".format(len(filenames)))
        for filename in filenames:
            process(filename, force=force, archivedir=archivedir, outdir=outdir)
