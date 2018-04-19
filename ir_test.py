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

# PROGRAM
while True:
        A = GPIO.input(IRsensor1)
		B = GPIO.input(IRsensor2)
		C = GPIO.input(IRsensor3)
		D = GPIO.input(IRsensor4)
        print (A, B, C, D)
        time.sleep(0.5)