from abstractModem import AbstractModem
from abstractSerial import AbstractSerial

from serialPort import SerialPort
import xml.dom.minidom
import time
import sys

serialPort = SerialPort()


class ModemTeledyne(AbstractModem):

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

        #This flag if for Controling the loop
        self.flag = False

        teledyne = xml.dom.minidom.parse('C:\\Users\\vtilve\\Desktop\\VictorTilve\\GitHub\\My-python-Workbook\\30 - SerialTerminal-and-Parser\\configurarModem2\\config\\localModemConfig.xml') #TODO: change the path, not make it hard coded
        # teledyne = xml.dom.minidom.parse('D:\\xx - Github\\My-python-Workbook\\32 - Configurar modems\\config\\localModemConfig.xml') #TODO: change the path, not make it hard coded
        
        self.handleteledyne(teledyne=teledyne)

        serialPort.Open(port,baud)
        serialPort.RegisterReceiveCallback(self.OnReceiveSerialData)
        # time.sleep(1)
        # if self.commandMode():
        #     # print('<modem><__init__>:exit command mode')
        #     for key in self.modem:
        #         self.sendCommand('@' + key + '=' + self.modem[key])
        #         time.sleep(1)
        #         if self.CheckClamCommand(key):
        #             print('@' + key + '=' + self.modem[key] + '\t\t\tDONE')
        #         # elif self.commandModeCheck():

        for key in self.serial1:
            self.sendCommand('@' + key + '=' + self.serial1[key])
            time.sleep(1)
            if self.CheckClamCommand(key): #TODO: Eliminar los parametros almacenados en el buffer self.textReceived con pop(0:tamaño buffer)
                print('@' + key + '=' + self.serial1[key] + '\t\t\tDONE')
            else:
                print('@' + key + '=' + self.serial1[key] + '\t\t\tERROR')
        
    ############# Send command functions #############

    
    def commandMode(self) -> bool:
        '''
        Messages examples
        +++#CR#LFCommand '+++' not found#CR#LFError#CR#LFuser:12>
        +++#CR#LFuser:145>
        +++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:147>    
        '''
        serialPort.Send('+++\r\n') 
        time.sleep(1)
        if self.flag:
            return self.commandModeCheck()

    def commandModeCheck(self)->bool:
        found_flag = False
        # print(f'<modem><commandModeCheck>: Inside function')
        while len(self.textReceived) != 0:
            if self.textReceived.pop() == '>':
                print(f'<modem><commandModeCheck>: Modo comando activo')
                self.textReceived.clear()
                found_flag = True
                return True
        if len(self.textReceived) == 0 and not found_flag:
            print(f'<modem><commandModeCheck>: No se estableció conexión')
            return False

    def CheckClamCommand(self,command):
        ''' Esta funcion verifica si el modem respondio con el conmando configurado, es decir,
            que la configuración se realizó
        '''
        seconds = 10
        elapse = 0
        startTime = time.time()
        while elapse < seconds:
            elapse = time.time() - startTime
            str_buffer =""
            # print(f'<modem><CheckClamCommand> Before: {self.textReceived}')
            for chr in self.textReceived:
                str_buffer+=chr
            # print(f'<modem><CheckClamCommand> After: {self.textReceived}')
            # print(f'<modem><CheckClamCommand>: {str_buffer}')
            '''El bucle se mantendrá activo por 10 seg si no encuentra el comando programado'''
            if str_buffer.find(command) != -1:
                if str_buffer.find('Bad') == -1:
                    return self.commandModeCheck()
                else:
                    return False    
            else:
                return False    
            

#####

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


############################# XML extract config ###############################################
    
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


################### TetReceived ########################

    def OnReceiveSerialData(self,message):
        '''Almacena toda la información que proviene desde la puerta serial'''
        self.textReceived.append(message.decode("utf-8")) #TODO: debo limpiar el buffer previo a enviar un nuevo comando
        # print(f'<modem><OnReceiveSerialData>: {self.textReceived}')
        if self.textReceived != "":
            self.flag = True

################### Observe patter methods ########################

    def update(self, abstractSerial: AbstractSerial) -> None:
        if abstractSerial._state < 3:
            print("ModemTeledyne: Reacted to the event")