#!/usr/bin/env python3
import cairo
import cairosvg

#
# the display code will resample the image down to 400 by 300
# so the only thing that matters is that we get the aspect ratio
# right. The Inky display is 400 x 300.
#

#
# don't get fancy with colors, we're dithered monochrome grayscale on
# the output end. gradients and such should probably be restained.
#
with cairo.SVGSurface("example.svg", 400 * .75, 300 * .75) as surface:
    context = cairo.Context(surface)
    x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
    x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
    context.set_source_rgba(1, 1.0, 1.0, 1.0)
    context.scale(400 * .75, 300 * .75)
    context.set_line_width(0.04)
    context.move_to(x, y)
    context.curve_to(x1, y1, x2, y2, x3, y3)
    context.stroke()
    context.set_source_rgba(1, 0.5, 0.5, 0.5)
    context.set_line_width(0.02)
    context.move_to(x, y)
    context.line_to(x1, y1)
    context.move_to(x2, y2)
    context.line_to(x3, y3)
    context.stroke()

cairosvg.svg2png(url="example.svg", write_to="example.png")
