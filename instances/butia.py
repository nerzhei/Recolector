__author__ = 'maicol'

from modules.pybot import usb4butia


class Butia():
    def __init__(self):
        self._butia = None

    def get_butia(self):
        if not self._butia:
            self._butia = usb4butia.USB4Butia()
        return self._butia