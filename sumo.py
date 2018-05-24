import directions as d
import echo as e
import time

# max distance 180 cm
count = 0
def main():
    while count < 4:
        scout()

def backwards():
    d.backwards()
    time.sleep(1)
    d.TurnLeft()
    time.sleep(0.2)
    global count
    count += 1


def scout():
    r = range(5, 180)
    if any(t == 1 for t in d.ir_read()):
        backwards()
    elif e.reading(0) < 180 and any(t == 0 for t in d.ir_read()):
        d.TurnLeft()
    elif e.reading(0) in r and any(t == 0 for t in d.ir_read()):
        d.forward()




main()