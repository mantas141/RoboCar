import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

ain1 = 2
ain2 = 3
bin1 = 14
bin2 = 15
PWMA = 18
PWMB = 13

GPIO.setup(ain1, GPIO.OUT)
GPIO.setup(ain2, GPIO.OUT)
GPIO.setup(bin1, GPIO.OUT)
GPIO.setup(bin2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)

speed_a = GPIO.PWM(PWMA, 50)  # a is right side engines
speed_b = GPIO.PWM(PWMB, 50)  # b is left side engines


def forward():
    GPIO.output(ain1, GPIO.HIGH)
    GPIO.output(ain2, GPIO.LOW)
    GPIO.output(bin1, GPIO.HIGH)
    GPIO.output(bin2, GPIO.LOW)


def backwards():
    GPIO.output(ain1, GPIO.LOW)
    GPIO.output(ain2, GPIO.HIGH)
    GPIO.output(bin1, GPIO.LOW)
    GPIO.output(bin2, GPIO.HIGH)


def TurnRight():
    GPIO.output(ain1, GPIO.HIGH)  # a side/right side going forwards
    GPIO.output(ain2, GPIO.LOW)
    GPIO.output(bin1, GPIO.LOW)  # b side/left side going backwards
    GPIO.output(bin2, GPIO.HIGH)


def TurnLeft():
    GPIO.output(ain1, GPIO.LOW)  # a side/right side going backwards
    GPIO.output(ain2, GPIO.HIGH)
    GPIO.output(bin1, GPIO.HIGH)  # b side/left side going forwards
    GPIO.output(bin2, GPIO.LOW)



def main():
    while True:

