# *Vortex* SVG e-ink display

A series of Python experiments using the *Pimoroni Inky e-ink what* (https://shop.pimoroni.com/products/inky-what?variant=13590497624147)
as an auxiliary grayscale display. Animation isn't really possible, but it should be an acceptable target for static SVG output.

### System preparation

You'll need an RPi with a recent install of Raspbian and SPI enabled.

### Installing

`sudo make install`

will install the Pimoroni driver, compile and install the Python SPI driver, and all the Python support.

If you need to reinstall for some reason,

`sudo make clobber`

first.

### Running the moon phase clock

`cd src/moon`
`nohup ./moon.sh > /dev/null`

should get you a moon phase clock more or less at 5 minute intervals.

### Next

Python SVG (maybe Cairo) and cleanup.
