__author__ = 'maicol'
import sys, os
if os.path.exists('../modules/nxt'):
    sys.path.insert(0, '../modules/nxt')
    import nxt.locator
    from nxt.motor import *
    from nxt.sensor import *


class Nxt():
    def __init__(self):
        self._brick = None
        self._motor_a = None
        self._motor_b = None
        self._motor_c = None
        self._ultrasonic = None

    def get_nxt(self):
        if not self._brick:
            try:
                self._brick = nxt.locator.find_one_brick(name="NXT")
                self._motor_a = Motor(self._brick, PORT_A)
                self._motor_b = Motor(self._brick, PORT_B)
                self._motor_c = Motor(self._brick, PORT_C)
                self._ultrasonic = Ultrasonic(self.brick, PORT_1)
            except:
                pass
        return self._brick

    def get_port(self, key):
        if key == 1:
            return self._ultrasonic
        elif key == "a":
            return self._motor_a
        elif key == "b":
            return self._motor_b
        elif key == "c":
            return self._motor_c
