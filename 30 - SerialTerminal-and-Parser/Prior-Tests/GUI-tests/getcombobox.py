from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


class Test:
    def __init__(self, tk):
        self.var = StringVar()
        self.data = ("one", "two", "three", "four")
        self.cb = Combobox(tk, values=self.data)
        self.cb.place(x=60, y=150)
        self.b1 = Button(tk, text="Check", command=self.select).place(x=60, y=300)

    def select(self):
        value = self.cb.get()
        messagebox.showinfo("Xiith.com", "You selected " + value)


tk = Tk()
tk.geometry("600x500")
tk.title("Xiith.com")
tt = Test(tk)
tk.mainloop()