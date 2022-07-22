import turtle
from tkinter import *

fenster = Tk()

fenster.title("Kreisprogramm")

canvas = Canvas(master=fenster, width=400, height=400)
canvas.pack()

schildi = turtle.RawTurtle(canvas)


def main():
    canvas.bind_all("<KeyPress-w>",w_funktion)
    canvas.bind_all("<KeyPress-s>",s_funktion)
    canvas.bind_all("<KeyPress-d>",d_funktion)
    canvas.bind_all("<KeyPress-a>",a_funktion)

    fenster.mainloop()

    
def w_funktion(event):
    schildi.forward(25)
    
def s_funktion(event):
    schildi.backward(25)
    
def d_funktion(event):
    schildi.right(45)
    
def a_funktion(event):
    schildi.left(45)
main()





    
    
