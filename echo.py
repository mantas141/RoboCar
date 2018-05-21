"""Based on a previous script given to us by Kaj"""

import board_setup as b
import time
import RPi.GPIO as GPIO

def reading(sensor):
    pingtime = 0
    echotime = 0
    if sensor == 0:
        GPIO.output(b.Trigger,GPIO.LOW)
        GPIO.output(b.Trigger,GPIO.HIGH)
        pingtime = time.time()
        time.sleep(0.00001)
        GPIO.output(b.Trigger,GPIO.LOW)
        while GPIO.input(b.Echo)==0:
            pingtime = time.time()
        while GPIO.input(b.Echo)==1:
            echotime=time.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
        #print(pingtime)
        #print(echotime)
        return distance

if __name__ == "__main__":
    range = reading(0)
    print(range)
    print()
    time.sleep(0.25)