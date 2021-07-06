import xml.dom.minidom
import time


class Modem:
    def __init__(self,config_path) -> None:
        self.serial1    = {}
        self.serial2    = {}
        self.system     = {}
        self.modem      = {}
        self.release    = {}
        self.transport  = {}
        self.test       = {}
        self.xpnd       = {}
        self.nav        = {}
    
        teledyne = xml.dom.minidom.parse(config_path)
        self.handleteledyne(teledyne=teledyne)
        # for key in self.serial1:
        #     print(key +' : ' + self.serial1[key])


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

if __name__ == '__main__':
    modem = Modem('config\\remoteModemConfig.xml')
    for key in modem.serial1:
        print('@' + key + '=' + modem.serial1[key])
        time.sleep(1)