from plutonium.interfaces.Interface import Interface

import smbus


class SMBusInterface(Interface):
    def __init__(self, bus_number):
        self.bus = smbus.SMBus(bus_number)

    def write_byte(self, device_address, register_address, byte):
        self.bus.write_byte_data(device_address, register_address, byte)

    def write_bytes(self, device_address, register_address, byte_sequence):
        self.bus.write_i2c_block_data(device_address, register_address, byte_sequence)

    def read_byte(self, device_address, register_address):
        return self.bus.read_byte_data(device_address, register_address)

    def read_bytes(self, device_address, register_address, number_of_bytes):
        return self.bus.read_i2c_block_data(device_address, register_address, number_of_bytes)


class SMBusRegister(object):
    def __init__(self, interface: Interface,  device_address: int, register_address: int):
        self.interface = interface
        self.device_address = device_address
        self.register_address = register_address

    def set(self, v):
        self.interface.write_byte(self.device_address, self.register_address, v)

    def get(self):
        return self.interface.read_byte(self.device_address, self.register_address)
