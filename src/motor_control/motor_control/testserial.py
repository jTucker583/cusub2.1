import serial.tools.list_ports as lp

def list_ports():
    ports = lp.comports()
    for port in ports:
        print(port)

list_ports()