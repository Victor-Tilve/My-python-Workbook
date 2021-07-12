# from processor import Processor
from classes2 import SerialPort,Processor
import sys
import time

import threading

serialPort = SerialPort()
port = "COM11"
baud = 9600
serialPort.Open(port,baud)

processor = Processor()


serialPort.attach(processor)
# serialPort.RegisterReceiveCallback()

# print(str(threading.current_thread()))

serialPort.Send('Hola, Terminal' + '\r\n')
while True:
    # print('<test><While>:dentro del bucle')
    # print(f'<test><While>:processor._state = {processor._state}')
    # print(str(threading.current_thread()))
    try:
        if processor._state:
            print('<test><While>:dentro del condicional')
            processor._state = False
        time.sleep(1.5)
    except KeyboardInterrupt:
        print("<test><while>: ", sys.exc_info()[0])
        serialPort.Close()
        serialPort.exit_thread()
        sys.exit(1)
