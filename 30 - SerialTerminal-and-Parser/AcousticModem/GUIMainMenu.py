import tkinter as tk    # TODO: Borrar estos imcommand despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk

#TODO: delete this module
from tkinter import messagebox
from GUISent import *

import time

class MainMenu:
    def __init__(self,window:'tk.Tk()',sentText:'Sent') -> None:
        #     self.sentText = sentText
            self.labelframe_mainMenu=ttk.LabelFrame(window, text="Main Menu:")
            self.labelframe_mainMenu.grid(column = 0,row = 2, padx = 5, pady = 10,sticky="nw")
            self.labelframe_commands=ttk.Frame(self.labelframe_mainMenu)
            self.labelframe_commands.grid(column = 1,row = 0, padx = 8, pady = 5,sticky="w")
            '''
            I'm thinking about 3-4 commands maximun per epoch
            '''
            #Commands
            self.label_commands=ttk.Label(self.labelframe_mainMenu, text=" Commands:")  
            self.label_commands.grid(column=0, row=0, padx=4, pady=4,sticky="nsw")
            # label_commands.pack(side=tk.LEFT)

            self.ent_commands1 = tk.Entry(self.labelframe_commands,width=7)
            self.ent_commands1.pack(side=tk.LEFT)
            # ent_commands1.grid(column=1, row=0, padx=4, pady=4,sticky="nw")
            self.ent_commands2 = tk.Entry(self.labelframe_commands,width=7)
            self.ent_commands2.pack(side=tk.LEFT)
            # ent_commands2.grid(column=2, row=0, padx=4, pady=4,sticky="nw")
            self.ent_commands3 = tk.Entry(self.labelframe_commands,width=7)
            self.ent_commands3.pack(side=tk.LEFT)

            #Period
            self.label_period=ttk.Label(self.labelframe_mainMenu, text=" Period:")  
            self.label_period.grid(column=0, row=1, padx=4, pady=4,sticky="nw")
            #combobox creation Perior
            self.n_period = tk.StringVar()
            self.monthchoosen_period       = ttk.Combobox(self.labelframe_mainMenu, width = 20, textvariable = self.n_period)
            self.monthchoosen_period['values'] = (' 5 seg', 
                                    ' 10 seg',
                                    ' 15 seg',
                                    ' 30 seg',
                                    ' 45 seg',
                                    ' 60 seg')
            self.monthchoosen_period.grid(column = 1, row = 1)

            #Times
            self.label_times=ttk.Label(self.labelframe_mainMenu, text=" Times:")  
            self.label_times.grid(column=0, row=2, padx=4, pady=4,sticky="nw")
            #combobox creation Times
            self.n_times = tk.StringVar()
            self.monthchoosen_times       = ttk.Combobox(self.labelframe_mainMenu, width = 20, textvariable = self.n_times)
            self.monthchoosen_times['values'] = (' 1', 
                                    ' 2',
                                    ' 3',
                                    ' 5',
                                    ' 10',
                                    ' 15')
            self.monthchoosen_times.grid(column = 1, row = 2)

            #Start Button
            self.btn_start = ttk.Button(self.labelframe_mainMenu, text="Start", command=self.interactive(sentText))
            self.btn_start.grid(column=0, row=3,columnspan=2, padx=4, pady=4)

    def interactive(self,sentText:'Sent') -> None:
                print('Inside mainMenu\'s interactive method')
                command_value1 = self.ent_commands1.get()
                command_value2 = self.ent_commands2.get()
                command_value3 = self.ent_commands3.get()

                period_value = self.monthchoosen_period.get()
                times_value = self.monthchoosen_times.get()

                # for i in range(3): #TODO: Use times_value
                #         sentText.printMessage(command_value1)
                #         time.sleep(.100)
                        
                #         sentText.printMessage(command_value1)
                #         time.sleep(.100)
                        
                #         sentText.printMessage(command_value1)
                #         time.sleep(.100)
                        

                #         time.sleep(5) #TODO: Make the convertion of the time, use period_value






                # messagebox.showinfo("Xiith.com", "command1 selected " + command_value1 + 
                # "\ncommand2 selected " + command_value2 + 
                # "\ncommand2 selected " + command_value3 + 
                # "\ncommand2 selected " + period_value + 
                # "\ncommand2 selected " + times_value)
