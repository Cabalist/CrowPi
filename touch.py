#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time

import RPi.GPIO as GPIO

# define touch pin
TOUCH_PIN = 11

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# set GPIO pin to INPUT
GPIO.setup(TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # check if touch detected
        if GPIO.input(TOUCH_PIN):
            print('Touch Detected')
        time.sleep(0.1)
except KeyboardInterrupt:
    # CTRL+C detected, cleaning and quitting the script
    GPIO.cleanup()
