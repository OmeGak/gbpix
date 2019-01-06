# gbpix

`gbpix` is a command-line tool for processing GameBoy Camera pictures as exported with [BitBoy](http://gameboyphoto.bigcartel.com/product/bitboy).

Features:
- Export to JPEG
- Remove frame
- Scale up

## Why?

BitBoy exports pictures in BMP format.
This is not ideal for sharing them online, as few services accept the format.

Also, GameBoy Camera pictures feature cute frames, that, although charismatic, get old fast and don't quite cut it for art galleries.

Finally, the original resolution of pictures is `128 x 112` and websites tend to scale up pictures if they are too small.
The problem with this is that it will, most likely, destroy the crispiness of the picture, as pixels will not be preserved thanks to their smart algorithms.
`gbpix` resizes pictures to `1024 x 896`, large enough to avoid server-side post-processing in most cases, while preserving their characteristic crispiness by using the good ol' nearest neighbor.

## Install

```shell
git clone https://github.com/OmeGak/gbpix.git
cd gbpix
pipenv install
```

## Usage

Process single picture:

```shell
pipenv shell
gbpix GB_0001.BMP
```

Process all BMP pictures in a directory:

```shell
gbpix .
```
