"""Prints the accelerometer values every second."""
import time
import datetime
from plugandpie import accelerometer

G_RANGE = 2
INTERVAL = 0.5  # seconds

if __name__ == '__main__':
    while True:
        ms = accelerometer.get_ms2()
        print("----")
        print(datetime.datetime.now())
        print('m/s^2 | x: {:.2f}, y: {:.2f}, z: {:.2f}'.format(ms['x'],
                                                               ms['y'],
                                                               ms['z']))
        time.sleep(INTERVAL)
