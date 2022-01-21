#!/usr/bin/env python3
from datetime import datetime
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

from font_fredoka_one import FredokaOne
import requests
import json

inky = InkyWHAT("black")

font = ImageFont.truetype("./Eaglefeather-BoldItalic.ttf", 34)
img = Image.new("P", (inky.WIDTH, inky.HEIGHT))

draw = ImageDraw.Draw(img)

def date():
    date = datetime.now().strftime('%A %B %d %H:%M%p')
    w,h = font.getsize(date)
    draw.text((0, 6*h + h/2), date, inky.BLACK, font=font)

def location():
    loc = requests.get('https://ipinfo.io').json()
    locstr = loc['city'] + ' ' + loc['region'] + ' ' + loc['postal']
    draw.text((0, 16), locstr, inky.BLACK, font=font)

date()
location()

inky.set_image(img.rotate(180))
inky.show()
