import time
from plutonium.common.utils import *
from plutonium.devices.mapping import driver_map


class Proxy:
    MAX_TRIES = 5
    TRY_INTERVAL = 0.2

    def __init__(self, target):
        self._target = target
        self._obj = None
        self._tries = 0

    def __getattribute__(self, name):
        """
        If attribute is not local to proxy, look at the wrapped object.
        If wrapped object is still None, wait a little bit and try again.
        (It might take some time to configure the device drivers after startup)
        After a number of tries, give up with AttributeError
        """
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            if self._obj is not None:
                return getattr(self._obj, name)
            else:
                self._tries += 1
                if self._tries > 5:
                    self._tries = 0
                    raise AttributeError("Proxy has no wrapped object plugged")
                else:
                    time.sleep(Proxy.TRY_INTERVAL)
                    plug(self, self._target)
                    getattr(self, name)


accelerometer = Proxy('accelerometer')
thermometer = Proxy('thermometer')

DEVICES = {}


def plug(proxy: Proxy, sensor: str):
    addresses = i2c_addresses()
    # Update devices list
    for address in addresses:
        if address not in DEVICES.keys():
            device = driver_map[address]()
            DEVICES[address] = device
    # Plug any device that has the required sensor
    for device in DEVICES.values():
        if sensor in device.sensors:
            proxy._obj = device
