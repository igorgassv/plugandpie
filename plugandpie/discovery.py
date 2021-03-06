""" This module is responsible for device detection and Proxy configuration
"""
import logging
import re
from subprocess import check_output
from plugandpie.drivers.mapping import I2C_MAP

I2C_DEVICES = {}
SPI_DEVICES = {}


def i2c_detect():
    """
    Uses i2c-tools to parse all I2C addresses connected
    """
    logging.debug("Searching for new I2C devices...")
    i2tool_output = check_output(["i2cdetect", "-y", "1"]).decode("utf-8")
    addresses = [address.strip() for address in re.findall("[0-9A-Fa-f]{2} ", i2tool_output)]
    new_addresses = [address for address in addresses if address not in I2C_DEVICES]
    for address in new_addresses:
        logging.info("New I2C device found at address " + address)
        I2C_DEVICES[address] = I2C_MAP[address]


def spi_detect():
    """
    Analyse the SPI interface for connected devices
    """
    logging.debug("Searching for new SPI devices...")
    logging.error("SPI discovery was not implemented!")
    pass


def plug(proxy):
    """
    Searches for any connected device that has the wanted sensor for a device proxy.
    Crete a new driver instance and wrap it.
    :param proxy:
    :return:
    """
    i2c_detect()
    spi_detect()
    logging.info("Looking for a {} on I2C devices...".format(proxy.wanted_sensor))
    for address, device in I2C_DEVICES.items():
        if proxy.wanted_sensor in device.sensors:
            proxy.wrap(device())
            return
    logging.info("Looking for a {} on SPI devices...".format(proxy.wanted_sensor))
    logging.error("No device found with sensor {}".format(proxy.wanted_sensor))

