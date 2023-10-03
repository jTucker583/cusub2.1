import serial
import time

#setting up microcontroller
servo = serial.Serial('COM10',9600) # probably can just change this to our port
PololuCmd = bytearray([0xAA,0x0C])
extensionPin = 0x016 # this indexing is wrong, need to change
w3Pin = 0x014
w6Pin = 0x015

high = 1999
low = 1000

#pololu commands
def sendCMD(cmd):
    cmdStr = PololuCmd + cmd
    servo.write(cmdStr)
    print(cmdStr)

def setTarget(chan, target):
    target = target*4
    lsb = target & 0x7f #7 bits for least significant byte
    msb = (target >> 7) & 0x7f #shift 7 and take next 7 bits for msb
    cmd = bytearray([0x04, chan, lsb, msb])
    sendCMD(cmd)

def impact():
    time.sleep(1)
    setTarget(extensionPin, high)
    time.sleep(0.05)
    setTarget(extensionPin, low)

def trending():
    setTarget(w3Pin, high)
    time.sleep(1)    

    setTarget(w6Pin, high)
    time.sleep(1)

    setTarget(w3Pin, low)
    time.sleep(1)

    setTarget(w6Pin, low)

def main(cycles):  
    for i in range(cycles + 1):
        if i % trendInterval == 0:
            trending()
        impact()
        print('cycle #' + str(i))

trendInterval = 100
main(1000)


