#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
from sys import argv

#Map bells to GPIO outputs
bell1=7
bell2=15
bell3=31
bell4=37

#Set Default 'on' time
stayOn=2

#override on time with command argument
if len(argv) > 1:
    stayOn = int(argv[1])

# Set GPIO Mode
GPIO.setmode(GPIO.BOARD)

# Set relay pins as output
GPIO.setup(bell1, GPIO.OUT)
GPIO.setup(bell2, GPIO.OUT)
GPIO.setup(bell3, GPIO.OUT)
GPIO.setup(bell4, GPIO.OUT)


# Turn all relays ON
print('bell1')
GPIO.output(bell1, GPIO.HIGH)
sleep(0.12)
print('bell2')
GPIO.output(bell2, GPIO.HIGH)
sleep(0.12)
print('bell3')
GPIO.output(bell3, GPIO.HIGH)
sleep(0.12)
print('bell4')
GPIO.output(bell4, GPIO.HIGH)

# stay on for stayOn seconds
sleep(stayOn)

# Turn all relays OFF
GPIO.output(bell1, GPIO.LOW)
GPIO.output(bell2, GPIO.LOW)
GPIO.output(bell3, GPIO.LOW)
GPIO.output(bell4, GPIO.LOW)

GPIO.cleanup()
