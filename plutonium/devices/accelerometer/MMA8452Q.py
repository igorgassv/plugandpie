from plutonium.common.utils import twos_complement
from plutonium.devices.accelerometer.Accelerometer import Accelerometer
from plutonium.interfaces.SMBus import SMBusRegister
from plutonium.interfaces import smbus

DEFAULT_I2C_BUS = 1
DEFAULT_I2C_ADDRESS = 0x1d

# register values
# CTRL_REG1 Register (Read/Write)
# +------------+------------+-------+-------+------+--------+--------+--------+
# | bit 7      | bit 6      | bit 5 | bit 4 | bit 3| bit 2  | bit 1  | bit 0  |
# +------------+------------+-------+-------+------+--------+--------+--------+
# | ASLP_RATE1 | ASLP_RATE0 | DR2   | DR1   | DR0  | LNOISE | F_READ | ACTIVE |
# +------------+------------+-------+-------+------+--------+--------+--------+
CTRL_REG1_SET_ACTIVE = 0x01
# DR2 DR1 DR0
CTRL_REG1_ODR_800 = 1 << 3  # period = 1.25 ms
CTRL_REG1_ODR_400 = 2 << 3  # period = 2.5 ms
CTRL_REG1_ODR_200 = 3 << 3  # period = 5 ms
CTRL_REG1_ODR_100 = 4 << 3  # period = 10 ms
CTRL_REG1_ODR_50 = 5 << 3  # period = 20 ms
CTRL_REG1_ODR_12_5 = 6 << 3  # period = 80 ms
CTRL_REG1_ODR_6_25 = 7 << 3  # period = 160 ms
CTRL_REG1_ODR_1_56 = 8 << 3  # period = 640 ms

# XYZ_DATA_CFG (Read/Write)
# +-------+-------+-------+---------+-------+-------+-------+-------+
# | bit 7 | bit 6 | bit 5 | bit 4   | bit 3 | bit 2 | bit 1 | bit 0 |
# +-------+-------+-------+---------+-------+-------+-------+-------+
# | 0     | 0     | 0     | HPF_OUT | 0     | 0     | FS1   | FS0   |
# +-------+-------+-------+---------+-------+-------+-------+-------+
XYZ_DATA_CFG_FSR_2G = 0x00
XYZ_DATA_CFG_FSR_4G = 0x01
XYZ_DATA_CFG_FSR_8G = 0x02


STANDARD_GRAVITY = 9.80665


