#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time

import RPi.GPIO as GPIO

BUZZER_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Make buzzer sound
GPIO.output(BUZZER_PIN, GPIO.HIGH)
time.sleep(0.5)
# Stop buzzer sound
GPIO.output(BUZZER_PIN, GPIO.LOW)

GPIO.cleanup()
