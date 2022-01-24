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

"""text: json text utilities
"""

import os
import json
import cairo
import cairosvg
import math
from datetime import datetime

width = 400
height = 300
twelfth = math.pi/6

# static configuration
noon = 8 * twelfth
sw = 0.015 # stroke width

conf_dict = None
penta_minute = None
dodeca_hour = None
penta = None

def path(path, file_name):
    return os.path.join(os.path.abspath(os.path.dirname(path)), file_name)

def config():
    global conf_dict
    global penta_minute
    global dodeca_hour
    global penta
    
    conf_dict = []
    with open(path(__file__, './conf.json'), 'r') as file:
        conf_dict = json.load(file)
    penta_minute = int(int(datetime.now().strftime('%M')) / 5);
    dodeca_hour = int(datetime.now().strftime('%H')) % 12;
    penta = penta_minute + 1

def gnomon(hour, r0):
    r = .5 - sw * 2
    x0 = (r - r0) * math.cos(hour) + 0.7
    y0 = (r - r0) * math.sin(hour) + 0.5
    return x0, y0

def render():
    with cairo.SVGSurface("example.svg", width * .75, height * .75) as surface:
        context = cairo.Context(surface)
        context.scale(height * .75, height * .75)
        context.set_source_rgba(1, 1.0, 1.0, 1.0)
    
        context.set_line_width(sw)
    
        context.arc(0.7, 0.5, .5 - sw * 2, 0, 2 * 3.1415)
        context.set_source_rgb(0.5, 0.5, 0.5)
        context.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        context.fill()
    
        context.move_to(0.7, 0.5)
        context.set_source_rgb(1, 1, 1)
        context.arc(0.7, 0.5, 0.5, noon + (twelfth * penta), (noon + (twelfth * (penta + 1))))
        context.fill()

        context.move_to(0.7, 0.5)
        context.set_source_rgb(0, 0, 0)

        xg, yg = gnomon(dodeca_hour, .04 + sw * 2)
        context.arc(xg, yg, 0.04, 0, 2 * math.pi)
        context.fill()
        
        context.stroke()

config()
render()
        
cairosvg.svg2png(url="example.svg", write_to="example.png")
