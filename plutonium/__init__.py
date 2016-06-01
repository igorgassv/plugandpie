import threading
import time
from plutonium.common.utils import i2c_addresses
from plutonium.drivers.mapping import driver_map

DEVICE_CHECK_INTERVAL = 5  # seconds
DEVICES = {}


def monitor():
    while True:
        addresses = i2c_addresses()
        for addr in addresses:
            if addr not in DEVICES.keys():
                driver = driver_map[addr]()
                driver.open()
                DEVICES[addr] = driver
        time.sleep(DEVICE_CHECK_INTERVAL)
    pass

monitor_thread = threading.Thread(target=monitor)
monitor_thread.start()
