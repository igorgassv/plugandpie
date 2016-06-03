from plutonium.devices.Device import Device


class DeviceProxy:
    def __init__(self, device: Device = None):
        self._device = device

    def set_device(self, device: Device):
        object.__setattr__(self, '_device', device)

    def no_op(self):
        pass

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return getattr(self._device, name)
