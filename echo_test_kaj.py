import time
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.IN)


def reading(sensor):
    pingtime = 0
    echotime = 0
    if sensor == 0:
        GPIO.output(27,GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        pingtime = time.time()
        time.sleep(0.00001)
        GPIO.output(27,GPIO.LOW)
        while GPIO.input(17)==0:
            pingtime = time.time()
        while GPIO.input(17)==1:
            echotime=time.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
        print(pingtime)
        print(echotime)
        return distance

while True:
    range = reading(0)
    print(range)
    print()
    time.sleep(1)
