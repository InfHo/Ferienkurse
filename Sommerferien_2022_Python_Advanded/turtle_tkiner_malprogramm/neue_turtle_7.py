import turtle
from tkinter import *
import math

fenster = Tk()


fenster.title("Kreisprogramm")

canvas = Canvas(master=fenster, width=400, height=400)
canvas.pack()

schildi = turtle.RawTurtle(canvas)
schildi.speed(0)
schildi.left(90)
dicke = 1
global DIAGONAL
DIAGONAL = 0

def main():
    canvas.bind_all("<KeyPress-w>",w_funktion)
    canvas.bind_all("<KeyPress-s>",s_funktion)
    canvas.bind_all("<KeyPress-a>",a_funktion)
    canvas.bind_all("<KeyPress-d>",d_funktion)
    canvas.bind_all("<KeyPress-R>",reset)
    canvas.bind_all("<KeyPress-z>",undo)
    canvas.bind_all("<KeyPress-1>",funktionirgendwas)
    canvas.bind_all("<KeyPress-r>",rot)
    canvas.bind_all("<KeyPress-g>",grun)
    canvas.bind_all("<KeyPress-y>",gelb)
    canvas.bind_all("<KeyPress-b>",blau)
    canvas.bind_all("<Up>",hoch_funktion)
    canvas.bind_all("<Down>",runter_funktion)
    
    fenster.mainloop()

def w_funktion(event):
    if globals()["DIAGONAL"]%2 == 0:
        schildi.forward(25)
    else:
        schildi.forward(math.sqrt(2*25*25))

def s_funktion(event):
    if globals()["DIAGONAL"]%2 == 0:
        schildi.back(25)
    else:
        schildi.back(math.sqrt(2*25*25))

def a_funktion(event):
    schildi.left(45)
    globals()["DIAGONAL"] += 1

def d_funktion(event):
    schildi.right(45)
    globals()["DIAGONAL"] += 1

def reset(event):
    schildi.clear()
    
def undo(event):
    schildi.undo()

def hoch_funktion(event):
    global dicke
    dicke = dicke + 1
    schildi.width(dicke)

def runter_funktion(event):
    global dicke
    if dicke <= 1:
        dicke = 1
    else:
        dicke = dicke - 1
    schildi.width(dicke)


def funktionirgendwas(event):
    schildi.width(10)


def rot(event):
    schildi.color("red")
def blau(event):
    schildi.color("blue")
def grun(event):
    schildi.color("green")
def gelb(event):
    schildi.color("yellow")

main()
