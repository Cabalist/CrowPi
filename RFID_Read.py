#!/usr/bin/env python
# coding=utf-8

import signal
import sys
import time

from pirc522 import RFID

# TODO Needs testing
# TODO Prints an error:
# SAMPLE OUTPUT:
#   Starting
#
#   Detected: 10
#   Card read UID: 130,8,5,60
#   Setting tag
#   Selecting UID [130, 8, 5, 60, 179]
#
#   Authorizing
#   Changing used auth key to [116, 0, 82, 53, 0, 255] using method B
#
#   Reading
#   Calling card_auth on UID [130, 8, 5, 60, 179]
#   E2
#   Error on S1B0
#
#   Deauthorizing
#   Changing auth key and method to None


run = True
rdr = RFID()
util = rdr.util()
util.debug = True


def end_read(signal, frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()


signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    error, data = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    error, uid = rdr.anticoll()
    if not error:
        print("Card read UID: {0},{1},{2},{3}".format(str(uid[0]), str(uid[1]), str(uid[2]), str(uid[3])))

        print("Setting tag")
        util.set_tag(uid)
        print("\nAuthorizing")
        util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
        print("\nReading")
        util.read_out(4)
        print("\nDeauthorizing")
        util.deauth()

        time.sleep(1)
