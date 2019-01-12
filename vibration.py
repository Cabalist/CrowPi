#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time

import RPi.GPIO as GPIO

# NOTE: Make sure dipswitch 1 is set to on.

# define vibration pin
VIBRATION_PIN = 13

# Set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# Setup vibration pin to OUTPUT
GPIO.setup(VIBRATION_PIN, GPIO.OUT)

# turn on vibration
GPIO.output(VIBRATION_PIN, GPIO.HIGH)
# wait
time.sleep(2)
# turn off vibration
GPIO.output(VIBRATION_PIN, GPIO.LOW)
# cleaup GPIO
GPIO.cleanup()
