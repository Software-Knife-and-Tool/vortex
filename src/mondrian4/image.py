#!/usr/bin/env python3

import sys
import numpy as np

from PIL import Image

from inky.auto import auto

def alpha_composite(front, back):
    front = np.asarray(front)
    back = np.asarray(back)
    result = np.empty(front.shape, dtype='float')
    alpha = np.index_exp[:, :, 3:]
    rgb = np.index_exp[:, :, :3]
    falpha = front[alpha] / 255.0
    balpha = back[alpha] / 255.0
    result[alpha] = falpha + balpha * (1 - falpha)
    old_setting = np.seterr(invalid='ignore')
    result[rgb] = (front[rgb] * falpha + back[rgb] * balpha * (1 - falpha)) / result[alpha]
    np.seterr(**old_setting)
    result[alpha] *= 255
    np.clip(result, 0, 255)
    # astype('uint8') maps np.nan and np.inf to 0
    result = result.astype('uint8')
    result = Image.fromarray(result, 'RGBA')
    return result

def alpha_composite_with_color(image, color=(255, 255, 255)):
    back = Image.new('RGBA', size=image.size, color=color + (255,))
    return alpha_composite(image, back)

inky = auto(ask_user=True, verbose=True)
saturation = 0.50

if len(sys.argv) == 1:
    print("""
Usage: {file} image-file
""".format(file=sys.argv[0]))
    sys.exit(1)

image = Image.open(sys.argv[1])
convertedimage = image.resize(inky.resolution)
# convertedimage = convertedimage.convert("RGB");
convertedimage = convertedimage.rotate(180);
convertedimage = alpha_composite_with_color(convertedimage, color=(192, 192, 192));

if len(sys.argv) > 2:
    saturation = float(sys.argv[2])

inky.set_image(convertedimage, saturation=saturation)
inky.show()
