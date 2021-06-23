import tkinter as tk    # TODO: Borrar estos import despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk


def sent(window):
    labelframe_sent=ttk.LabelFrame(window, text="Sent:")
    labelframe_sent.grid(column = 1,row = 1, padx = 5, pady = 10, sticky="nw")
    
    text = tk.Text(labelframe_sent,height=10,width=50)
    text.grid(padx=4, pady=4)
