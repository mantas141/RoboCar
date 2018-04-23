import RPi.GPIO as GPIO
import time

PWMA = X
PWMB = X
AIN1 = X
AIN2 = X
BIN1 = X
BIN2 = X

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

GPIO.output(AIN1, GPIO.LOW)
GPIO.output(AIN2, GPIO.HIGH)
GPIO.output(BIN1, )
GPIO.output(BIN2, )

rightmotor = GPIO.PWM(PWMA, 50)
rightmotor.start(0)

rightmotor.ChangeDutyCycle(100)

leftmotor = GPIO.PWM(PWMB, 50)
leftmotor.start(0)

leftmotor.ChangeDutyCycle(100)