""" This module is a collection of standalone utility functions used throughout the package.
"""
import re
from subprocess import check_output


def i2c_addresses():
    """
    Uses i2c-tools to parse all I2C addresses connected
    :return: a list of addresses detected on the I2C
    """
    address_map = check_output(["i2cdetect", "-y", "1"]).decode("utf-8")
    return [address.strip() for address in re.findall("[0-9A-Fa-f]{2} ", address_map)]


def twos_complement(value, bits):
    """Signs a value with an arbitrary number of bits."""
    if value >= (1 << (bits - 1)):
        value = -((~value + 1) + (1 << bits))
    return value
