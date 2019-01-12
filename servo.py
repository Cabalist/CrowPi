#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Original author WindVoiceVox
# Original Author Github: https://github.com/WindVoiceVox/Raspi_SG90
# http://elecrow.com/

# NOTE: Make sure dipswitches 7-8 are set to on.

import time

import RPi.GPIO as GPIO


class sg90(object):

    def __init__(self, direction):
        self.PIN = 22
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIN, GPIO.OUT)
        self.direction = int(direction)
        self.servo = GPIO.PWM(self.PIN, 50)
        self.servo.start(0.0)

    def cleanup(self):

        self.servo.ChangeDutyCycle(self._henkan(0))
        time.sleep(0.3)
        self.servo.stop()
        GPIO.cleanup()

    def currentdirection(self):
        return self.direction

    def _henkan(self, value):
        return 0.05 * value + 7.0

    def setdirection(self, direction, speed):
        for d in range(self.direction, direction, int(speed)):
            self.servo.ChangeDutyCycle(self._henkan(d))
            self.direction = d
            time.sleep(0.1)
        self.servo.ChangeDutyCycle(self._henkan(direction))
        self.direction = direction


def main():
    s = sg90(0)

    try:
        while True:
            print("Turn left ...")
            s.setdirection(100, 10)
            time.sleep(0.5)
            print("Turn right ...")
            s.setdirection(-100, -10)
            time.sleep(0.5)
    except KeyboardInterrupt:
        s.cleanup()


if __name__ == "__main__":
    main()
