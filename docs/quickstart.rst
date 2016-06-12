Plug&Pie Quickstart
===================

Automagic sensor setup
----------------------

``plugandpie`` was designed to automatically set up one sensor for each of the most common ones.
What actually happens is the immediate instantiation of a Proxy class for each of these sensors,
but they will only configure themselves after the first attempt of use.

If you set the ``logging`` level to ``INFO``, you can see its inner magic like in this example:

.. code:: python

    >>> import plugandpie as pnp
    >>> pnp.accelerometer
    <plugandpie.device.Proxy.Proxy object at 0x76a1fa70>
    >>> pnp.accelerometer.get_ms2()
    INFO:root:New I2C device found at address 1d
    INFO:root:Looking for a Sensor.ACCELEROMETER on I2C devices...
    INFO:root:MMA8452Q at 1d has Sensor.ACCELEROMETER
    {'x': -1.37906015625, 'y': -3.9935283691406247, 'z': 8.724470849609375}

Hopefully for most basic applications this will be enough and save a few hours of work.


Automatic sensor import
-----------------------

When the magic does not happen, it can be for one of a few reasons:

1. The wrong driver was assigned to the device, but there is a driver for it
2. The device has no driver in the library (yet)

