"""Prints the accelerometer values every second."""
import time
import datetime
from drivers.accelerometer.mma8452q import MMA8452Q

G_RANGE = 2
INTERVAL = 0.5  # seconds

if __name__ == '__main__':
    with MMA8452Q() as accelerometer:
        # Configure (This is completely optional -- shown here as an example)
        accelerometer.standby()
        accelerometer.set_g_range(G_RANGE)
        accelerometer.activate()
        print("g = {}".format(G_RANGE))
        time.sleep(INTERVAL)  # settle

        # print data
        while True:
            ms = accelerometer.get_xyz_ms2()
            print("----")
            print(datetime.datetime.now())
            print('m/s^2 | x: {:.2f}, y: {:.2f}, z: {:.2f}'.format(ms['x'],
                                                                   ms['y'],
                                                                   ms['z']))
            time.sleep(INTERVAL)
