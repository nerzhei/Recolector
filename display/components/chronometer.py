__author__ = 'maicol'

import thread
from time import sleep


class Chronometer():
	def __init__(self, time):
		self._time = time
		self._value = False
		thread.start_new_thread(self.start, ())

	def start(self):
		try:
			while True:
				self._value = True
				sleep(self._time)
				self._value = False
				sleep(self._time)
		except Exception:
			pass


	def get_value(self):
		return self._value