import RPi.GPIO as GPIO
import board_setup as b

#Motor functions
def forward():
    GPIO.output(b.ain1, GPIO.HIGH)
    GPIO.output(b.ain2, GPIO.LOW)
    GPIO.output(b.bin1, GPIO.HIGH)
    GPIO.output(b.bin2, GPIO.LOW)
    b.motor_a.ChangeDutyCycle(50)
    b.motor_b.ChangeDutyCycle(50)


def backwards():
    GPIO.output(b.ain1, GPIO.LOW)
    GPIO.output(b.ain2, GPIO.HIGH)
    GPIO.output(b.bin1, GPIO.LOW)
    GPIO.output(b.bin2, GPIO.HIGH)
    b.motor_a.ChangeDutyCycle(50)
    b.motor_b.ChangeDutyCycle(50)


def TurnRight():
    GPIO.output(b.ain1, GPIO.HIGH)  # a side/right side going forwards
    GPIO.output(b.ain2, GPIO.LOW)
    GPIO.output(b.bin1, GPIO.LOW)  # b side/left side going backwards
    GPIO.output(b.bin2, GPIO.HIGH)
    b.motor_a.ChangeDutyCycle(65)
    b.motor_b.ChangeDutyCycle(65)


def TurnLeft():
    GPIO.output(b.ain1, GPIO.LOW)  # a side/right side going backwards
    GPIO.output(b.ain2, GPIO.HIGH)
    GPIO.output(b.bin1, GPIO.HIGH)  # b side/left side going forwards
    GPIO.output(b.bin2, GPIO.LOW)
    b.motor_a.ChangeDutyCycle(65)
    b.motor_b.ChangeDutyCycle(65)

#IR functions
def ir_read():
    IR_A = GPIO.input(b.IRsensor4)
    IR_B = GPIO.input(b.IRsensor3)
    IR_C = GPIO.input(b.IRsensor2)
    IR_D = GPIO.input(b.IRsensor1)
    return [IR_A, IR_B, IR_C, IR_D]