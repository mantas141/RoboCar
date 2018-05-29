import directions as d
import echo as e
import time
import signal

# max distance 180 cm
count = 0
range = 70

def main():
    #while count < 4:
    #    scout()
    while True:
        scout()

def backwards(speed1, speed2):
    d.backwards(speed1)
    time.sleep(1)
    d.TurnLeft(speed2)
    time.sleep(0.5)
    global count
    count += 1

def scout():
    dist = (e.reading(0))
    if all(t == 1 for t in d.ir_read()):
        print(dist)
        d.backwards(75)
        time.sleep(0.5)
        print("backwards")
    elif dist > range:
        print(dist)
        d.TurnLeft(50)
        print("left")
        time.sleep(0.2)
    elif dist < range:
        while any(t == 0 for t in d.ir_read()):
            print(dist)
            d.forward(65)
            print("forward")
            time.sleep(0.01)
        backwards(65, 50)

# When recieving ctrl-C
signal.signal(signal.SIGINT, d.handler)

main()

