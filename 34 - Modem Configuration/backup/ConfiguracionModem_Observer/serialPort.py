# from processor import AbstractProcessor
# from random import randrange
from typing import List
from abc import ABC, abstractmethod #https://docs.python.org/3/library/abc.html
import serial
import sys
import _thread

class AbstractSerial(ABC):
    """
    The AbstractModem interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, abstractProcessor: AbstractProcessor) -> None:
        """
        Attach an AbstractModem to the AbstractSerial.
        """
        pass

    @abstractmethod
    def detach(self, abstractProcessor: AbstractProcessor) -> None:
        """
        Detach an abstractModem from the AbstractSerial.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all AbstractModems about an event.
        """
        pass

class SerialPort(AbstractSerial):
    def __init__(self) -> None:
        self.comportName = ""
        self.baud = 0
        self.timeout = 0
        self.ReceiveCallback = None
        self.isopen = False
        self.receivedBit = None
        self.serialport = serial.Serial()
        
        # The Subject owns some important state and notifies processors when the state changes.
        self._state: bool = False

        #For the sake of simplicity, the Subject's state, essential to all subscribers, is stored in this variable.
        self._processor: List[AbstractProcessor] = []

  ######################  Serial port methods  ########################    
    def RegisterReceiveCallback(self): #TODO: I have to pass this parameter like  "self"
        
        try:
            _thread.start_new_thread(self.readLine(), ())
            # print('<SerialPorti><RegisterReceiveCallback>: thread started')
        except:
            print("<SerialPorti><RegisterReceiveCallback>: Error starting Read thread: ", sys.exc_info()[0])
    
    def readLine(self,):
        while True:
            try:
                if self.isopen:
                    # print(f'<SerialPorti><readLine>: Inside conditional')
                    # self.receivedBit = self.serialport.readline()
                    self.receivedBit = self.serialport.read()
                    if self.receivedBit != "": #TODO: Notify to the observer
                        # print(f'<SerialPorti><readLine>: {self.receivedBit.decode("utf-8")}')
                        self._state = True
                        self.notify()
                        # self.ReceiveCallback(self.receivedBit)
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

    def attach(self, processor: AbstractProcessor) -> None:
        print("Subject: Attached an processor.")
        self._processor.append(processor)

    def detach(self, processor: AbstractProcessor) -> None:
        self._processor.remove(processor)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying processors...")
        for processor in self._processor:
            processor.update(self)

    """def some_business_logic(self) -> None:
        
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
       

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify() """


class AbstractProcessor(ABC):
    """
    The AbstractProcessor interface declares the update method, used by abstractSerial.
    """

    @abstractmethod
    def update(self, abstractSerial: AbstractSerial) -> None:
        """
        Receive update from abstractSerial.
        """
        pass


class Processor(AbstractProcessor):
    def __init__(self,serialPort: SerialPort) -> None:
        self._state: bool = False
        serialPort.RegisterReceiveCallback(self.OnReceiveSerialData)

    def preprocess_buffer(self):
        pass

    def process_data(self):
        pass
    
    def postprocess_data(self):
        pass

    def clam_commnad(self):
        pass

    def at_command(self):
        pass

    def check_command_prompt(self):
        pass
    
    #
    def OnReceiveSerialData(self,message):
        # '''Almacena toda la información que proviene desde la puerta serial'''
        # self.textReceived.append(message.decode("utf-8")) #TODO: debo limpiar el buffer previo a enviar un nuevo comando
        # # print(f'<modem><OnReceiveSerialData>: {self.textReceived}')
        # if self.textReceived != "":
        #     self.flag = True
        pass

    #Obverb pattern's Methods

    def update(self, abstractSerial: AbstractSerial) -> None:
        if abstractSerial._state:
            self._state = True
            print("Processor: Reacted to the event")



