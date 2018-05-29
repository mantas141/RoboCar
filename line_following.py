import time
import directions as d
import signal



def main():
    while True:
        ir_read = d.ir_read()
        if ir_read[1] == 1 and ir_read[2] == 1:
            d.forward(75)
            print ("Forward")
        elif ir_read[3] == 1 and ir_read[2] == 1:
            d.TurnRight(75)
            print ("Turning Right")
        elif ir_read[3] == 1:
            d.TurnRight(75)
            print ("Turning Right")
        elif ir_read[0] == 1 and ir_read[1] == 1:
            d.TurnLeft(75)
            print ("Turning Left")
        elif ir_read[0] == 1:
            d.TurnLeft(75)
            print ("Turning Left")
        time.sleep(0.01)
        print (d.ir_read())

# When recieving ctrl-C
signal.signal(signal.SIGINT, d.handler)

main()