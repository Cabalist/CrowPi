#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO
from mcpi.minecraft import Minecraft

# create Minecraft Object
mc = Minecraft.create()

# set touch pin
TOUCH_PIN = 11
# set gpio mode as GPIO BOARD
GPIO.setmode(GPIO.BOARD)
# set as INPUT
GPIO.setup(TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(TOUCH_PIN):  # look for button press
        mc.player.setPos(0, 0, 0)  # teleport player
        print("Teleported successfully!")
        time.sleep(0.5)  # wait 0.5 seconds
