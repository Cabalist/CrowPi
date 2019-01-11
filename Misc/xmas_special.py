#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
from Adafruit_LED_Backpack import SevenSegment

# Define LCD column and row size for 16x2 LCD.
LCD_COLUMNS = 16
LCD_ROWS = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
# Initialize the segment
segment = SevenSegment.SevenSegment(address=0x70)
segment.begin()

TONE_PIN = 18

GPIO.setup(TONE_PIN, GPIO.IN)
GPIO.setup(TONE_PIN, GPIO.OUT)

# setup the LCD for merry xmas
lcd.set_backlight(0)
lcd.message('Merry Christmas \n from Elecrow!')
# set the segment 12:25 (December 25th)
segment.set_digit(0, 1)
segment.set_digit(1, 2)
segment.set_digit(2, 2)
segment.set_digit(3, 5)
# Toggle colon at 1Hz
segment.set_colon(1 % 2)
segment.write_display()


# High-level abstraction of the Arduino's Delay function
def delay(times):
    time.sleep(times / 500.0)


# High-level abstraction of the Arduino's Tone function, though this version is blocking
def tone(pin, pitch, duration):
    if pitch == 0:
        delay(duration)
        return
    p = GPIO.PWM(TONE_PIN, pitch)

    # Change the duty-cycle to 50 if you wish
    p.start(30)
    delay(duration)
    p.stop()

    # Delay used to discourage overlap of PWM cycles
    delay(2)


def midi():
    try:
        tone(TONE_PIN, 261, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 349, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 349, 87.0)
        delay(10.0)
        tone(TONE_PIN, 391, 87.0)
        delay(10.0)
        tone(TONE_PIN, 349, 87.0)
        delay(10.0)
        tone(TONE_PIN, 220, 58.5)
        tone(TONE_PIN, 329, 28.5)
        delay(10.0)
        tone(TONE_PIN, 293, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 293, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 174, 154.5)
        tone(TONE_PIN, 293, 18.75)
        delay(20.8333333333)
        tone(TONE_PIN, 391, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 391, 87.0)
        delay(10.0)
        tone(TONE_PIN, 440, 87.0)
        delay(10.0)
        tone(TONE_PIN, 391, 87.0)
        delay(10.0)
        tone(TONE_PIN, 195, 58.5)
        tone(TONE_PIN, 349, 28.5)
        delay(10.0)
        tone(TONE_PIN, 329, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 329, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 261, 154.5)
        tone(TONE_PIN, 329, 18.75)
        delay(20.8333333333)
        tone(TONE_PIN, 440, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 440, 87.0)
        delay(10.0)
        tone(TONE_PIN, 466, 87.0)
        delay(10.0)
        tone(TONE_PIN, 440, 87.0)
        delay(10.0)
        tone(TONE_PIN, 277, 58.5)
        tone(TONE_PIN, 391, 28.5)
        delay(10.0)
        tone(TONE_PIN, 349, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 293, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 261, 87.0)
        delay(10.0)
        tone(TONE_PIN, 261, 87.0)
        delay(10.0)
        tone(TONE_PIN, 293, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 233, 154.5)
        tone(TONE_PIN, 391, 18.75)
        delay(20.8333333333)
        tone(TONE_PIN, 329, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 349, 346.5)
        delay(41.6666666667)
        tone(TONE_PIN, 261, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 349, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 349, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 174, 154.5)
        tone(TONE_PIN, 349, 18.75)
        delay(20.8333333333)
        tone(TONE_PIN, 329, 346.5)
        delay(41.6666666667)
        tone(TONE_PIN, 233, 154.5)
        tone(TONE_PIN, 329, 18.75)
        delay(20.8333333333)
        tone(TONE_PIN, 349, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 329, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 195, 154.5)
        tone(TONE_PIN, 293, 18.75)
        delay(20.8333333333)
        tone(TONE_PIN, 261, 346.5)
        delay(41.6666666667)
        tone(TONE_PIN, 391, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 440, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 391, 87.0)
        delay(10.0)
        tone(TONE_PIN, 391, 87.0)
        delay(10.0)
        tone(TONE_PIN, 349, 87.0)
        delay(10.0)
        tone(TONE_PIN, 220, 58.5)
        tone(TONE_PIN, 349, 28.5)
        delay(10.0)
        tone(TONE_PIN, 523, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 261, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 261, 87.0)
        delay(10.0)
        tone(TONE_PIN, 174, 58.5)
        tone(TONE_PIN, 261, 28.5)
        delay(10.0)
        tone(TONE_PIN, 293, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 195, 154.5)
        tone(TONE_PIN, 391, 18.75)
        delay(20.8333333333)
        tone(TONE_PIN, 329, 173.25)
        delay(20.8333333333)
        tone(TONE_PIN, 349, 346.5)
    except KeyboardInterrupt:
        # Turn the screen off
        lcd.clear()
        lcd.set_backlight(1)
        # clean the segment
        segment.clear()
        segment.write_display()
        # clean GPIO pins
        GPIO.cleanup()
        exit()


while True:
    midi()
