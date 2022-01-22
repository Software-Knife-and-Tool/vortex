#!/usr/bin/env python3
import cairo
import cairosvg
import math
from datetime import datetime

width = 400
height = 300
twelfth = math.pi/6
hand = 8 * twelfth

sw = 0.015 # stroke width
penta_minute = int(int(datetime.now().strftime('%M')) / 5);
dodeca_hour = int(datetime.now().strftime('%H')) % 12;

# print(penta_minute);
# print(dodeca_hour);

penta = penta_minute + 1

with cairo.SVGSurface("example.svg", width * .75, height * .75) as surface:
    context = cairo.Context(surface)
    context.scale(height * .75, height * .75)
    context.set_source_rgba(1, 1.0, 1.0, 1.0)
    context.set_line_width(sw)
    # x, y, radius, starting angle, sweep
    context.arc(0.7, 0.5, .5 - sw * 2, 0, 2 * 3.1415)
    context.set_source_rgb(0.5, 0.5, 0.5)
    context.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
    context.fill()

    context.move_to(0.7, 0.5)
    context.arc(0.7, 0.5, 0.5, hand + (twelfth * penta), (hand + (twelfth * (penta + 1))))
    # context.close_path()
    context.set_source_rgb(1, 1, 1)
    context.fill()

    context.stroke()

cairosvg.svg2png(url="example.svg", write_to="example.png")
