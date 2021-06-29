import tkinter as tk
from tkinter import ttk
from widgets import Widgets


from PIL import Image, ImageTk

class App(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window

        self.initUI()

    def get_details(self):

        self.widgets.button.config(text='goodbye')

    #Init user interface
    def initUI(self):

        self.window.title('Acustic Modem')
        #Change the Icon
        ico = Image.open("D:\\xx - Github\\My-python-Workbook\\30 - SerialTerminal-and-Parser\\pics\\router.png")
        photo = ImageTk.PhotoImage(ico)
        self.window.wm_iconphoto(False, photo)

        self.window.rowconfigure([0, 1, 2], minsize=50, weight=1)
        self.window.columnconfigure([0, 1], minsize=50, weight=1)
        #TODO: Need to specify more about the window. Make it responsive

        #Frame for title
        fr_title = tk.Frame(self.window)
        ttk.Label(fr_title, text = "Módem Acústico AMT-915", 
                font = ("Times New Roman", 15)).pack(expand = True)
        fr_title.grid(column = 0,row = 0,columnspan = 2,padx = 5, pady = 5, sticky="nsew")
        


        #create Widgets
        
        # self.widgets = Widgets(self)
        # self.widgets.pack(side="top", anchor="center", fill="both", expand=True)

