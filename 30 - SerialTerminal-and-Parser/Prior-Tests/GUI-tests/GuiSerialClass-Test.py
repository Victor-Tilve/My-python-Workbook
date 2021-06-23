import tkinter as tk
from tkinter import ttk

#Tutorial: https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=67&codigo=67&inicio=60

class Application:
    
    def __init__(self):
        # creating the main window
        self.window = tk.Tk()
        self.window.title('Acustic Modem')
        self.window.geometry('500x800') #TODO: Make this responsive
        self.window.rowconfigure([0, 1], minsize=50, weight=1)
        self.window.columnconfigure([0, 1], minsize=50, weight=1)
        #TODO: Need to specify more about the window. Make it responsive
        
        # Creating the LabelFrames
        stile = ttk.Style()
        stile.configure("Bold.TLabel", font = ("TkDefaultFont",9,"bold"))
        label = ttk.Label(text="Parameters:", style="Bold.TLabel")
        self.labelframe_parameters=ttk.LabelFrame(self.window, labelwidget=label)
        self.labelframe_mainMenu=ttk.LabelFrame(self.window, text="Parameters:")
        self.labelframe_sent=ttk.LabelFrame(self.window, text="Sent data")
        self.labelframe_received=ttk.LabelFrame(self.window, text="Received data")

        self.labelframe_parameters.grid(column = 0,row = 0, padx = 5, pady = 10)
        self.labelframe_mainMenu.grid(column = 0,row = 1, padx = 5, pady = 10)
        self.labelframe_sent.grid(column = 1,row = 0, padx = 5, pady = 10)
        self.labelframe_received.grid(column = 1,row = 1, padx = 5, pady = 10)
        self.window.mainloop()
        # Creating the frames

    
    def mainMenu(self):
        pass
    def parameter(self):
        pass
    def sentData(self):
        pass
    def receivedData(self):
        pass


application1 = Application()