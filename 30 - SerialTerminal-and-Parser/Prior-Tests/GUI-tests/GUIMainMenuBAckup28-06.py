import tkinter as tk    # TODO: Borrar estos import despues de terminar con este modulo, solo dejar los de el GUI principal
from tkinter import ttk


def mainMenu(window):
    labelframe_mainMenu=ttk.LabelFrame(window, text="Main Menu:")
    labelframe_mainMenu.grid(column = 0,row = 2, padx = 5, pady = 10,sticky="nw")
    labelframe_commands=ttk.Frame(labelframe_mainMenu)
    labelframe_commands.grid(column = 1,row = 0, padx = 8, pady = 5,sticky="w")
    '''
    I'm thinking about 3-4 commands maximun per epoch
    '''
    label_commands=ttk.Label(labelframe_mainMenu, text=" Commands:")  
    label_commands.grid(column=0, row=0, padx=4, pady=4,sticky="nsw")
    # label_commands.pack(side=tk.LEFT)

    ent_commands1 = tk.Entry(labelframe_commands,width=7)
    ent_commands1.pack(side=tk.LEFT)
    # ent_commands1.grid(column=1, row=0, padx=4, pady=4,sticky="nw")
    ent_commands2 = tk.Entry(labelframe_commands,width=7)
    ent_commands2.pack(side=tk.LEFT)
    # ent_commands2.grid(column=2, row=0, padx=4, pady=4,sticky="nw")
    ent_commands3 = tk.Entry(labelframe_commands,width=7)
    ent_commands3.pack(side=tk.LEFT)


    label_period=ttk.Label(labelframe_mainMenu, text=" Period:")  
    label_period.grid(column=0, row=1, padx=4, pady=4,sticky="nw")
    #combobox creation Perior
    n_period = tk.StringVar()
    monthchoosen_period       = ttk.Combobox(labelframe_mainMenu, width = 20, textvariable = n_period)
    monthchoosen_period['values'] = (' 5 seg', 
                            ' 10 seg',
                            ' 15 seg',
                            ' 30 seg',
                            ' 45 seg',
                            ' 60 seg')
    monthchoosen_period.grid(column = 1, row = 1)

    label_times=ttk.Label(labelframe_mainMenu, text=" Times:")  
    label_times.grid(column=0, row=2, padx=4, pady=4,sticky="nw")
    #combobox creation Times
    n_times = tk.StringVar()
    monthchoosen_times       = ttk.Combobox(labelframe_mainMenu, width = 20, textvariable = n_times)
    monthchoosen_times['values'] = (' 1', 
                            ' 2',
                            ' 3',
                            ' 5',
                            ' 10',
                            ' 15')
    monthchoosen_times.grid(column = 1, row = 2)




    btn_start = ttk.Button(labelframe_mainMenu, text="Start")
    btn_start.grid(column=0, row=3,columnspan=2, padx=4, pady=4)

    