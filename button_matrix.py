#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : original author stenobot
# Original Author Github: https://github.com/stenobot/SoundMatrixPi
# http://elecrow.com/

import time

import RPi.GPIO as GPIO

# TODO BUG Buttons are mapped backwards
# TODO Cleanup

class ButtonMatrix():

    def __init__(self):

        GPIO.setmode(GPIO.BOARD)

        # matrix button ids
        self.buttonIDs = [[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12],
                          [13, 14, 15, 16]]
        # gpio inputs for rows
        self.rowPins = [13, 15, 29, 31]
        # gpio outputs for columns
        self.columnPins = [33, 35, 37, 22]

        # define four inputs with pull up resistor
        for each_pin in self.rowPins:
            GPIO.setup(each_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # define four outputs and set to high
        for each_pin in self.columnPins:
            GPIO.setup(each_pin, GPIO.OUT)
            GPIO.output(each_pin, 1)

    def activateButton(self, row_pin, col_pin):
        # get the button index
        btn_index = self.buttonIDs[row_pin][col_pin] - 1
        print("button {} pressed".format(btn_index + 1))

        # prevent button presses too close together
        time.sleep(.3)

    def buttonHeldDown(self, pin):
        if GPIO.input(self.rowPins[pin]) == 0:
            return True
        return False


def main():
    # initial the button matrix
    buttons = ButtonMatrix()
    try:
        while True:
            for j in range(len(buttons.columnPins)):
                # set each output pin to low
                GPIO.output(buttons.columnPins[j], 0)
                for i in range(len(buttons.rowPins)):
                    if GPIO.input(buttons.rowPins[i]) == 0:
                        # button pressed, activate it
                        buttons.activateButton(i, j)
                        # do nothing while button is being held down
                        while buttons.buttonHeldDown(i):
                            pass
                # return each output pin to high
                GPIO.output(buttons.columnPins[j], 1)
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
