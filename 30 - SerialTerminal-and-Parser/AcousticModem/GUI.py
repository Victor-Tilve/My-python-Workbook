import tkinter as tk
from tkinter import ttk
from GUIParameters import *
from GUIMainMenu import *
from GUIReceived import *
from GUISent import *
from PIL import Image, ImageTk

#Tutorial: https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=67&codigo=67&inicio=60

# creating the main window
window = tk.Tk()
window.title('Acustic Modem')
# window.geometry('500x800') #TODO: Make this responsive

#Change the Icon
# window.iconbitmap("C:\Users\vtilve\Desktop\VictorTilve\GitHub\My-python-Workbook\30 - SerialTerminal-and-Parser\pics\router.png")

ico = Image.open("..\\pics\\router.png")
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)


window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)
#TODO: Need to specify more about the window. Make it responsive

fr_title = tk.Frame(window)
fr_title.grid(column = 0,row = 0,columnspan = 2,padx = 5, pady = 5, sticky="nsew")
# label text for title
# ttk.Label(fr_title, text = "Módem Acústico AMT-915", 
#           font = ("Times New Roman", 15)).grid(column = 0,row = 0,columnspan = 2, sticky="nsew")

ttk.Label(fr_title, text = "Módem Acústico AMT-915", 
          font = ("Times New Roman", 15)).pack(expand = True)

parameter(window)
mainMenu(window)
received(window)
sent(window)

window.mainloop()
# Creating the frames