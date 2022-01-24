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

# static configuration
twelfth = math.pi/6
noon = 8 * twelfth

width, height = None, None
stroke_width = None
conf_dict = None
penta_minute = None
dodeca_hour = None
gnomon_radius = None
center_x, center_y = 0.7, 0.5

def path(path, file_name):
    return os.path.join(os.path.abspath(os.path.dirname(path)), file_name)

def config():
    global conf_dict
    global gnomon_radius
    global penta_minute, dodeca_hour
    global stroke_width
    global width, height

    width, height = 400, 300
    
    conf_dict = []
    with open(path(__file__, './conf.json'), 'r') as file:
        conf_dict = json.load(file)

    stroke_width = float(conf_dict['stroke']['width'])
    gnomon_radius = float(conf_dict['gnomon']['radius'])

    penta_minute = int(int(datetime.now().strftime('%M')) / 5) + 1;
    dodeca_hour = int(datetime.now().strftime('%H')) % 12;

def gnomon(hour, r0):
    r = center_y - (stroke_width * 2)
    x0 = (r - r0) * math.cos(noon + hour) + center_x
    y0 = (r - r0) * math.sin(noon + hour) + center_y

    return x0, y0

def set_context_color(context, map):
    context.set_source_rgb(float(map[0]), float(map[1]), float(map[2]))

def render():
    with cairo.SVGSurface("example.svg", width * .75, height * .75) as surface:
        context = cairo.Context(surface)
        context.scale(height * .75, height * .75)

        # set_context_color(context, conf_dict['canvas']['color'])
        # context.set_source_rgba(1, 0.0, 0.0, 0.0)
    
        context.set_line_width(stroke_width)
    
        context.arc(center_x, center_y, 0.5 - (stroke_width * 2), 0, math.pi * 2)
        # context.set_source_rgb(0.5, 0.5, 0.5)
        set_context_color(context, conf_dict['stroke']['color'])
        context.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        context.fill()
    
        context.move_to(center_x, center_y)
        context.set_source_rgb(1, 1, 1)
        context.arc(center_x, center_y, 0.5, noon + (twelfth * penta_minute), (noon + (twelfth * (penta_minute + 1))))
        context.fill()

        context.move_to(center_x, center_y)
        set_context_color(context, conf_dict['gnomon']['color'])

        xg, yg = gnomon(dodeca_hour, gnomon_radius + (stroke_width * 2))
        context.arc(xg, yg, gnomon_radius, 0, 2 * math.pi)
        context.fill()
        
        context.stroke()

config()
render()
        
cairosvg.svg2png(url="example.svg", write_to="example.png")
