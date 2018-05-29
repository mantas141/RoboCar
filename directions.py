import RPi.GPIO as GPIO
import board_setup as b

#Motor functions
def forward(speed):
    GPIO.output(b.ain1, GPIO.LOW)
    GPIO.output(b.ain2, GPIO.HIGH)
    GPIO.output(b.bin1, GPIO.HIGH)
    GPIO.output(b.bin2, GPIO.LOW)
    b.motor_a.ChangeDutyCycle(speed)
    b.motor_b.ChangeDutyCycle(speed)


def backwards(speed):
    GPIO.output(b.ain1, GPIO.HIGH)
    GPIO.output(b.ain2, GPIO.LOW)
    GPIO.output(b.bin1, GPIO.LOW)
    GPIO.output(b.bin2, GPIO.HIGH)
    b.motor_a.ChangeDutyCycle(speed)
    b.motor_b.ChangeDutyCycle(speed)


def TurnRight(speed):
    GPIO.output(b.ain1, GPIO.HIGH)  # a side/right side going backwards
    GPIO.output(b.ain2, GPIO.LOW)
    GPIO.output(b.bin1, GPIO.HIGH)  # b side/left side going forwards
    GPIO.output(b.bin2, GPIO.LOW)
    b.motor_a.ChangeDutyCycle(speed)
    b.motor_b.ChangeDutyCycle(speed)


def TurnLeft(speed):
    GPIO.output(b.ain1, GPIO.LOW)  # a side/right side going forwards
    GPIO.output(b.ain2, GPIO.HIGH)
    GPIO.output(b.bin1, GPIO.LOW)  # b side/left side going backwards
    GPIO.output(b.bin2, GPIO.HIGH)
    b.motor_a.ChangeDutyCycle(speed)
    b.motor_b.ChangeDutyCycle(speed)

#IR functions
def ir_read():
    IR_A = GPIO.input(b.IRsensor4)
    IR_B = GPIO.input(b.IRsensor3)
    IR_C = GPIO.input(b.IRsensor2)
    IR_D = GPIO.input(b.IRsensor1)
    return [IR_A, IR_B, IR_C, IR_D]

#Handler setup
def handler(signum, frame): #stop when ctrl-c is recieved
    print("Signal handler called with signal", signum)
    print("Exiting...")
    GPIO.output(b.PWMA, GPIO.LOW)
    GPIO.output(b.PWMB, GPIO.LOW)
    GPIO.cleanup()
    exit(0)
