import RPi.GPIO as GPIO
import time

PWMA = 18
PWMB = 13
AIN1 = 2
AIN2 = 3
BIN1 = 14
BIN2 = 15

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

GPIO.output(AIN1, GPIO.HIGH)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(BIN1, GPIO.HIGH)
GPIO.output(BIN2, GPIO.LOW)

rightmotor = GPIO.PWM(PWMA, 50)
rightmotor.start(0)

rightmotor.ChangeDutyCycle(100)

leftmotor = GPIO.PWM(PWMB, 50)
leftmotor.start(0)

leftmotor.ChangeDutyCycle(100)