#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import time

from inky.auto import auto
from PIL import Image

inky_display = auto(ask_user=True, verbose=False)

# Command line arguments to determine number of cycles to run
parser = argparse.ArgumentParser()
parser.add_argument('--number', '-n', type=int, required=False, help="number of cycles")
args = parser.parse_args()

cycles = 2

colours = (inky_display.BLACK, inky_display.WHITE)
colour_names = (inky_display.colour, "black", "white")
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

for i in range(cycles):
    for j, c in enumerate(colours):
        inky_display.set_border(c)
        for x in range(inky_display.WIDTH):
            for y in range(inky_display.HEIGHT):
                img.putpixel((x, y), c)
        inky_display.set_image(img)
        inky_display.show()
        time.sleep(1)
