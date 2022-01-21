#!/usr/bin/env python3
from datetime import datetime

from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

import qrcode

from font_fredoka_one import FredokaOne
import requests
import json

inky = InkyWHAT("black")

font = ImageFont.truetype("./Eaglefeather-BoldItalic.ttf", 34)
# img = Image.new("P", (inky.WIDTH, inky.HEIGHT))

# draw = ImageDraw.Draw(img)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

date = datetime.now().strftime('%A %B %d %H:%M%p')
qr.add_data(date)
qr.make(fit=True)

qi = qr.make_image(fill_color="black", back_color="white")

img = qi.resize((inky.WIDTH, inky.HEIGHT))

def date():
    date = datetime.now().strftime('%A %B %d %H:%M%p')
    w,h = font.getsize(date)
    draw.text((0, 6*h + h/2), date, inky.BLACK, font=font)

def location():
    loc = requests.get('https://ipinfo.io').json()
    locstr = loc['city'] + ' ' + loc['region'] + ' ' + loc['postal']
    draw.text((0, 16), locstr, inky.BLACK, font=font)

# date()
# location()

inky.set_image(img.rotate(180))
inky.show()
