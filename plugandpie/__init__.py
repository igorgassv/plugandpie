"""A package for ease of access to sensors data on Raspberry Pi

Standard sensor accessors:
- accelerometer
- thermometer
"""
from plugandpie.device.Proxy import Proxy

accelerometer = Proxy('accelerometers')
thermometer = Proxy('thermometer')

