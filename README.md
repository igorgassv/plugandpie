# Plutonium

### Installation
Requires `python-smbus` for Python 3
https://procrastinative.ninja/2014/07/21/smbus-for-python34-on-raspberry/


Workaround for repeated starts on Raspberry Pi i2c driver:
```
sudo su -
echo -n 1 > /sys/module/i2c_bcm2708/parameters/combined
exit
```

### Goal
```
>>> import plutonium as pu
>>> accelerometer = pu.get_accelerometer()
>>> accelerometer.get_xyz()
{'x': 0.12, 'y': 1.14, 'z': 9.23}
```