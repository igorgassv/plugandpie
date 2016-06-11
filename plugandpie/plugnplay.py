""" This module is responsible for device detection and Proxy configuration
"""
from plugandpie.common.utils import i2c_addresses
from plugandpie.drivers.mapping import DRIVER_MAP

DEVICES = {}


def plug(proxy, sensor):
    """ Finds a sensor to plug in the specified proxy.
    """
    addresses = i2c_addresses()
    # Update device list
    for address in addresses:
        if address not in DEVICES.keys():
            device = DRIVER_MAP[address]()
            DEVICES[address] = device
    # Plug any device that has the required sensor
    for device in DEVICES.values():
        if sensor in device.sensors:
            proxy.wrap(device)
