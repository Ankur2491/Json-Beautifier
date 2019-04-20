from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
import json
def clicked():
    opt.delete(1.0, END)
    text = inp.get(1.0, END)
    parsed_json = json.loads(text)
    result = json.dumps(parsed_json, indent = 2,sort_keys=False)
    opt.insert(INSERT,result)
def clearInput():
    inp.delete(1.0, END)
def clearOutput():
    opt.delete(1.0, END)
window = Tk()
window.title("Json Beautifier")
window.geometry('1524x800')
frame1 = tk.Frame(
master = window,
bg='#000000'
)
frame1.pack(fill='both',expand='yes')
inp = scrolledtext.ScrolledText(
master=frame1,
wrap=tk.WORD,
width=80,
height=20
)
btn = ttk.Button(window, text="Beautify", command=clicked)
btn.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
btn2 = ttk.Button(window, text="Clear Input", command=clearInput)
btn2.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
btn3 = ttk.Button(window, text="Clear Output", command=clearOutput)
btn3.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
lbl = Label(window, text="Developed by Ankur Sharma (April 2019)")
lbl.pack()
opt = scrolledtext.ScrolledText(
master=frame1,
wrap=tk.WORD,
width=80,
height=20
)
inp.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
opt.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
window.mainloop()
