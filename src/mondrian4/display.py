#!/usr/bin/env python3
import sys
import requests

from inky.auto import auto

inky_display = auto(ask_user=True, verbose=True)

from PIL import Image, ImageDraw

# dithering support

# Open our image
img = Image.open(sys.argv[1])

# Get the width and height of the image
w, h = img.size

# Calculate the new height and width of the image
h_new = 400
w_new = int((float(w) / h) * h_new)
w_cropped = 640

# Resize the image with high-quality resampling
img = img.resize((w_new, h_new), resample=Image.LANCZOS)

# Calculate coordinates to crop image to 640 pixels wide
x0 = (w_new - w_cropped) / 2
x1 = x0 + w_cropped
y0 = 0
y1 = h_new

# Crop image
img = img.crop((x0, y0, x1, y1))

# Convert the image to use a white / black colour palette
pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0) + (0, 0, 0) * 253)

# img = img.convert("RGBA").quantize(palette=pal_img)
img = img.convert("1")

inky_display.set_image(img.rotate(180))
inky_display.show()
