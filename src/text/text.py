#!/usr/bin/env python3
##########
##
##  SPDX-License-Identifier: MIT
##
##  Copyright (c) 2022 James M. Putnam <putnamjm.design@gmail.com>
##
##########

##########
##
## text utilities
##
###########

import os
import json
import cairo

"""text: json text utilities
"""

WIDTH = 3
HEIGHT = 2
PIXEL_SCALE = 200

conf_dict = None

def path(path, file_name):
    """make an absolute path to file
    """
    return os.path.join(os.path.abspath(os.path.dirname(path)), file_name)

# static configuration
conf_dict = []
with open(path(__file__, './fonts.json'), 'r') as file:
    conf_dict = json.load(file)

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             WIDTH*PIXEL_SCALE,
                             HEIGHT*PIXEL_SCALE)
x
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Drawing code
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(0.25)

arial = conf_dict['arial']
ctx.select_font_face(arial['face'],
                     getattr(cairo, arial["style"]),
                     getattr(cairo, arial["weight"]))

ctx.move_to(0.5, 0.5)
ctx.show_text('Drawing text')

surface.write_to_png('text.png')
