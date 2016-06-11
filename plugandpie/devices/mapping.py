"""This module contains the curated map between I2C addresses and device drivers automatically detected."""
from plugandpie.devices import MMA8452Q

DRIVER_MAP = {
    "1d": MMA8452Q
}