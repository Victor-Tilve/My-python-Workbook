import tkinter as tk    # TODO: Borrar estos import despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk


class Sent:
    def __init__(self,window:'tk.Tk()') -> None:
        self.labelframe_sent=ttk.LabelFrame(window, text="Sent:")
        self.labelframe_sent.grid(column = 1,row = 1, padx = 5, pady = 10, sticky="nw")
        
        self.text = tk.Text(self.labelframe_sent,height=10,width=50)
        self.text.grid(padx=4, pady=4)
    
    def printMessage(self,message:'str') -> None:
        self.text.insert(tk.END,message)
