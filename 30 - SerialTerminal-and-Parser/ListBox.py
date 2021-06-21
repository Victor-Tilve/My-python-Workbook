listbox_frame=Frame(root,borderwidth=5, relief=SUNKEN)
listbox_frame.pack(pady=10)
 
listbox=Listbox(listbox_frame)
listbox.pack()
 
listbox.insert(END,"one")
 
for item in ["two","three","four","five"]:
    listbox.insert(END, item)
 
def list_item_selected():
    selection=listbox.curselection()
    if selection:
        print(listbox.get(selection[0]))
        list_box_label.configure(text=listbox.get(selection[0]))

window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


list_box_button = Button(listbox_frame,text='list item button', command=list_item_selected)
list_box_button.pack()
window.mainloop()