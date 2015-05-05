__author__ = 'maicol'

import thread
from time import sleep


class Timer():
    def __init__(self, main, time):
        self._main = main
        self._time = time
        self._value = False
        thread.start_new_thread(self.start, ())

    def start(self):
        sleep(self._time)
        self._value = True
        self._main.set_ready()