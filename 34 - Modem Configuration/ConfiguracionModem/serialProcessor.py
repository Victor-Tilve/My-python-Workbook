from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep #https://docs.python.org/3/library/abc.html
# from random import randrange
from typing import List
import threading

import time

import serial
import sys
# import _thread



################################## Serial ###############################################

class AbstractSerial(ABC):
    """
    The AbstractSerial interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, abstractProcessor: AbstractProcessor) -> None:
        """
        Attach an AbstractProcessor to the AbstractSerial.
        """
        pass

    @abstractmethod
    def detach(self, abstractProcessor: AbstractProcessor) -> None:
        """
        Detach an AbstractProcessor from the AbstractSerial.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all AbstractProcessors about an event.
        """
        pass

class SerialPort(AbstractSerial):

    def __init__(self) -> None:
        self.comportName = ""
        self.baud = 0
        self.timeout = 0
        self.ReceiveCallback = None
        self.isopen = False
        self.receivedData = []
        self._state: bool = False             # una bandera para saber si hay datos 
        self.serialport = serial.Serial()
        self.exitapp: bool = False

        """
        The AbstractSerial owns some important state and notifies AbstractProcessors when the state
        changes.
        """

        """
        For the sake of simplicity, the AbstractSerial's state, essential to all
        subscribers, is stored in this variable.
        """
        self._state: bool = False
        """
        List of subscribers. In real life, the list of subscribers can be stored
        more comprehensively (categorized by event type, etc.).
        """
        self.abstractProcessors: List[AbstractProcessor] = []
    
    ################### Observe patter methods ########################
    def attach(self, AbstractProcessor: AbstractProcessor) -> None:
        print("AbstractSerial: Attached an AbstractProcessor.")
        # self.RegisterReceiveCallback()
        # print(str(threading.current_thread()))
        self.abstractProcessors.append(AbstractProcessor)

    def detach(self, AbstractProcessor: AbstractProcessor) -> None:
        self.abstractProcessors.remove(AbstractProcessor)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("<classes><AbstractSerial>: Notifying AbstractProcessors...")
        for AbstractProcessor in self.abstractProcessors:
            AbstractProcessor.update(self)

    ######################  setters  ########################    
    def data_status(self):
        '''
        Change the value of the flag
        '''
        self._state = not(self._state)
    ######################  Serial port methods  ########################    
    def RegisterReceiveCallback(self): #TODO: I have to pass this parameter like  "self"
        
        try:
            # _thread.start_new_thread(self.readLine(), ())
            self._thread = threading.Thread(target=self.readLine)
            self._thread.start()
            print('<classes><RegisterReceiveCallback>: thread started')
        except:
            print("<SerialPorti><RegisterReceiveCallback>: Error starting Read thread: ", sys.exc_info()[0])
    
    def readLine(self,):
        '''
        this is the function that will be running in the background. 
        i'm going to use 2 flags, one if there is information arraving in the serial port, 
        the other one if the buffer is full. if there is information in the buffer but 
        the buffer is not full, after 15 sec, then send the information to the listener anyway
        '''
        # start_time = time.time()

        while not self.exitapp:
            # print(f'<SerialPorti><readLine>: Inside while (self.exitapp)')
            try:
                if self.isopen:
                    # print(f'<SerialPorti><readLine>: Inside conditional:')
                    
                    if self.serialport.inWaiting() > 0:
                        self._state = True #TODO: find the point where put it False again (Observer, method already created). Delete, this work is being performance by _status
                         
                        self._state = True #COMEBACK:   what do i do with this flag? seria el mismo de data
                        # print(f'<SerialPorti><readLine>: Hay dato en puerto')
                        
                        receivedBit = self.serialport.read(self.serialport.inWaiting()) 
                        
                        # self.receivedData.append(receivedBit.decode("utf-8"))
                        self.receivedData.append(receivedBit.decode("utf-8"))                        
                        self.notify()

                    # else:
                    #     print(f'<SerialPorti><readLine>: No data')
            except:
                print("<SerialPorti><readLine>: Error reading COM port: ", sys.exc_info()[0])    
                sys.exit(1)
            time.sleep(1.5)

    def exit_thread(self):
        self.exitapp = True

    def IsOpen(self):
        return self.isopen

    def Open(self,portname,baudrate):
        if not self.isopen:
            # serialPort = 'portname', baudrate, bytesize = 8, parity = 'N', stopbits = 1, timeout = None, xonxoff = 0, rtscts = 0)
            self.serialport.port = portname
            self.serialport.baudrate = baudrate
            try:
                self.serialport.open()
                self.RegisterReceiveCallback()
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

################################## Processor ###############################################
class AbstractProcessor(ABC):
    """
    The AbstractProcessor interface declares the update method, used by AbstractSerials.
    """

    @abstractmethod
    def update(self, AbstractSerial: AbstractSerial) -> None:
        """
        Receive update from AbstractSerial.
        """
        pass

class Processor(AbstractProcessor):
    """
    Concrete AbstractProcessors react to the updates issued by the AbstractSerial they had been
    attached to.
    """
    # def __init__(self,serialPort: SerialPort) -> None:
    def __init__(self) -> None:
        self._state: bool = False
        self.buffer: str = ""
        # serialPort.RegisterReceiveCallback(self.OnReceiveSerialData) #COMEBACK: Do i need this
        
        #TODO: Use this in the modem program for sending commands
        self.at_command : bool = False      #Help me to know when i have to check a Clam or at command
        self.clam_command : bool = False    #Help me to know when i have to check a Clam or at command

    def preprocess_buffer(self):
        pass

    def process_status(self):
        pass
    
    def postprocess_status(self):
        pass

    def clam_commnad(self):
        pass

    def check_at_command(self,command)-> bool:
        
        if self.buffer.find(command) != -1:
            if self.buffer.find('Bad') == -1: #COMEBACK: look for the at answer and develope the proper method
                return self.commandModeCheck()
            else:
                return False    
        else:
            return False  

    def check_command_prompt(self)-> bool:
        if self.buffer.find('>') != -1:
            print(f'<modem><commandModeCheck>: Modo comando activo')    
            return True
        else:
            return False    

    
    def check_command_CLAM(self,command)-> bool: #TODO: how the program knows when                                                                               
    
        if self.buffer.find(command) != -1:
            if self.buffer.find('Bad') == -1:
                return self.commandModeCheck()
            else:
                return False    
        else:
            return False    

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
            self._state = True #flag for controlling the main thread
            for chr in abstractSerial.receivedData:
                self.buffer += chr
            # print(str(threading.current_thread()))
            print(f"Processor: Reacted to the event\n {self.buffer}")
            abstractSerial.data_status()

            self.buffer = ""
            abstractSerial.receivedData.clear()

    ###################### Decoded received messages #############################
    #TODO: do this for every AT command
    def ATX(src_str):
        sub_index   = src_str.find('MOD:')
        MOD         = src_str[sub_index + 4:sub_index + 6]
        sub_index   = src_str.find('ERR:')
        ERR         = src_str[sub_index + 4:sub_index + 7]
        sub_index   = src_str.find('SNR:')
        SNR         = src_str[sub_index + 4:sub_index + 8]
        sub_index   = src_str.find('AGC:')
        AGC         = src_str[sub_index + 4:sub_index + 6]
        sub_index   = src_str.find('SPD:')
        SPD         = src_str[sub_index + 4:sub_index + 9]
        sub_index   = src_str.find('CCERR:')
        CCERR       = src_str[sub_index + 6:sub_index + 9]

        print(f'el valor de MOD es: {MOD}')
        print(f'el valor de ERR es: {ERR}')
        print(f'el valor de SNR es: {SNR}')
        print(f'el valor de AGC es: {AGC}')
        print(f'el valor de SPD es: {SPD}')
        print(f'el valor de CCERR es: {CCERR}')


###################### Modem class #############################

