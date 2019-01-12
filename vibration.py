#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time

import RPi.GPIO as GPIO

# TODO Does not work in Py2/Py3

# define vibration pin
VIBRATION_PIN = 13

# Set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# Setup vibration pin to OUTPUT
GPIO.setup(VIBRATION_PIN, GPIO.OUT)

# turn on vibration
GPIO.output(VIBRATION_PIN, GPIO.HIGH)
# wait half a second
time.sleep(0.5)
# turn off vibration
GPIO.output(VIBRATION_PIN, GPIO.LOW)
# cleaup GPIO
GPIO.cleanup()
