import threading
import time
from plutonium.common.utils import i2c_addresses

DEVICE_CHECK_INTERVAL = 1  # seconds
DEVICES = {}


def monitor():
    while True:
        addresses = i2c_addresses()
        for addr in addresses:
            if addr not in DEVICES.keys():
                DEVICES[addr] = None
                print("Device added")
            else:
                print("Device is known")
        time.sleep(DEVICE_CHECK_INTERVAL)
    pass

monitor_thread = threading.Thread(target=monitor)
monitor_thread.start()
