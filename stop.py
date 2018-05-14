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

motor_a = GPIO.PWM(PWMA, 50)  # a is right side engines
motor_b = GPIO.PWM(PWMB, 50)  # b is left side engines

motor_a.start(80)
motor_b.start(80)


GPIO.output(AIN1, GPIO.LOW)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(BIN1, GPIO.LOW)
GPIO.output(BIN2, GPIO.LOW)

motor_a.ChangeDutyCycle(0)
motor_b.ChangeDutyCycle(0)
