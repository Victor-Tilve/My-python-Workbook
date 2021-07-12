# from processor import Processor
from serialPort import SerialPort,Processor

processor = Processor()
serialPort = SerialPort()

serialPort.attach(processor)

port = "COM11"
baud = 9600

serialPort.Open(port,baud)
serialPort.Send('Hola, Terminal' + '\r\n')
while True:
    if processor._state:
        print('<test><While>:dentro del bucle')
        processor._state = False
