import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Acustic Modem')
window.geometry('500x250') #TODO: Make this responsive


window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

# Frame for 0,0
fr_00 = tk.Frame(window, relief=tk.RAISED)
# Frame for 0,1
fr_01 = tk.Frame(window, relief=tk.RAISED)
# Frame for 1,0
fr_10 = tk.Frame(window, relief=tk.RAISED)
# Frame for 1,1
fr_11 = tk.Frame(window, relief=tk.RAISED)



# label fr_00
ttk.Label(fr_00, text = "Port :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 0, padx = 10, pady = 25)
ttk.Label(fr_00, text = "Baud :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 1, padx = 10, pady = 25)
ttk.Label(fr_00, text = "Data size :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 2, padx = 10, pady = 25)
ttk.Label(fr_00, text = "Parity :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 3, padx = 10, pady = 25)
ttk.Label(fr_00, text = "Handshake :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 4, padx = 10, pady = 25)

#  fr_00 Combobox creation
n = tk.StringVar()
monthchoosen_port       = ttk.Combobox(fr_00, width = 20, textvariable = n)
monthchoosen_baud       = ttk.Combobox(fr_00, width = 20, textvariable = n)
monthchoosen_dataZise   = ttk.Combobox(fr_00, width = 20, textvariable = n)
monthchoosen_parity     = ttk.Combobox(fr_00, width = 20, textvariable = n)
monthchoosen_handshake  = ttk.Combobox(fr_00, width = 20, textvariable = n)
  
# fr_ 00 Adding comboboxs drop down lists
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

fr_00.grid(row=0, column=0, sticky="ns")
window.mainloop()
