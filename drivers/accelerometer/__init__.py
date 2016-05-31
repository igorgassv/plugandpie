from abc import ABC, abstractmethod
from common.i2c import *

STANDARD_GRAVITY = 9.80665

DEFAULT_I2C_BUS = 1
DEFAULT_I2C_ADDRESS = 0x1d


class Accelerometer(I2CMaster, ABC):
    def __init__(self,
                 i2c_bus=DEFAULT_I2C_BUS,
                 i2c_address=DEFAULT_I2C_ADDRESS):
        super().__init__(i2c_bus)
        self.i2c_address = i2c_address

    def __enter__(self):
        super().__enter__()
        self.init()
        return self

    def init(self):
        """Initalises the accelerometer2 with some default values."""
        self.standby()
        self.set_output_data_rate(800)  # Hz
        self.set_g_range(2)
        self.activate()

    @abstractmethod
    def reset(self):
        """Resets the accelerometer2."""

    @abstractmethod
    def activate(self):
        """Start recording the accelerometer2 values. Call this after
        changing any settings.
        """

    @abstractmethod
    def standby(self):
        """Stop recording the accelerometer2 values. Call this before
        changing any settings.
        """

    @abstractmethod
    def get_xyz(self, raw=False, res12=True):
        """Returns the x, y and z values as a dictionary. By default it returns
        signed values at 12-bit resolution. You can specify a lower resolution
        (8-bit) or request the raw register values. Signed values are
        in G's. You can alter the recording range with `set_g_range()`.

        :param raw: If True: return raw, unsigned data, else: sign values
        :type raw: boolean (default: False)
        :param res12: If True: read 12-bit resolution, else: 8-bit
        :type res12: boolean (default: True)
        """

    @abstractmethod
    def set_g_range(self, g_range):
        """Sets the force range (in Gs -- where 1G is the force of gravity).

        Be sure to call `standby()` before using this method and `activate()`
        after using this method.

        :param g_range: The force range in Gs.
        :type g_range: int (acceptable ranges: 2, 4 or 8)
        """

    @abstractmethod
    def set_output_data_rate(self, output_data_rate):
        """Sets the output data rate in Hz.

        Be sure to call `standby()` before using this method and `activate()`
        after using this method.

        :param output_data_rate: The output data rate.
        :type output_data_rate: int (acceptable rates: 800, 400, 200, 100,
                                50, 12.5, 6.25, 1.56)
        """