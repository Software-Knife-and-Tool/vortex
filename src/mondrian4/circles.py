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

import argparse
import time

from inky.auto import auto
inky_display = auto(ask_user=True, verbose=False)

# static configuration
twelfth = math.pi/6
noon = 8 * twelfth

width, height = None, None
face_width = None
conf_dict = None
penta_minute = None
dodeca_hour = None
gnomon_radius = None
center_x, center_y = .825, 0.55

def path(path, file_name):
    return os.path.join(os.path.abspath(os.path.dirname(path)), file_name)

def config():
    global conf_dict
    global gnomon_radius
    global penta_minute, dodeca_hour
    global face_width
    global width, height

    width, height = 640, 400
    
    conf_dict = []
    with open(path(__file__, './conf.json'), 'r') as file:
        conf_dict = json.load(file)

    face_width = float(conf_dict['face']['width'])
    gnomon_radius = float(conf_dict['gnomon']['radius'])

    penta_minute = int(int(datetime.now().strftime('%M')) / 5) + 1;
    dodeca_hour = int(datetime.now().strftime('%H')) % 12;

def gnomon_pos(hour, r0):
    r = center_y - ((face_width * 2) * 3)
    x0 = (r - r0) * math.cos(noon + ((hour + 1) * twelfth)) + center_x
    y0 = (r - r0) * math.sin(noon + ((hour + 1) * twelfth)) + center_y

    return x0, y0

def set_context_color(context, map):
    context.set_source_rgb(float(map[0]), float(map[1]), float(map[2]))

def float_of(dict, name, minor):
    return float(dict[name][minor])
    
def render():
    with cairo.SVGSurface("example.svg", width * .75, height * .75) as surface:
        context = cairo.Context(surface)
        context.scale(height * .70, height * .70)

        context.set_line_width(face_width)

        # render clock face
        context.arc(center_x, center_y, 0.5 - (face_width * 2), 0, math.pi * 2)
        set_context_color(context, conf_dict['face']['color'])
        context.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        context.fill()

        # render minutes arc
        context.move_to(center_x, center_y)
        context.arc(center_x, center_y, 0.5, noon + (twelfth * penta_minute), (noon + (twelfth * (penta_minute + 1))))
        set_context_color(context, conf_dict['minutes']['color'])
        context.fill()

        # render gnomon
        context.move_to(center_x, center_y)
        set_context_color(context, conf_dict['gnomon']['color'])

        xg, yg = gnomon_pos(dodeca_hour, gnomon_radius + (face_width * 2))
        context.arc(xg, yg, gnomon_radius, 0, 2 * math.pi)
        context.fill()

        # render from conf
        render_list = conf_dict["render"]
        for obj in render_list:
            type = list(obj.keys())[0]
            context.save()
            if type == 'cx':
                context.arc(float_of(obj, 'cx', 'x'),
                            float_of(obj, 'cx', 'y'),
                            float_of(obj, 'cx', 'r'),
                            0, 2 * math.pi)
            elif type == 'ln':
                context.set_line_width(float_of(obj, 'ln', 'w'))
                set_context_color(context, obj['ln']['color'])
                context.move_to(float_of(obj, 'ln', 'x0'),
                                float_of(obj, 'ln', 'y0'))
                context.line_to(float_of(obj, 'ln', 'x1'),
                                float_of(obj, 'ln', 'y1'))
            context.fill()
            context.restore()

        context.stroke()

config()
render()
        
cairosvg.svg2png(url="example.svg", write_to="example.png")
