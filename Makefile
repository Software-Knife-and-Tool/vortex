#
# vortex
#
.PHONY: lint venv src

install:
	@apt-get -y install python3-pip
	@apt-get -y install python-dev
	@apt-get -y install python3-dev
	@apt-get install python3-setuptools
	@apt-get install python-setuptools
	@apt-get install libjpeg-dev zlib1g-dev
	@pip3 install Pillow
	@pip3 install wiringpi
	@git clone https://github.com/doceme/py-spidev.git
	@(cd py-spidev; make ; make install)
	@pip3 install inky[rpi]

clobber:
	@sudo rm -rf ./py-spidev
