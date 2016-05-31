import sys
import posix
from fcntl import ioctl
from common.linux_i2c import *
import ctypes

# Try to make this support Python 2 as well.
assert sys.version_info.major >= 3, __name__ + " is only supported on Python 3"


DEFAULT_BUS = 1


class I2CMaster(object):
    """Performs I2C I/O transactions on an I2C bus.

    Transactions are performed by passing one or more I2C I/O messages
    to the transaction method of the I2CMaster.  I2C I/O messages are
    created with the reading, reading_into, writing and writing_bytes
    functions.

    An I2CMaster acts as a context manager, allowing it to be used in a
    with statement.  The I2CMaster's file descriptor is closed at
    the end of the with statement and the instance cannot be used for
    further I/O.

    For example:

        with I2CMaster() as i2c:
            i2c.transaction(
                writing(0x20, bytes([0x01, 0xFF])))
    """

    def __init__(self, bus=DEFAULT_BUS):
        """
        :param bus:   the number of the bus
        """
        self.bus = bus
        self.fd = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self):
        self.close()

    def open(self, extra_open_flags=0):
        """Opens the bus device.

        Arguments:
        extra_open_flags -- extra flags passed to posix.open when
                            opening the I2C bus device file (default 0;
                            e.g. no extra flags).
        """
        self.fd = posix.open("/dev/i2c-{}".format(self.bus),
                             posix.O_RDWR | extra_open_flags)

    def close(self):
        """
        Closes the I2C bus device.
        """
        posix.close(self.fd)

    def transaction(self, *msgs):
        """
        Perform an I2C I/O transaction.

        Arguments:
        *msgs -- I2C messages created by one of the reading, reading_into,
                 writing or writing_bytes functions.

        Returns: a list of byte sequences, one for each read operation
                 performed.
        """

        msg_count = len(msgs)
        msg_array = (i2c_msg*msg_count)(*msgs)
        ioctl_arg = i2c_rdwr_ioctl_data(msgs=msg_array, nmsgs=msg_count)

        ioctl(self.fd, I2C_RDWR, ioctl_arg)

        return [i2c_msg_to_bytes(m) for m in msgs if (m.flags & I2C_M_RD)]


def read(address, n_bytes):
    """An I2C I/O message that reads n_bytes bytes of data"""
    return reading_into(address, ctypes.create_string_buffer(n_bytes))


def reading_into(address, buf):
    """An I2C I/O message that reads into an existing ctypes string buffer."""
    return _new_i2c_msg(address, I2C_M_RD, buf)


def write(address, byte_sequence):
    """An I2C I/O message that writes one or more bytes of data.

    The bytes are passed to this function as a sequence.
    """
    buf = bytes(byte_sequence)
    return _new_i2c_msg(address, 0, ctypes.create_string_buffer(buf, len(buf)))


def _new_i2c_msg(address, flags, buf):
    return i2c_msg(addr=address, flags=flags, len=ctypes.sizeof(buf), buf=buf)


def i2c_msg_to_bytes(m):
    return ctypes.string_at(m.buf, m.len)