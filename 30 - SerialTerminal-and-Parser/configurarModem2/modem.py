'''
this configuration apply for the local and the remote modem. I have to make sure of that
'''
from __future__ import print_function
from serialPort import SerialPort
import xml.dom.minidom
import time
import sys

import serial

serialPort = SerialPort()

class Modem:
    def __init__(self,port,baud) -> None:
        self.serial1    = {}
        self.serial2    = {}
        self.system     = {}
        self.modem      = {}
        self.release    = {}
        self.transport  = {}
        self.test       = {}
        self.xpnd       = {}
        self.nav        = {}

        self.textReceived = []
        teledyne = xml.dom.minidom.parse('C:\\Users\\vtilve\\Desktop\\VictorTilve\\GitHub\\My-python-Workbook\\30 - SerialTerminal-and-Parser\\configurarModem2\\config\\localModemConfig.xml') #TODO: change the path, not make it hard coded
        # teledyne = xml.dom.minidom.parse('D:\\xx - Github\\My-python-Workbook\\32 - Configurar modems\\config\\localModemConfig.xml') #TODO: change the path, not make it hard coded
        
        self.handleteledyne(teledyne=teledyne)

        serialPort.Open(port,baud)
        serialPort.RegisterReceiveCallback(self.OnReceiveSerialData)
        # time.sleep(1)
        if self.commandMode():
            print('<modem><__init__>:exit command mode')
            # for key in self.serial1:
            #     self.sendCommand('@' + key + '=' + self.serial1[key])
            #     time.sleep(1)
        # if self.closeCommandLow():

        
    ############# Send command functions #############

    # +++#CR#LFCommand '+++' not found#CR#LFError#CR#LF
    # +++#CR#LFuser:145>
    # +++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:147>
    def commandMode(self):
        
        serialPort.Send('+++\r\n') 
        time.sleep(5)
        # src_str = serialPort.receivedMessage #COMEBACK: This work because i use <CR><LF> after >, but it doesn't happent in the REALITY
        for message in self.textReceived: 
            src_str = message
            # src_str = src_str.decode("utf-8")
            if src_str != "":
                print(f'<modem><commandMode> src_str:{src_str}')
        self.textReceived.clear
        # print(f'<modem><commandMode> src_str:{type(src_str)}')
        # try:
        #     sub_index   = src_str.find('>')
        #     if sub_index != -1:
        #         print('<modem><commandMode>:Listo para configurar')
        #         return True
        #     else:
        #         sub_index   = src_str.find('Command')
                
        #         if sub_index != -1:
        #             print('<modem><commandMode>: Command mode activo')
        #             return True
        #         else:
        #             print('<modem><commandMode>: No se estabeció comunicacion con modem')
        #             return False
        # except AttributeError as error: 
        #     print(f'<modem><commandMode>: {error}')
        #     sys.exit(1)

    def CheckClamCommand(self):
        pass

    #+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:122>at#CR#LFOK#CR#LFuser:123>atl#CR#LF#CR#LFuser:124>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:124>at#CR#LFOK#CR#LFuser:125>atl#CR#LF#CR#LFuser:126>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:126>at#CR#LFOK#CR#LFuser:127>atl#CR#LF#CR#LFuser:128>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:128>at#CR#LFOK#CR#LFuser:129>atl#CR#LF#CR#LFuser:130>Lowpower#CR#LF
    #+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:147>

    def sendCommand(self,command):
        serialPort.Send(command + '\r\n')
        #COMEBACK: A validation of the configuration
        
    # user:87>ATL#CR#LF#CR#LF#CR#LFuser:88>Lowpower#CR#LF
    # user:89>ATL#CR#LF#CR#LF#CR#LFuser:90>Lowpower#CR#LF
    def closeCommandLow(self) -> bool:
        serialPort.Send('ATL\r\n')
        time.sleep(5)
        src_str = serialPort.receivedMessage #COMEBACK: This work because i use <CR><LF> after >, but it doesn't happent in the REALITY
        src_str = src_str.decode("utf-8")
        try:
            sub_index   = src_str.find('Lowpower')
            if sub_index != -1:
                return True
            else:
                return False
        except AttributeError as error:
            print(f'<modem><closeCommandLow>: {error}')
            sys.exit(1)
            

    def closeCommandOnline(self) -> bool:
        serialPort.Send('ATO\r\n') 
        time.sleep(5)
        src_str = serialPort.receivedMessage 
        src_str = src_str.decode("utf-8")
        try:
            sub_index   = src_str.find('Lowpower') #TODO: Need to be check. This is not the message i receive
            if sub_index != -1:
                return True
            else:
                return False
        except AttributeError as error:
            print(f'<modem><closeCommandOnline>: {error}')
            sys.exit(1)


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
            print('<ReadingXML3><handleSerial> el tipo seleccionado no es valido')

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

###################### Decoded received messages #############################
  
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

    def AT(cmd_answer:'str'):
        print(f'el valor de CCERR es: ')


###############################################

    def OnReceiveSerialData(self,message):
        self.textReceived.append(message.decode("utf-8"))
        




# if __name__ == "__main__":
    