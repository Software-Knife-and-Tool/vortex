#
# vortex
#
.PHONY: lint venv src

install:
	@apt-get -y -qq install python3-pip
	@apt-get -y -qq install python-dev
	@apt-get -y -qq install python3-dev
	@apt-get -y -qq install python3-setuptools
	@apt-get -y -qq install python-setuptools
	@apt-get -y -qq install libjpeg-dev zlib1g-dev
	@apt-get -y -qq install libcairo2-dev
	@apt-get -y -qq install pkg-config
	@apt-get -y -qq install cairosvg

	@pip3 -q install Pillow
	@pip3 -q install wiringpi
	@pip3 -q install pycairo
	@pip3 -q install inky[rpi]

	@git clone https://github.com/doceme/py-spidev.git
	@(cd py-spidev; make ; make install)

clobber:
	@sudo rm -rf ./py-spidev