class MMA8452Q(Accelerometer):
    STATUS = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x00)
    OUT_X_MSB = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x01)
    OUT_X_LSB = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x02)
    OUT_Y_MSB = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x03)
    OUT_Y_LSB = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x04)
    OUT_Z_MSB = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x05)
    OUT_Z_LSB = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x06)
    SYSMOD = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x0B)
    INT_SOURCE = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x0C)
    WHO_AM_I = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x0D)
    XYZ_DATA_CFG = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x0E)
    HP_FILTER_CUTOFF = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x0F)
    PL_STATUS = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x10)
    PL_CFG = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x11)
    PL_COUNT = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x12)
    PL_BF_ZCOMP = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x13)
    P_L_THS_REG = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x14)
    FF_MT_CFG = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x15)
    FF_MT_SRC1 = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x16)
    FF_MT_SRC2 = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x17)
    FF_MT_COUNT = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x18)
    TRANSIENT_CFG = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x1D)
    TRANSIENT_THS = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x1F)
    TRANSIENT_COUNT = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x20)
    PULSE_CFG = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x21)
    PULSE_SRC = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x22)
    PULSE_THSX = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x23)
    PULSE_THSY = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x24)
    PULSE_THSZ = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x25)
    PULSE_TMLT = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x26)
    PULSE_LTCY = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x27)
    PULSE_WIND = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x28)
    ASLP_COUNT = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x29)
    CTRL_REG1 = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x2A)
    CTRL_REG2 = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x2B)
    CTRL_REG3 = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x2C)
    CTRL_REG4 = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x2D)
    CTRL_REG5 = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x2E)
    OFF_X = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x2F)
    OFF_Y = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x30)
    OFF_Z = SMBusRegister(smbus[DEFAULT_I2C_BUS], DEFAULT_I2C_ADDRESS, 0x31)

    def __init__(self, i2c_bus=DEFAULT_I2C_BUS, i2c_address=DEFAULT_I2C_ADDRESS):
        super().__init__(smbus[i2c_bus])
        self.i2c_address = i2c_address
        # cache control registers
        self._XYZ_DATA_CFG_VALUE = 0
        self._CTRL_REG1_VALUE = 0

    def init(self):
        """Initialises the accelerometer2 with some default values."""
        self.standby()
        self.set_output_data_rate(800)  # Hz
        self.set_g_range(2)
        self.activate()

    def reset(self):
        """Resets the accelerometer2."""
        self._CTRL_REG1_VALUE = 0
        self.CTRL_REG1.set(self._CTRL_REG1_VALUE)

    def activate(self):
        """Start recording the accelerometer2 values. Call this after
        changing any settings.
        """
        self._CTRL_REG1_VALUE |= CTRL_REG1_SET_ACTIVE
        self.CTRL_REG1.set(self._CTRL_REG1_VALUE)

    def standby(self):
        """Stop recording the accelerometer2 values. Call this before
        changing any settings.
        """
        self._CTRL_REG1_VALUE &= 0xff ^ CTRL_REG1_SET_ACTIVE
        self.CTRL_REG1.set(self._CTRL_REG1_VALUE)

    def set_g_range(self, g_range):
        """Sets the force range (in Gs -- where 1G is the force of gravity).

        Be sure to call `standby()` before using this method and `activate()`
        after using this method.

        :param g_range: The force range in Gs.
        :type g_range: int (acceptable ranges: 2, 4 or 8)
        """
        g_ranges = {2: XYZ_DATA_CFG_FSR_2G,
                    4: XYZ_DATA_CFG_FSR_4G,
                    8: XYZ_DATA_CFG_FSR_8G}
        if g_range in g_ranges:
            self._XYZ_DATA_CFG_VALUE &= 0b11111100
            self._XYZ_DATA_CFG_VALUE |= g_ranges[g_range]
            self.XYZ_DATA_CFG.set(self._XYZ_DATA_CFG_VALUE)

    def set_output_data_rate(self, output_data_rate):
        """Sets the output data rate in Hz.

        Be sure to call `standby()` before using this method and `activate()`
        after using this method.

        :param output_data_rate: The output data rate.
        :type output_data_rate: int (acceptable rates: 800, 400, 200, 100,
                                50, 12.5, 6.25, 1.56)
        """
        output_data_rates = {800: CTRL_REG1_ODR_800,
                             400: CTRL_REG1_ODR_400,
                             200: CTRL_REG1_ODR_200,
                             100: CTRL_REG1_ODR_100,
                             50: CTRL_REG1_ODR_50,
                             12.5: CTRL_REG1_ODR_12_5,
                             6.25: CTRL_REG1_ODR_6_25,
                             1.56: CTRL_REG1_ODR_1_56}
        if output_data_rate in output_data_rates:
            self._CTRL_REG1_VALUE &= 0b11100111
            self._CTRL_REG1_VALUE |= output_data_rates[output_data_rate]
            self.CTRL_REG1.set(self._CTRL_REG1_VALUE)

    def get_g(self, raw=False, res12=True):
        """Returns the x, y and z values as a dictionary. By default it returns
        signed values at 12-bit resolution. You can specify a lower resolution
        (8-bit) or request the raw register values. Signed values are
        in G's. You can alter the recording range with `set_g_range()`.

        :param raw: If True: return raw, unsigned data, else: sign values
        :type raw: boolean (default: False)
        :param res12: If True: read 12-bit resolution, else: 8-bit
        :type res12: boolean (default: True)
        """
        buf = self.interface.read_bytes(self.i2c_address, 0x00, 7)
        # status = buf[0]
        if res12:
            x = (buf[1] << 4) | (buf[2] >> 4)
            y = (buf[3] << 4) | (buf[4] >> 4)
            z = (buf[5] << 4) | (buf[6] >> 4)
        else:
            x, y, z = buf[1], buf[3], buf[5]

        if not raw:
            # get range
            fsr = self._XYZ_DATA_CFG_VALUE & 0x03
            g_ranges = {XYZ_DATA_CFG_FSR_2G: 2,
                        XYZ_DATA_CFG_FSR_4G: 4,
                        XYZ_DATA_CFG_FSR_8G: 8}
            g_range = g_ranges[fsr]
            resolution = 12 if res12 else 8
            gmul = g_range / (2 ** (resolution - 1))
            x = twos_complement(x, resolution) * gmul
            y = twos_complement(y, resolution) * gmul
            z = twos_complement(z, resolution) * gmul

        return {'x': x, 'y': y, 'z': z}

    def get_ms2(self):
        """Returns the x, y, z values as a dictionary in SI units (m/s^2)."""
        xyz = self.get_g(raw=False, res12=True)
        # multiply each xyz value by the standard gravity value
        return {direction: magnitude * STANDARD_GRAVITY
                for direction, magnitude in xyz.items()}
