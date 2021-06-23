import tkinter as tk    # TODO: Borrar estos import despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk


def parameter(window):
      
    labelframe_parameters=ttk.LabelFrame(window, text="Parameters:")
    labelframe_parameters.grid(column = 0,row = 2, padx = 5, pady = 10, sticky="nw")

    # label1=ttk.Label(labelframe_parameters, text=" Port:")
    # label1.grid(column=0, row=0, padx=4, pady=4, sticky="nw")  

    # label labelframe_parameters
    ttk.Label(labelframe_parameters, text = "Port :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 0, padx = 4, pady = 4, sticky="w")
    ttk.Label(labelframe_parameters, text = "Baud :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 1, padx = 4, pady = 4, sticky="w")
    ttk.Label(labelframe_parameters, text = "Data size :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 2, padx = 4, pady = 4, sticky="w")
    ttk.Label(labelframe_parameters, text = "Parity :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 3, padx = 4, pady = 4, sticky="w")
    ttk.Label(labelframe_parameters, text = "Handshake :",
            font = ("Times New Roman", 10)).grid(column = 0,
            row = 4, padx = 4, pady = 4, sticky="w")

    #  labelframe_parameters Combobox creation
    n_port = tk.StringVar()
    n_baud = tk.StringVar()
    n_dataZise = tk.StringVar()
    n_parity = tk.StringVar()
    n_handshake = tk.StringVar()
    
    monthchoosen_port       = ttk.Combobox(labelframe_parameters, width = 20, textvariable = n_port)
    monthchoosen_baud       = ttk.Combobox(labelframe_parameters, width = 20, textvariable = n_baud)
    monthchoosen_dataZise   = ttk.Combobox(labelframe_parameters, width = 20, textvariable = n_dataZise)
    monthchoosen_parity     = ttk.Combobox(labelframe_parameters, width = 20, textvariable = n_parity)
    monthchoosen_handshake  = ttk.Combobox(labelframe_parameters, width = 20, textvariable = n_handshake)
    
    # labelframe_parameters Adding comboboxs drop down lists
    monthchoosen_port['values'] = (' COM1', 
                            ' COM2',
                            ' COM3',
                            ' COM4',
                            ' COM5',
                            ' COM6',
                            ' COM7',
                            ' COM8')
    monthchoosen_baud['values'] = (' 600', 
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
    monthchoosen_dataZise['values'] = (' 7',' 8')
    monthchoosen_parity['values'] = (' OFF', 
                            ' RTS/CTS',
                            ' Xon/Xoff')
    monthchoosen_handshake['values'] = (' Free', 
                            ' PortStore test',
                            ' Data',
                            ' Setup')                                                                


    monthchoosen_port.grid(column = 1, row = 0)
    monthchoosen_baud.grid(column = 1, row = 1)
    monthchoosen_dataZise.grid(column = 1, row = 2)
    monthchoosen_parity.grid(column = 1, row = 3)
    monthchoosen_handshake.grid(column = 1, row = 4)
    # monthchoosen_baud.current()
    # monthchoosen_port.current()
    # monthchoosen_dataZise.current()
    # monthchoosen_parity.current()
    # monthchoosen_handshake.current()

    # labelframe_parameters.grid(row=0, column=0, sticky="ns")