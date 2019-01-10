#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO

# configure both button and buzzer pins
BUTTON_PIN = 37
BUZZER_PIN = 12

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# setup button pin as input and buzzer pin as output
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    while True:
        # check if button pressed
        if GPIO.input(BUTTON_PIN) == 0:
            # set buzzer on
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
        else:
            # it's not pressed, set button off
            GPIO.output(BUZZER_PIN, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
