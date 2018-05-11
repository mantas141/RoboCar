# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
IRsensor1 = 12 # Broadcom pin - Up for change
IRsensor2 = 16 # Broadcom pin - Up for change
IRsensor3 = 20 # Broadcom pin - Up for change
IRsensor4 = 21 # Broadcom pin - Up for change

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(IRsensor1, GPIO.IN) # sensor set as input
GPIO.setup(IRsensor2, GPIO.IN) # sensor set as input
GPIO.setup(IRsensor3, GPIO.IN) # sensor set as input
GPIO.setup(IRsensor4, GPIO.IN) # sensor set as input

# PROGRAM - 0 = reflective surface, 1 = nonreflective surface
while True:
    A = GPIO.input(IRsensor4)
    B = GPIO.input(IRsensor3)
    C = GPIO.input(IRsensor2)
    D = GPIO.input(IRsensor1)
    print (A, B, C, D)
    time.sleep(0.5)