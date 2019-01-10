#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time
import RPi.GPIO as GPIO

# define LED pin
LED_PIN = 37

# set GPIO mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)
# set pin as output
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # turn on LED
        GPIO.output(LED_PIN, GPIO.HIGH)
        # Wait
        time.sleep(0.2)
        # turn off LED
        GPIO.output(LED_PIN, GPIO.LOW)
        # Wait
        time.sleep(0.2)
except KeyboardInterrupt:
    # CTRL+C detected, cleaning and quitting the script
    GPIO.cleanup()
