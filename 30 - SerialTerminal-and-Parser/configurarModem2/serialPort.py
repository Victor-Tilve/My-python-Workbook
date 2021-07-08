import serial
import sys
import _thread

class SerialPort:
    def __init__(self):
        self.comportName = ""
        self.baud = 0
        self.timeout = 0
        self.ReceiveCallback = None
        self.isopen = False
        self.receivedBit = None
        self.serialport = serial.Serial()

    def __del__(self):
        try:
            if self.serialport.is_open():
                self.serialport.close()
        except:
            print("<SerialPorti><__del__>: Destructor error closing COM port: ", sys.exc_info()[0] )

    def RegisterReceiveCallback(self,aReceiveCallback):
        self.ReceiveCallback = aReceiveCallback
        try:
            _thread.start_new_thread(self.readLine, ())
            # print('<SerialPorti><RegisterReceiveCallback>: thread started')
        except:
            print("<SerialPorti><RegisterReceiveCallback>: Error starting Read thread: ", sys.exc_info()[0])

    def readLine(self):
        while True:
            try:
                if self.isopen:
                    # print(f'<SerialPorti><readLine>: Inside conditional')
                    # self.receivedBit = self.serialport.readline()
                    self.receivedBit = self.serialport.read()
                    if self.receivedBit != "":
                        # print(f'<SerialPorti><readLine>: {self.receivedBit.decode("utf-8")}')
                        self.ReceiveCallback(self.receivedBit)

            except:
                print("<SerialPorti><readLine>: Error reading COM port: ", sys.exc_info()[0])
                sys.exit(1)


    def IsOpen(self):
        return self.isopen

    def Open(self,portname,baudrate):
        if not self.isopen:
            # serialPort = 'portname', baudrate, bytesize = 8, parity = 'N', stopbits = 1, timeout = None, xonxoff = 0, rtscts = 0)
            self.serialport.port = portname
            self.serialport.baudrate = baudrate
            try:
                self.serialport.open()
                self.isopen = True
            except:
                print("<SerialPorti><Open>: Error opening COM port: ", sys.exc_info()[0])
                sys.exit(1)

    def Close(self):
        if self.isopen:
            try:
                self.serialport.close()
                self.isopen = False
            except:
                print("Close error closing COM port: ", sys.exc_info()[0])

    def Send(self,message):
        if self.isopen:
            try:
                # Ensure that the end of the message has both \r and \n, not just one or the other
                newmessage = message.strip()
                newmessage += '\r\n'
                self.serialport.write(newmessage.encode('utf-8'))
            except:
                print("Error sending message: ", sys.exc_info()[0] )
            else:
                return True
        else:
            return False




