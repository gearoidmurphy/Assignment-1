#!/usr/bin/python
import RPi.GPIO as GPIO # import a library
GPIO.setmode(GPIO.BCM) # set the pin numbering system to BCM
GPIO.setup(13,GPIO.OUT) # set GPIO17 as an OUTPUT
GPIO.setup(27,GPIO.OUT) # set GPIO27 as am OUTPUT
GPIO.output(13,GPIO.LOW) # set GPIO17 low, 3v3 will now be
# de-active on that pin
GPIO.output(27,GPIO.LOW) # set GPIO27 low, 3v3 will now be
# de-active on that pin
