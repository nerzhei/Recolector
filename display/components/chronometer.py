__author__ = 'maicol'

import thread
from time import sleep


class Chronometer():
    def __init__(self, time):
        self._time = time
        self._value = False
        thread.start_new_thread(self.start, ())

    def start(self):
        while True:
            self._value = True
            sleep(self._time)
            self._value = False
            sleep(self._time)

    def get_value(self):
        return self._value