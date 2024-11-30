from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()
label = ttk.Label(frm, text="Hello World!\n").grid(column=0, row=0)
btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
# fred = ttk.Button(frm, fg="red", bg="blue")
print(btn)
root.mainloop()