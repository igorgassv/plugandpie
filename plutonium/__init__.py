from plutonium.devices.DeviceProxy import DeviceProxy
import threading
import time
from plutonium.common.utils import i2c_addresses
from plutonium.devices.mapping import driver_map

DEVICE_CHECK_INTERVAL = 5  # seconds
DEVICES = {}

accelerometer = DeviceProxy()


def monitor():
    while True:
        addresses = i2c_addresses()
        for addr in addresses:
            if addr not in DEVICES.keys():
                device = driver_map[addr]()
                DEVICES[addr] = device
                if 'accelerometer' in device.sensors:
                    accelerometer.set_device(device)
        time.sleep(DEVICE_CHECK_INTERVAL)
    pass

monitor_thread = threading.Thread(target=monitor)
monitor_thread.daemon = True
monitor_thread.start()