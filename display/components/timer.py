__author__ = 'maicol'

import thread
from time import sleep


class Timer():
    def __init__(self, time):
        self._time = time
        self._value = False
        thread.start_new_thread(self.start, ())

    def start(self):
        sleep(self._time)
        self._value = True

    def get_value(self):
        return self._value