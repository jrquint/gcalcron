#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BOARD)

# Set relay pins as output
GPIO.setup(7, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)


# Turn all relays ON
print('GPIO 7')
GPIO.output(7, GPIO.HIGH)
sleep(0.12)
print('GPIO 15')
GPIO.output(15, GPIO.HIGH)
sleep(0.12)
print('GPIO 31')
GPIO.output(31, GPIO.HIGH)
sleep(0.12)
print('GPIO 37')
GPIO.output(37, GPIO.HIGH)
# Sleep for 5 seconds
sleep(2.1)
# Turn all relays OFF
GPIO.output(7, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(31, GPIO.LOW)
GPIO.output(37, GPIO.LOW)
