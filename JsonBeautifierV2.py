from tkinter import *
from tkinter.scrolledtext import *
from tkinter import ttk
import subprocess
import json
import tkinter as tkr
import uuid

window = Tk()
window.configure(bg='grey')
window.title('Json Beautifier')
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(6, weight=1)

def clearAll():
    inp.delete(1.0, END)
    opt.delete(1.0,END)
    int_fields.delete(*int_fields.get_children())

def pasteFrom():
    inp.delete(1.0,END)
    clipboardData = subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
    inp.insert(INSERT,clipboardData)

def copyTo():
    copyToClipboardData = opt.get(1.0, END)
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(copyToClipboardData.encode('utf-8'))

def beautify():
    global result
    opt.delete(1.0, END)
    text = inp.get(1.0, END)
    parsed_json = json.loads(text)
    result = json.dumps(parsed_json, indent = 4,sort_keys=False)
    for i in result:
        if i in ['{','}']:
            opt.insert(END,i,"curly")
        elif i in ['[',']']:
            opt.insert(END,i,"square")
        else:   
            opt.insert(END,i,"general")
    populateInterstingFields(int_fields,'',json.loads(result))

def populateInterstingFields(tree,parent,dictionary):
    for key in dictionary:
        uid = uuid.uuid4()
        if isinstance(dictionary[key],dict):
            tree.insert(parent,'end',uid,text = key)
            populateInterstingFields(tree,uid,dictionary[key])
        elif isinstance(dictionary[key],list):
            tree.insert(parent,'end',uid,text=key+':[]')
            populateInterstingFields(tree,uid,dict([(i, x) for i, x in enumerate(dictionary[key])]))
        else:
            value = dictionary[key]
            if value is None:
                value = 'None'
            elif value is True:
                value = 'true'
            elif value is False:
                value = 'false'
            tree.insert(parent, 'end', uid, text=key, value=value)

inp_label = Label(window,text="Input",font=('Helvetica bold', 18), width=40,background='grey')
inp_label.grid(row=0,column=0,columnspan=5, sticky=W + N + S + E, pady=5, padx=5)

opt_label = Label(window,text="Output",font=('Helvetica bold', 18), width=40,background='grey')
opt_label.grid(row=0,column=6,columnspan=5, sticky=W + N + S + E, pady=5, padx=5)

inp = ScrolledText(window, font=('Helvetica', 14), width=100,relief="solid")
inp.grid(row=1, column=0, columnspan=5, sticky=W + N + S + E, pady=5, padx=5)

opt = ScrolledText(window, font=('Helvetica', 14), width=100)
opt.grid(row=1, column=6, columnspan=5, sticky=W + N + S + E, pady=5, padx=5)

int_label = Label(window,text="Interesting Fields",font=('Helvetica bold', 18), width=40,background='grey')
int_label.grid(row=2,column=6,columnspan=5, sticky=W + N + S + E, pady=5, padx=5)

fromBtn = ttk.Button(window,text="Paste From Clipboard",command=pasteFrom)
fromBtn.grid(row=3,column=0, sticky=W + N + S + E, pady=5, padx=5)

bty = ttk.Button(window,text="Beautify", command=beautify)
bty.grid(row=3,column=1, sticky=W + N + S + E, pady=5, padx=5)

toBtn = ttk.Button(window,text="Copy beautified JSON to Clipboard", command=copyTo)
toBtn.grid(row=3,column=2, sticky=W + N + S + E, pady=5, padx=5)

clearBtn = ttk.Button(window,text="Clear All Data",command=clearAll)
clearBtn.grid(row=3,column=3, sticky=W + N + S + E, pady=5, padx=5)

int_fields = ttk.Treeview(window)
int_fields.grid(row=3,column=6, sticky=W + N + S + E, pady=5, padx=5)
int_fields["columns"]=("one","two","three","four","five")

int_fields.heading("#0",text="Fields",anchor=tkr.W)
int_fields.column('#0',width=220,stretch=NO)
int_fields.column('one',width=220,stretch=NO)
int_fields.column('two',width=220,stretch=NO)
int_fields.column('three',width=220,stretch=NO)
int_fields.column('four',width=220,stretch=NO)
int_fields.column('five',width=220,stretch=NO)

opt.tag_config("curly",foreground="blue",font=('Helvetica',15,'bold'))
opt.tag_config("square",foreground="red",font=('bold'))
opt.tag_config("general",foreground="black")

dev_label = Label(window,text="Developed by Ankur Sharma (April 2019)",font=('Helvetica', 12), width=40,background='grey')
dev_label.grid(row=4,column=0, columnspan=10, sticky=W + N + S + E, pady=5, padx=5)

window.mainloop()
