#!/usr/bin/env python3
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

import requests
from datetime import datetime
font = ImageFont.truetype("./Eaglefeather-BoldItalic.ttf", 24)

# dithering support
# Set up the inky wHAT display and border colour
inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)

# Open our image
img = Image.open("./orb.png")

# Get the width and height of the image
w, h = img.size

# Calculate the new height and width of the image
h_new = 300
w_new = int((float(w) / h) * h_new)
w_cropped = 400

# Resize the image with high-quality resampling
img = img.resize((w_new, h_new), resample=Image.LANCZOS)

# Calculate coordinates to crop image to 400 pixels wide
x0 = (w_new - w_cropped) / 2
x1 = x0 + w_cropped
y0 = 0
y1 = h_new

# Crop image
img = img.crop((x0, y0, x1, y1))

# Convert the image to use a white / black / red colour palette
pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

img = img.convert("RGB").quantize(palette=pal_img)
text = ImageDraw.Draw(img)

# dynamic values
date = datetime.now().strftime('%A %B %d %H:%M%p')

def date():
    date = datetime.now().strftime('%A %B %d %H:%M%p')
    w,h = font.getsize(date)
    text.text((54, 0), date, inky_display.BLACK, font=font)

date()

inky_display.set_image(img.rotate(180))
inky_display.show()
