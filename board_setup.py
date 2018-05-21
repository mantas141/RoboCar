import RPi.GPIO as GPIO

#Board Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Motor setup
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
GPIO.setup(PWMB, GPIO.OUT)

motor_a = GPIO.PWM(PWMA, 50)  # a is right side engines
motor_b = GPIO.PWM(PWMB, 50)  # b is left side engines

motor_a.start(80)
motor_b.start(80)

#IR sensor setup
IRsensor1 = 12 # Broadcom pin - Up for change
IRsensor2 = 16 # Broadcom pin - Up for change
IRsensor3 = 20 # Broadcom pin - Up for change
IRsensor4 = 21 # Broadcom pin - Up for change

GPIO.setup(IRsensor1, GPIO.IN) # sensor set as input
GPIO.setup(IRsensor2, GPIO.IN) # sensor set as input
GPIO.setup(IRsensor3, GPIO.IN) # sensor set as input
GPIO.setup(IRsensor4, GPIO.IN) # sensor set as input

"""IR_A = GPIO.input(IRsensor4)
IR_B = GPIO.input(IRsensor3)
IR_C = GPIO.input(IRsensor2)
IR_D = GPIO.input(IRsensor1)"""

#Echo setup
Echo = 17
Trigger = 27

GPIO.setup(Echo, GPIO.IN) # sensor set as input
GPIO.setup(Trigger, GPIO.OUT) # sensor set as input