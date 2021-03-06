#!/usr/bin/python
# -*- coding: utf-8 -*-

# Example using a character LCD backpack.
import time

import Adafruit_CharLCD as LCD

# Define LCD column and row size for 16x2 LCD.
LCD_COLUMNS = 16
LCD_ROWS = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

try:
    # Turn backlight on
    lcd.set_backlight(0)

    # Print a two line message
    lcd.message('Hello\nworld!')

    # Wait 5 seconds
    time.sleep(5)

    # Demo showing the cursor.
    lcd.clear()
    lcd.show_cursor(True)
    lcd.message('Show cursor')

    time.sleep(5)

    # Demo showing the blinking cursor.
    lcd.clear()
    lcd.blink(True)
    lcd.message('Blink cursor')

    time.sleep(5)

    # Stop blinking and showing cursor.
    lcd.show_cursor(False)
    lcd.blink(False)

    # Demo scrolling message right/left.
    lcd.clear()
    message = 'Scroll'
    lcd.message(message)
    for i in range(LCD_COLUMNS - len(message)):
        time.sleep(0.5)
        lcd.move_right()
    for i in range(LCD_COLUMNS - len(message)):
        time.sleep(0.5)
        lcd.move_left()

    # Demo turning backlight off and on.
    lcd.clear()

    for i in range(5, 0, -1):
        lcd.message('Flash backlight\nin {} seconds...'.format(i))
        time.sleep(1)
        lcd.clear()

    # Turn backlight off.
    lcd.set_backlight(1)
    time.sleep(2)

    # Change message.
    lcd.clear()
    lcd.message('Goodbye!')
    time.sleep(1)

    # Turn backlight on.
    lcd.set_backlight(0)

    # Turn backlight off.
    time.sleep(2)
    lcd.clear()
    lcd.set_backlight(1)
except KeyboardInterrupt:
    # Turn the screen off
    lcd.clear()
    lcd.set_backlight(1)
