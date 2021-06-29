import tkinter as tk    # TODO: Borrar estos import despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk

#TODO: delete this module
from tkinter import messagebox
from typing import Text

import serial
from GUISent import *

class Parameter:
        def __init__(self,window:'tk.Tk()',sentText:'Sent') -> None:
                self.state = True
                
                self.labelframe_parameters=ttk.LabelFrame(window, text="Parameters:")
                self.labelframe_parameters.grid(column = 0,row = 1, padx = 5, pady = 10, sticky="nw")

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

                self.monthchoosen_port.grid(column = 1, row = 0)
                self.monthchoosen_baud.grid(column = 1, row = 1)
                #TODO: Label have to change when connect is already clicked
                
                #Configuring the port
                self.set_port()

                self.btn_connect = ttk.Button(self.labelframe_parameters, text="Connect", command=self.portHandler(sentText))
                self.btn_connect.grid(column=0, row=2,columnspan=2, padx=4, pady=4)


                # self.btn_connect.bind('button-1',self.portHandler(sentText))

        def set_port(self) -> None:
                self.ser        = serial.Serial(
                        port='COM11',
                        baudrate=9600,
                        parity          = serial.PARITY_NONE,
                        stopbits        = serial.STOPBITS_ONE,
                        bytesize        = serial.EIGHTBITS)

                self.ser.timeout = 5
       
        def portHandler(self, sentText:'Sent') -> None:
                        print('Inside the portHandler')
                        if self.ser.close():
                                self.ser.open()
                                sentText.printMessage('\r\nPort opened')
                        elif self.ser.open():
                                self.ser.close()
                                sentText.printMessage('\r\nPort closed')
                        




                # if self.state:
                #         # port_value = self.monthchoosen_port.get()
                #         # baud_value = int(self.monthchoosen_baud.get())

                #         # self.btn_connect(text) #TODO: change the text when the button is click

                #         self.ser        = serial.Serial(
                #         port='COM11',
                #         baudrate=9600,
                #         parity          = serial.PARITY_NONE,
                #         stopbits        = serial.STOPBITS_ONE,
                #         bytesize        = serial.EIGHTBITS)

                #         self.ser.timeout = 5
                         

                #         # while True: #TODO: Como meto aquí el ciclo while para que
                #         #         buffer = ""
                #         #         print("send another massege\n")
                #         #         while True:
                #         #                 oneByte = self.ser.read(1)
                #         #                 if oneByte == b"\r":    #method should returns bytes
                #         #                         print (buffer)
                #         #                         self.ser.write("Received\r\n".encode())
                #         #                         break
                #         #                 else:
                #         #                         buffer += oneByte.decode()
                #         self.state = not self.state        
                # else: 
                #         self.ser.close() #TODO: check the port clousure
                #         self.state = not self.state

