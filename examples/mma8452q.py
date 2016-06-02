"""Prints the accelerometer values every second."""
import time
import datetime
import plutonium as pu

G_RANGE = 2
INTERVAL = 0.5  # seconds

if __name__ == '__main__':
    accelerometer = pu.DEVICES['1d']

    # Configure (This is completely optional -- shown here as an example)
    accelerometer.standby()
    accelerometer.set_g_range(G_RANGE)
    accelerometer.activate()
    print("g = {}".format(G_RANGE))
    time.sleep(INTERVAL)  # settle

    # print data
    while True:
        ms = accelerometer.get_ms2()
        print("----")
        print(datetime.datetime.now())
        print('m/s^2 | x: {:.2f}, y: {:.2f}, z: {:.2f}'.format(ms['x'],
                                                               ms['y'],
                                                               ms['z']))
        time.sleep(INTERVAL)
