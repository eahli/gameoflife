# denna modul tar in en matris och visar den grafiskt

import numpy
import tkinter as tk

def greeting():
    window = tk.Tk()
    greeting = tk.Label(text="Conways Game of Life")
    greeting.pack()
    label = tk.Label(text="Hur stor skall spelplanen vara?")
    entry = tk.Entry()
    label.pack()
    entry.pack()
    psize = entry.get()
    window.mainloop()
    return psize




def show(pfield):
    psize = len(pfield)
    print(pfield)