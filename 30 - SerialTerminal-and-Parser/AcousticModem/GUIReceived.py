import tkinter as tk    # TODO: Borrar estos import despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk

class Received:
    def __init__(self,window) -> None:
        self.labelframe_received=ttk.LabelFrame(window, text="Received:")
        self.labelframe_received.grid(column = 1,row = 2, padx = 5, pady = 10, sticky="nw")

        self.text = tk.Text(self.labelframe_received,height=10,width=50)
        self.text.grid(column=0, row=0, padx=4, pady=4, sticky="nw")

