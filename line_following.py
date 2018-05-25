import time
import directions as d


def main():
    while True:
        ir_read = d.ir_read()
        if ir_read[1] == 1 and ir_read[2] == 1:
            d.forward()
            print ("Forward")
        elif ir_read[0] == 1 and ir_read[1] == 1:
            d.TurnRight()
            print ("Turning Right")
        elif ir_read[0] == 1:
            d.TurnRight()
            print ("Turning Right")
        elif ir_read[3] == 1 and ir_read[2] == 1:
            d.TurnLeft()
            print ("Turning Left")
        elif ir_read[3] == 1:
            d.TurnLeft()
            print ("Turning Left")
        time.sleep(0.01)
        print (d.ir_read())

main()