#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time

import RPi.GPIO as GPIO

# define relay pin
relay_pin = 40

# set GPIO mode as GPIO.BOARD
GPIO.setmode(GPIO.BOARD)
# setup relay pin as OUTPUT
GPIO.setup(relay_pin, GPIO.OUT)

# Open Relay
print("Opening relay...")
GPIO.output(relay_pin, GPIO.LOW)
# Wait half a second
time.sleep(1)
# Close Relay
print("Closing relay...")
GPIO.output(relay_pin, GPIO.HIGH)
GPIO.cleanup()
