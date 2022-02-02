import turtle
import random

turtle.colormode(255)

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(5)

def quadrat(farbe, linienstaerke, laenge):
    fred.width(linienstaerke)
    fred.color(farbe)
    for i in range(4):
        fred.forward(laenge)
        fred.right(90)


def dreieck(farbe):
    fred.color(farbe)
    for i in range(3):
        fred.forward(100)
        fred.right(120)

def hexagon(farbe,linienstaerke):
    fred.width(linienstaerke)
    fred.color(farbe)
    for i in range(6):
        fred.forward(100)
        fred.right(60)


def form_1(farbe,linienstaerke):
    fred.width(linienstaerke)
    fred.color(farbe)
    fred.forward(100)
    fred.right(30)
    fred.forward(50)
    fred.circle(30)
    fred.forward(50)
    quadrat(farbe, linienstaerke, 50)
    fred.backward(100)
    fred.right(150)
    fred.forward(100)
    fred.right(180)

def turtle_input():
    x = input("welche funktion soll ausgeführt werden?")
    if x == "a":
        dreieck("red")
        
    if x == "b":
        dreieck("blue")

    if x == "c":
        hexagon("green", 3)
        
    fred.right(20)


for j in range(10):
    turtle_input()

