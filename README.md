# Vortex Instrument Labs - Vortex E-Ink Clocks

_Beating Yesterday's Technology Senseless_

A series of Python experiments using the 

*Pimoroni Inky e-ink WHAT* (https://shop.pimoroni.com/products/inky-what?variant=13590497624147)</br>
*Pimoroni Inky e-ink Impression 4* (https://shop.pimoroni.com/products/inky-impression-4?variant=39599238807635

Animation isn't really possible, but it should be an acceptable target for static output.

### System preparation

You'll need an RPi with a recent install of Raspberry Pi OS and I2C/SPI enabled.

### Installing

`sudo make install`

will install the Pimoroni driver and all the Python support.

If you need to reinstall for some reason,

`sudo make clobber`

first.

### Running the Mondrian clock

mondrian for the WHAT and mondrian4 for the Impression 4

`cd src/mondrian`
`nohup ./clock.sh > /dev/null`

should get you a simple geometric clock face more or less at 5 minute intervals.
