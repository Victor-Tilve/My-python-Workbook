import tkinter as tk    # TODO: Borrar estos import despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk


def received(window):
    labelframe_received=ttk.LabelFrame(window, text="Received:")
    labelframe_received.grid(column = 1,row = 2, padx = 5, pady = 10, sticky="nw")

    text = tk.Text(labelframe_received,height=10,width=50)
    text.grid(column=0, row=0, padx=4, pady=4, sticky="nw")
    
