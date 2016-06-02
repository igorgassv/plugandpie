from plutonium.devices.Device import Device


class DeviceProxy:
    def __init__(self, device: Device = None):
        self._device = device

    def __getattribute__(self, name):
        if self._device is not None:
            return getattr(self._device, name)
        else:
            print("Device not found")
            return None
