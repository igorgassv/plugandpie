""" This module is responsible for device detection and Proxy configuration
"""
import re
from subprocess import check_output
from plugandpie.drivers.mapping import DRIVER_MAP

I2C_DEVICES = {}
SPI_DEVICES = {}


def i2c_detect():
    """
    Uses i2c-tools to parse all I2C addresses connected
    """
    i2tool_output = check_output(["i2cdetect", "-y", "1"]).decode("utf-8")
    addresses = [address.strip() for address in re.findall("[0-9A-Fa-f]{2} ", i2tool_output)]
    new_addresses = [address for address in addresses not in I2C_DEVICES]
    for address in new_addresses:
        I2C_DEVICES[address] = None


def spi_detect():
    pass


def i2c_plug():
    i2c_detect()


def plug():
    print ("Searching...")
    pass
