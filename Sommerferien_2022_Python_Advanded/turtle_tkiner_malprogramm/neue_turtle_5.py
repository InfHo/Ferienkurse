import turtle
from tkinter import *
import math

fenster = Tk()


fenster.title("Kreisprogramm")

canvas = Canvas(master=fenster, width=400, height=400)
canvas.pack()

turt = turtle.RawTurtle(canvas)
turt.speed(0)
turt.left(90)

global DIAGONAL
DIAGONAL = 0

def main():
    canvas.bind_all("<KeyPress-w>",w_funktion)
    canvas.bind_all("<KeyPress-s>",s_funktion)
    canvas.bind_all("<KeyPress-a>",a_funktion)
    canvas.bind_all("<KeyPress-d>",d_funktion)
    canvas.bind_all("<KeyPress-r>",reset)
    canvas.bind_all("<KeyPress-z>",undo)
    
    fenster.mainloop()

def w_funktion(event):
    if globals()["DIAGONAL"]%2 == 0:
        turt.forward(25)
    else:
        turt.forward(math.sqrt(2*25*25))

def s_funktion(event):
    if globals()["DIAGONAL"]%2 == 0:
        turt.back(25)
    else:
        turt.back(math.sqrt(2*25*25))

def a_funktion(event):
    turt.left(45)
    globals()["DIAGONAL"] += 1

def d_funktion(event):
    turt.right(45)
    globals()["DIAGONAL"] += 1

def reset(event):
    turt.clear()
    
def undo(event):
    turt.undo()

main()
