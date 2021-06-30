from tkinter import *

class Application(Frame):
    """Build the windows to show 20x10 Customer Pole Display data"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label1 = Label(self, text='Text window for data from serial port:')
        self.label1.grid(row=0, column=0, sticky =W)

        self.text1 = Text(self, width=20, height=2)
        self.text1.grid(row=1, column=0)
        self.text1.focus_set()


    def writeDisplay(self,inputCharacter):
        myCharacter = inputCharacter
        varText = self.text1.get("1.0", END)
        varReplaced = varText + myCharacter
        self.text1.delete("1.0", END)
        self.text1.insert(END, varReplaced)

    def openDisplay(self):
        root = Tk()
        root.title('Text widget test')
        root.geometry('360x250')
        #app = Application(root)
        app.mainloop()

class mySerialport():
    import serial, time    #initialization and open the port
    def __init__(self) -> None:    
        global ser
        ser = self.serial.Serial()        
        ser.port = "COM11"
        #ser.port = "COM2"
        ser.baudrate = 9600
        ser.bytesize = self.serial.EIGHTBITS #number of bits per bytes
        ser.parity = self.serial.PARITY_NONE #set parity check: no parity
        ser.stopbits = self.serial.STOPBITS_ONE #number of stop bits
        #ser.timeout = None          #block read
        ser.timeout = 1            #non-block read
        #ser.timeout = 2              #timeout block read
        ser.xonxoff = False     #disable software flow control
        ser.rtscts = False     #disable hardware (RTS/CTS) flow control
        ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
        ser.writeTimeout = 2     #timeout for write
                                #possible timeout values:
                                #    1. None: wait forever, block call
                                #    2. 0: non-blocking mode, return immediately
                                #    3. x, x is bigger than 0, float allowed, timeout block call

    def myOpenSerialPort(self):
        try: 
            self.ser.open()
        except self.serial.SerialException:
            print ("error open serial port: " + ser.port )
            exit()

    def myReadbyte(self):
        if self.ser.isOpen():
            try:            
                response = self.ser.readline(1)
                return(response)
            #except Exception, e1:
            except self.serial.SerialException as e1:
                print ("error communicating...: " + str(e1))
        else:
            print ("cannot open serial port ")


if __name__ == "__main__":
    root = Tk()
    root.title('Text widget test')
    root.geometry('360x250')
    app = Application(root)
    app.mainloop()       

    #Open the serial port and get date.    
    mySerialport = mySerialport() #Create serial port.
    mySerialport.myOpenSerialPort() #Open the port.

    #Get serial data forever and write to GUI
    while(True):

        #getting serial data
        foo= mySerialport.myReadbyte()

        #writing serial data to display.
        Application.writeDisplay(foo)   #Place holder for writing to GUI text window.

        #For development, print to shell instead.
        print(foo.decode()) 