from abstractSerial import AbstractSerial
from abstractModem import AbstractModem
from random import randrange
from typing import List

import serial
import sys
import _thread

class SerialPort(AbstractSerial):
    def __init__(self) -> None:
        self.comportName = ""
        self.baud = 0
        self.timeout = 0
        self.ReceiveCallback = None
        self.isopen = False
        self.receivedBit = None
        self.serialport = serial.Serial()
        
        # The Subject owns some important state and notifies modems when the state changes.
        self._state: int = None

        #For the sake of simplicity, the Subject's state, essential to all subscribers, is stored in this variable.
        self._modem: List[AbstractModem] = []

######################  Serial port methods  ########################    
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


################### Observe patter methods ########################

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, modem: AbstractModem) -> None:
        print("Subject: Attached an modem.")
        self._modem.append(modem)

    def detach(self, modem: AbstractModem) -> None:
        self._modem.remove(modem)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying modems...")
        for modem in self._modem:
            modem.update(self)

"""     def some_business_logic(self) -> None:
        
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
       

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify() """
