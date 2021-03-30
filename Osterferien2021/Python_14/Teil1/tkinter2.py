from tkinter import *
from tkinter import messagebox

fenster = Tk()

fenster.title("Hallo")

fenster.geometry('400x600')

def geklickt():
    print("geklickt!")
    messagebox.showwarning("TEST", "Alaaarm")
##    messagebox.showinfo(title="Test2","test234")


btn_1 = Button(fenster, text="Klick", command=geklickt).pack()
