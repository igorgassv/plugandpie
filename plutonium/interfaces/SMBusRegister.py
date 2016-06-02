from smbus import SMBus


class SMBusRegister(object):
    def __init__(self, bus: SMBus,  device_address: int, register_address: int):
        self.bus = bus
        self.device_address = device_address
        self.register_address = register_address

    def set(self, v):
        self.bus.write_byte_data(self.device_address, self.register_address, v)

    def get(self):
        return self.bus.read_byte_data(self.device_address, self.register_address)
