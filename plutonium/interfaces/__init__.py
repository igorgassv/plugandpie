from plutonium.interfaces.I2CInterface import I2CInterface
from plutonium.interfaces.SMBus import SMBusInterface

i2c = {1: I2CInterface(1)}
smbus = {1: SMBusInterface(1)}

i2c[1].open()
