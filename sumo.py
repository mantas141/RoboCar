import directions as d
import echo as e
import time

# max distance 180 cm
count = 0
def main():
    #while count < 4:
    #    scout()
    while True:
        scout()

def backwards():
    d.backwards()
    time.sleep(1)
    d.TurnLeft()
    time.sleep(0.2)
    global count
    count += 1

def scout():
    dist = (e.reading(0))
    print(dist)
    if all(t == 1 for t in d.ir_read()):
        d.backwards()
        time.sleep(0.5)
        print("backwards")
    elif dist > 180 and any(t == 0 for t in d.ir_read()):
        d.TurnLeft()
        print("left")
    elif dist < 180 and any(t == 0 for t in d.ir_read()):
        d.forward()
        print("forward")
        time.sleep(1)
        backwards()




main()