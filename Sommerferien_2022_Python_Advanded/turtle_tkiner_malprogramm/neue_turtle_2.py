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
    canvas.bind_all("<KeyPress-a>",a_funktion)

    fenster.mainloop()

    
def w_funktion(event):
    print("w taste")
    schildi.forward(25)
    
def s_funktion(event):
    print("k taste")
    schildi.backward(25)

        
def a_funktion(event):
    print("k taste")
    schildi.left(90)
    schildi.forward(25)
    schildi.right(90)

    
main()

