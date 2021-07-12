from abc import ABC, abstractmethod #https://docs.python.org/3/library/abc.html
from abstractSerial import AbstractSerial
from serial.serialwin32 import Serial
from serialPort import SerialPort

# serialPort = SerialPort()

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
