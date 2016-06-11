"""
This module implements the Interface and Register base classes for communication with
the devices through any standard (I2C/SMBus and SPI).
"""


class Interface(object):
    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def write_byte(self, device_address, register_address, byte):
        raise NotImplementedError()

    def write_bytes(self, device_address, register_address, byte_sequence):
        raise NotImplementedError()

    def read_byte(self, device_address, register_address):
        raise NotImplementedError()

    def read_bytes(self, device_address, register_address, number_of_bytes):
        raise NotImplementedError()


class Register(object):
    def __init__(self, interface,  device_address, register_address):
        self.interface = interface
        self.device_address = device_address
        self.register_address = register_address
        self._cached_value = None

    def set(self, v):
        self.interface.write_byte(self.device_address, self.register_address, v)
        self._cached_value = v

    def get(self, cached=False):
        if cached and self._cached_value is not None:
            return self._cached_value
        self._cached_value = self.interface.read_byte(self.device_address, self.register_address)
        return self._cached_value
