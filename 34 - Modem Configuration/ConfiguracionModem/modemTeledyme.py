
import time
import sys
from typing import Tuple

#XML Manipulation
import xml.dom.minidom

from serialProcessor import SerialPort
from serialProcessor import Processor
class ModemTeledyne():
    '''
    Modem se encargará de enviar todos los comando de configuraión mientras que 
    Processor se encargarás de validar que la información que llega es correcta
    '''
    def __init__(self) -> None:
        self.serial1    = {}
        self.serial2    = {}
        self.system     = {}
        self.modem      = {}
        self.release    = {}
        self.transport  = {}
        self.test       = {}
        self.xpnd       = {}
        self.nav        = {}

        # self.textReceived = []

        # #This flag if for Controling the loop
        # self.flag = False

        teledyne = xml.dom.minidom.parse('config\\localModemConfig.xml') 
        # teledyne = xml.dom.minidom.parse('D:\\xx - Github\\My-python-Workbook\\32 - Configurar modems\\config\\localModemConfig.xml') #TODO: change the path, not make it hard coded
        
        self.handleteledyne(teledyne=teledyne)


    ############################# XML config ###############################################
    
    def handleteledyne(self,teledyne):
        # handleteledyneTitle(teledyne.getElementsByTagName("title")[0])
        serial1      = teledyne.getElementsByTagName("serial1")
        serial2      = teledyne.getElementsByTagName("serial2")
        system       = teledyne.getElementsByTagName("system")
        modem        = teledyne.getElementsByTagName("modem")
        release      = teledyne.getElementsByTagName("release")
        transport    = teledyne.getElementsByTagName("transport")
        test         = teledyne.getElementsByTagName("test")
        xpnd         = teledyne.getElementsByTagName("xpnd")
        nav          = teledyne.getElementsByTagName("nav")

        self.handleSerial(serial=serial1, type=1)
        self.handleSerial(serial=serial2, type=2)
        self.handleSystem(system=system)
        self.handleModem(modem=modem)
        self.handleRelease(release=release)
        self.handleTransport(transport=transport)
        self.handleTest(test=test)
        self.handleXpnd(xpnd=xpnd)
        self.handleNav(nav=nav)

    def handleSerial(self,serial,type):
        items = serial[0].getElementsByTagName("item")
        if type == 1:
            for elem in items:
                self.serial1[elem.attributes['name'].value] = elem.firstChild.data
        elif type == 2:
            for elem in items:
                self.serial2[elem.attributes['name'].value] = elem.firstChild.data
        else:
            print('<modem><handleSerial> el tipo seleccionado no es valido')

    def handleSystem(self,system):
        items = system[0].getElementsByTagName("item")
        for elem in items:
            self.system[elem.attributes['name'].value] = elem.firstChild.data
        # print("\n")

    def handleModem(self,modem):
        items = modem[0].getElementsByTagName("item")
        for elem in items:
            self.modem[elem.attributes['name'].value] = elem.firstChild.data
        # print("\n")

    def handleRelease(self,release):
        items = release[0].getElementsByTagName("item")
        for elem in items:
            self.release[elem.attributes['name'].value] = elem.firstChild.data
        # print("\n")

    def handleTransport(self,transport):
        items = transport[0].getElementsByTagName("item")
        for elem in items:
            self.transport[elem.attributes['name'].value] = elem.firstChild.data
        # print("\n")

    def handleTest(self,test):
        items = test[0].getElementsByTagName("item")
        for elem in items:
            self.test[elem.attributes['name'].value] = elem.firstChild.data
        # print("\n")

    def handleXpnd(self,xpnd):
        items = xpnd[0].getElementsByTagName("item")
        for elem in items:
            self.xpnd[elem.attributes['name'].value] = elem.firstChild.data
        # print("\n")

    def handleNav(self,nav):
        items = nav[0].getElementsByTagName("item")
        for elem in items:
            self.nav[elem.attributes['name'].value] = elem.firstChild.data
        # print("\n")

    ############################# Configure Modem ###############################################
    def configure_modem(self, serialPort: SerialPort, procesor:Processor): #COMEBACK: serial port object as parameter
        '''
        This function gonna take all the parameter loaded from the XML and confiure the modem
        using a serial port object
        '''
        #COMEBACK: Implemente de validation from the processor. this is a test.
        _key = "P1Baud"
        self.sendCommand(serialPort,'@' + _key + '=' + self.serial1[_key])
        procesor.set_is_command_at(True) #TODO: this can be insede set_command_clam
        procesor.set_command_clam(_key)
        time.sleep(1)
        # try:
        #     ###################  Serial1 ######################
        #     for key in self.serial1:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.serial1[key])
        #         procesor.status_command_clam = True
        #         procesor.command_clam(key)
        #         time.sleep(1)
        #    ###################  Serial2 ######################
        #     for key in self.serial2:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.serial2[key])
        #         time.sleep(1)
        #     ###################  system ######################
        #     for key in self.system:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.system[key])
        #         time.sleep(1)
        #     ###################  modem ######################
        #     for key in self.modem:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.modem[key])
        #         time.sleep(1)
        #     ###################  Release ######################
        #     for key in self.release:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.release[key])
        #         time.sleep(1)
            
        #     ###################  transport ######################
        #     for key in self.transport:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.transport[key])
        #         time.sleep(1)
            
        #     ###################  Test ######################
        #     for key in self.test:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.test[key])
        #         time.sleep(1)

        #     ###################  xpnd ######################
        #     for key in self.xpnd:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.xpnd[key])
        #         time.sleep(1)
            
        #     ###################  nav ######################
        #     for key in self.nav:
        #         self.sendCommand(serialPort,'@' + key + '=' + self.nav[key])
        #         time.sleep(1)
        # except KeyError as e:
        #     print("<SerialPorti><readLine>: Error reading COM port: ", sys.exc_info()[0])
        

    ############################# AT commands ###############################################
    #TODO: Implement a method for each AT command

    def sendCommand(self,serialPort: SerialPort,command):
        serialPort.Send(command + '\r\n')

    def closeCommandLow(self,serialPort: SerialPort) -> bool:
        # serialPort.Send('ATL\r\n')
        # time.sleep(5)
        # src_str = serialPort.receivedMessage #COMEBACK: pass the serial port object as an argument
        # src_str = src_str.decode("utf-8")
        # try:
        #     sub_index   = src_str.find('Lowpower')
        #     if sub_index != -1:
        #         return True
        #     else:
        #         return False
        # except AttributeError as error:
        #     print(f'<modem><closeCommandLow>: {error}')
        #     sys.exit(1)
        pass
            
    def closeCommandOnline(self,serialPort: SerialPort) -> bool:
        # serialPort.Send('ATO\r\n') 
        # time.sleep(5)
        # src_str = serialPort.receivedMessage 
        # src_str = src_str.decode("utf-8")
        # try:
        #     sub_index   = src_str.find('Lowpower') #TODO: Need to be check. This is not the message i receive
        #     if sub_index != -1:
        #         return True
        #     else:
        #         return False
        # except AttributeError as error:
        #     print(f'<modem><closeCommandOnline>: {error}')
        #     sys.exit(1)
        pass


if __name__ == "__main__":
    modem_teledyne = ModemTeledyne()

    #Prueba para validar configuración
    for key in modem_teledyne.serial1:
        print('@' + key + '=' + modem_teledyne.serial1[key])
        

