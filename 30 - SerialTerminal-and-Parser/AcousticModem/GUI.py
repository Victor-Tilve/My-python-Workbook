import tkinter as tk
from tkinter import ttk
from GUIParameters import Parameter
from GUIMainMenu import MainMenu
from GUIReceived import Received
from GUISent import Sent
from PIL import Image, ImageTk

#Tutorial: https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=67&codigo=67&inicio=60

# creating the main window
window = tk.Tk()
window.title('Acustic Modem')
# window.geometry('500x800') #TODO: Make this responsive

#Change the Icon
ico = Image.open("D:\\xx - Github\\My-python-Workbook\\30 - SerialTerminal-and-Parser\\pics\\router.png")
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

sent        = Sent(window)
mainMenu    = MainMenu(window,sent) #TODO: start just works when contect is active. Main Menu has a method to write in the port in the time setted.
parameter   = Parameter(window, sent) #TODO: Inlcude sent in the parameters
received    = Received(window)
#RTODO: take the information that came from the listener and print it



sent.text.insert(tk.END, "\nPut me on a new line!")


window.mainloop()
# Creating the frames