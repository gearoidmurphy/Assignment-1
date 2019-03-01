#!/usr/bin/python
import time
import RPi.GPIO as GPIO # import a library

GPIO.setmode(GPIO.BCM) # set the pin numbering system to BCM

GPIO.setup(4,GPIO.OUT) # set GPIO17 as an OUTPUT
#GPIO.setup(63,GPIO.OUT) # set GPIO27 as am OUTPUT

GPIO.output(4,True) # set GPIO17 high, 3v3 will now be active on that pin
time.sleep(1)
GPIO.output(4,False)
#GPIO.output(63,GPIO.HIGH) # set GPIO27 high, 3v3 will now be active on that pin
