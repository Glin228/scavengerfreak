from tkinter import Tk, ttk, Text, END, WORD, filedialog
from threading import Thread
import time, sys

"""
dragons - increment current value by 1
did - increment current value 32
this - output a symbol
all - next cell
bad - previous cell
biowaste - decrease current value by 1
monsters - input 1 symbol
our_slaves <number> - move x commands forward or backward
"""

inpLetter = ""

def copyBetween(arg1, arg2, alltext):
    index1 = alltext.find(arg1, 1)
    index2 = alltext.find(arg2, -1)
    return alltext[index1:index2]

def inp():
    global inpLetter
    inpLetter = vvodilka.get()[0]

def run(program, _iter):
    t1 = time.perf_counter()
    global output, inpLetter
    field = {0:0}
    words = program.split()
    cur = 0
    out = ""
    i = 0
    print(words)
    while i < len(words):
        if "all" in words[i]:
            cur+=1
            field[cur] = 0 if not field.get(cur) else field[cur]
        if "bad" in words[i]:
            cur-=1
            field[cur] = 0 if not field.get(cur) else field[cur]
        if "dragons" in words[i]:
            field[cur] += 1
        if "biowaste" in words[i]:
            field[cur] -= 1
        if "did" in words[i]:
            field[cur] += 32
        if "this" in words[i]:
            out+=ALPHABET[field[cur]-32]
            output.config(text=out)
        if "monsters" in words[i]:
            while not inpLetter:
                pass
            field[cur] = ALPHABET.find(inpLetter)
            inpLetter = ""
        if "our_slaves" in words[i]:
            print(field[cur])
            i += int(words[i+1])
            continue
        i+=1
    global tmr
    tmr.config(text="Execution time: "+str(round(time.perf_counter() - t1, 4))+"sec")

def save():
    path = filedialog.asksaveasfilename(defaultextension="oasis")
    if not path:
        return
    with open(path, 'w') as f:
        f.write(programInput.get(1.0, END))
    

def load():
    global programInput
    filename = filedialog.askopenfilename(defaultextension="oasis")
    if not filename:
        return
    with open(filename, 'r') as f:
        data = f.read()
    programInput.delete(1.0, END)
    programInput.insert(1.0, data)
    

def runshit():
    output.config(foreground="#000000")
    global programInput
    t = Thread(target=run, args=(programInput.get(1.0, END).lower(), [1, 2]))
    t.start()

ALPHABET = " !"+"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

if __name__=="__main__":
    
    tk = Tk()
    tk.geometry("500x250")
    tk.title("skavengerf*ck")

    programInput = Text(height=10, width=25, wrap=WORD)
    programInput.grid(column=0, row=0, sticky="nw")

    runBtn = ttk.Button(text="Run!", command=runshit)
    runBtn.grid(column=1, row=0, sticky="nw")

    fileBtn = ttk.Button(text="Load", command=load)
    fileBtn.grid(column=2, row=0, sticky="nw")

    saveBtn = ttk.Button(text="Save", command=save)
    saveBtn.grid(column=3, row=0, sticky="nw")

    vvodilka = ttk.Entry()
    vvodilka.grid(column=1, columnspan=2, row=1, sticky='nw')

    vvodBtn = ttk.Button(text="Input", command=inp)
    vvodBtn.grid(column=3, row=1, sticky='nw')

    ttk.Label(text="Output:", font=("Helvetica", 15)).grid(column=0, row=1, sticky="nw")

    output = ttk.Label(font=("Arial", 10))
    output.grid(column=0, columnspan=2, row=2, sticky="nw")

    tmr = ttk.Label()
    tmr.grid(column=0, row=3, sticky="nw", columnspan=5)
    
    print(sys.argv)
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            data = f.read()
        programInput.delete(1.0, END)
        programInput.insert(1.0, data)
    
    tk.mainloop()
    import os
    os._exit(0)