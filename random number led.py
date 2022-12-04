import RPi.GPIO as GPIO
from time import sleep
import random

GPIO.setmode(GPIO.BOARD)

pins = [15,16,18,22]
for pin in pins:
GPIO.setup(pin, GPIO.OUT)

try:
while True:
x = random.randint(0,3)
if x is 0:
GPIO.output(15,1)
sleep(.3)
GPIO.output(15,0)
if x is 1:
GPIO.output(16,1)
sleep(.3)
GPIO.output(16,0)
if x is 2:
GPIO.output(18,1)
sleep(.3)
GPIO.output(18,0)
if x is 3:
GPIO.output(22,1)
sleep(.3)
GPIO.output(22,0)
except KeyboardInterrupt:
GPIO.cleanup()
