# coding=utf-8
import signal
import socket
from array import array

import RPi.GPIO as GPIO
import lirc

# TODO Needs testing

GPIO.setmode(11)
GPIO.setup(17, 0)
GPIO.setup(18, 0)
PORT = 42001
HOST = "localhost"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Lirc = lirc.init("keys")


# Un-Comment to stop nextcode() from waiting for a signal ( will return empty array when no key is pressed )
# lirc.set_blocking(False, Lirc)

def handler(signal, frame):
    s.close()
    GPIO.cleanup()
    exit(0)


signal.signal(signal.SIGTSTP, handler)


def sendCmd(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n >> 24) & 0xFF))
    a.append(chr((n >> 16) & 0xFF))
    a.append(chr((n >> 8) & 0xFF))
    a.append(chr(n & 0xFF))
    s.send(a.tostring() + cmd)


while True:
    output = lirc.nextcode()
    print(output[0])
