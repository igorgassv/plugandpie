import threading
import time
from plutonium.common.utils import i2c_addresses
from plutonium.devices.mapping import driver_map

DEVICE_CHECK_INTERVAL = 5  # seconds
DEVICES = {}


def monitor():
    while True:
        addresses = i2c_addresses()
        for addr in addresses:
            if addr not in DEVICES.keys():
                DEVICES[addr] = driver_map[addr]()
        time.sleep(DEVICE_CHECK_INTERVAL)
    pass

monitor_thread = threading.Thread(target=monitor)
monitor_thread.start()
