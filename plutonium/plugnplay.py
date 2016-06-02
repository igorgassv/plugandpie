import threading
import time
from plutonium.common.utils import i2c_addresses
from plutonium.devices.mapping import driver_map
from plutonium.devices.DeviceProxy import DeviceProxy

accelerometer = DeviceProxy()
thermometer = DeviceProxy()

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
monitor_thread.daemon = True
monitor_thread.start()
