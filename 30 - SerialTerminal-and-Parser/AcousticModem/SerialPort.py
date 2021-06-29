import serial

''' La configuración de la puerta serial se debe leer desde el GUI'''

class SerialPort:
    def __init__(self,port,baudrate) -> None:
        self.port       = port
        self.baudrate   = baudrate
        self.ser             = serial.Serial(
        port            = self.port,
        baudrate        = self.baudrate,
        parity          = serial.PARITY_NONE,
        stopbits        = serial.STOPBITS_ONE,
        bytesize        = serial.EIGHTBITS)
        self.ser.timeout = 5
        # self.ser.write("OUTP? 1 \r\n".encode()) #Asks the Lock-in for x-value
        # self.ser.write("++read\r\n".encode())
    #TODO: This must be implemented with threads
    def printsent(self,message:'str'):
        # while True:
        buffer = "" #TODO: Should I define how big is this buffer?
        self.ser.write(f"{message}\r\n".encode())
        
        while True:
            oneByte = self.ser.read(1)
            if oneByte == b"\r":    #method should returns bytes
                print (buffer)
                self.ser.write("Received\r\n".encode())
                break
            else:
                buffer += oneByte.decode()
        

if __name__ == '__main__': 
    serialPort = SerialPort('COM11',9600)
    serialPort.printsent("Hola, mundo")