import directions as d
import echo as e
import time


# max distance 180 cm

def main():
    if any(t == 1 for t in d.ir_read()):
        d.TurnLeft()
    elif e.reading(0) > 180:
        d.forward()
    time.sleep(0.2)

main()