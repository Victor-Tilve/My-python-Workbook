import tkinter as tk
from tkinter import ttk
from tkinter.constants import NO

import serial
from serialPort import SerialPort

class Widgets(tk.Frame): #TODO: add the parameter of the frame
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window

        self.initUI()

    def initUI(self):
        
        #Frame for parameter
        self.labelframe_parameters=ttk.LabelFrame(self.window, text="Parameters:")
        self.labelframe_parameters.grid(column = 0,row = 1, padx = 5, pady = 10, sticky="nw")

        #Frame for MainMenu
        self.labelframe_mainMenu=ttk.LabelFrame(self.window, text="Main Menu:")
        self.labelframe_mainMenu.grid(column = 0,row = 2, padx = 5, pady = 10,sticky="nw")
        self.labelframe_commands=ttk.Frame(self.labelframe_mainMenu)
        self.labelframe_commands.grid(column = 1,row = 0, padx = 8, pady = 5,sticky="w")

        #Frame for Receive
        self.labelframe_received=ttk.LabelFrame(self.window, text="Received:")
        self.labelframe_received.grid(column = 1,row = 2, padx = 5, pady = 10, sticky="nw")

        #Frame for Sent
        self.labelframe_sent=ttk.LabelFrame(self.window, text="Sent:")
        self.labelframe_sent.grid(column = 1,row = 1, padx = 5, pady = 10, sticky="nw")

        ############################ Serial port ######################
        self.ser = SerialPort('COM11',9600) #TODO: Read from the combobox

        ############################ tkinter widgets ######################

        #### Widgest for Parameters #####
        self.parameters()

        #### Widgest for Sent #####
        self.sent()

        #### Widgest for MainMenu #####
        self.mainMenu()

        #### Widgest for Receive #####
        self.received()

        # self.btn_connect = ttk.Button(self.labelframe_parameters, text="Connect", command=self.portHandler(sentText))
        # self.btn_connect = ttk.Button(self.labelframe_parameters, text="Connect")
        # self.btn_connect.grid(column=0, row=2,columnspan=2, padx=4, pady=4)

    def parameters(self):
        # label labelframe_parameters
        ttk.Label(self.labelframe_parameters, text = "Port :",
                font = ("Times New Roman", 10)).grid(column = 0,
                row = 0, padx = 4, pady = 4, sticky="w")
        ttk.Label(self.labelframe_parameters, text = "Baud :",
                font = ("Times New Roman", 10)).grid(column = 0,
                row = 1, padx = 4, pady = 4, sticky="w")
        
        #  labelframe_parameters Combobox creation
        self.n_port             = tk.StringVar()
        self.n_baud             = tk.StringVar()
        
        #Comboboxes
        self.monthchoosen_port  = ttk.Combobox(self.labelframe_parameters, width = 20, textvariable = self.n_port)
        self.monthchoosen_baud  = ttk.Combobox(self.labelframe_parameters, width = 20, textvariable = self.n_baud)

        # labelframe_parameters Adding comboboxs drop down lists
        #TODO: list available ports and store it in a list
        self.monthchoosen_port['values'] = (' COM1', 
                                ' COM2',
                                ' COM3',
                                ' COM4',
                                ' COM5',
                                ' COM6',
                                ' COM7',
                                ' COM11')
        self.monthchoosen_baud['values'] = (' 600', 
                                ' 1200',
                                ' 2400',
                                ' 4800',
                                ' 9600',
                                ' 14400',
                                ' 19200',
                                ' 38400',
                                ' 56000',
                                ' 57600',
                                ' 115200')

        #Position
        self.monthchoosen_port.grid(column = 1, row = 0)
        self.monthchoosen_baud.grid(column = 1, row = 1)
        #TODO: Label have to change when connect is already clicked

        #Configuring the port
        # self.parameters_set_SerialPort()
        # self.serial = None

        self.btn_connect = ttk.Button(self.labelframe_parameters, text="Connect", command=self.parameters_portHandler)
        # self.btn_connect = ttk.Button(self.labelframe_parameters, text="Connect")
        self.btn_connect.grid(column=0, row=2,columnspan=2, padx=4, pady=4)


        # self.btn_connect.bind('<Button-1>',self.parameters_portHandler) #TODO: how to use this without run it straightway

    # def parameters_set_SerialPort(self) -> None:
    #     self.ser = serial.Serial()
    #             # port = None, #
    #             # baudrate=9600,
    #             # parity          = serial.PARITY_NONE,
    #             # stopbits        = serial.STOPBITS_ONE,
    #             # bytesize        = serial.EIGHTBITS)

    #     self.ser.timeout = 5
    #     # self.ser.close()
    #     #TODO: handle the raises
    #     #TODO:Implement loop or thread

    def parameters_portHandler(self) -> None:
        print('Inside Parameters\'s interactive method')
        try:
            # self.ser.set_port('COM11')
            self.ser.open()
            # self.ser.write("Port opened\r\n".encode())
            self.ser.read_serial(self.textReceived)
            self.sent_printMessage('Port opened\r\n')
            # self.btn_connect.config(text="Disconnect") #TODO: Change the text

        except Exception as e:
            print("<widgets><func: parameters_portHandler()>:error open serial port: " + str(e))
            
        if self.ser.isOpen():
            # self.ser.write("Port closed\r\n".encode())
            self.ser.close()
            self.sent_printMessage('Port closed\r\n')
     
    def sent(self):    
        self.labelframe_sent=ttk.LabelFrame(self.window, text="Sent:")
        self.labelframe_sent.grid(column = 1,row = 1, padx = 5, pady = 10, sticky="nw")
        
        self.textSent = tk.Text(self.labelframe_sent,height=10,width=50)
        self.textSent.grid(padx=4, pady=4)
        #TODO: Auto adjust when the number of line be bigger than the default height

    def sent_printMessage(self,message:'str') -> None:
        self.textSent.insert(tk.END,message)

    def mainMenu(self):
        #Commands
        self.label_commands=ttk.Label(self.labelframe_mainMenu, text=" Commands:")  
        self.label_commands.grid(column=0, row=0, padx=4, pady=4,sticky="nsw")
        # label_commands.pack(side=tk.LEFT)

        self.ent_commands1 = tk.Entry(self.labelframe_commands,width=7)
        self.ent_commands1.pack(side=tk.LEFT)
        # ent_commands1.grid(column=1, row=0, padx=4, pady=4,sticky="nw")
        self.ent_commands2 = tk.Entry(self.labelframe_commands,width=7)
        self.ent_commands2.pack(side=tk.LEFT)
        # ent_commands2.grid(column=2, row=0, padx=4, pady=4,sticky="nw")
        self.ent_commands3 = tk.Entry(self.labelframe_commands,width=7)
        self.ent_commands3.pack(side=tk.LEFT)

        #Period
        self.label_period=ttk.Label(self.labelframe_mainMenu, text=" Period:")  
        self.label_period.grid(column=0, row=1, padx=4, pady=4,sticky="nw")
        #combobox creation Perior
        self.n_period = tk.StringVar()
        self.monthchoosen_period       = ttk.Combobox(self.labelframe_mainMenu, width = 20, textvariable = self.n_period)
        self.monthchoosen_period['values'] = (' 5 seg', 
                                ' 10 seg',
                                ' 15 seg',
                                ' 30 seg',
                                ' 45 seg',
                                ' 60 seg')
        self.monthchoosen_period.grid(column = 1, row = 1)

        #Times
        self.label_times=ttk.Label(self.labelframe_mainMenu, text=" Times:")  
        self.label_times.grid(column=0, row=2, padx=4, pady=4,sticky="nw")
        #combobox creation Times
        self.n_times = tk.StringVar()
        self.monthchoosen_times       = ttk.Combobox(self.labelframe_mainMenu, width = 20, textvariable = self.n_times)
        self.monthchoosen_times['values'] = (' 1', 
                                ' 2',
                                ' 3',
                                ' 5',
                                ' 10',
                                ' 15')
        self.monthchoosen_times.grid(column = 1, row = 2)

        #Start Button
        # self.btn_start = ttk.Button(self.labelframe_mainMenu, text="Start", command=self.interactive(sentText))
        self.btn_start = ttk.Button(self.labelframe_mainMenu, text="Start")
        self.btn_start.grid(column=0, row=3,columnspan=2, padx=4, pady=4)

    def received(self):
        self.textReceived = tk.Text(self.labelframe_received,height=10,width=50)
        self.textReceived.grid(column=0, row=0, padx=4, pady=4, sticky="nw")

    # def received_printMessage(self,message:'str') -> None:
    #     self.textReceived.insert(tk.END,message)