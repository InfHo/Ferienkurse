import turtle
import random

turtle.colormode(255)

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(9)

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


for i in range(36):
    r = i*7
    g = 0
    b = 255-(i*7)
    print("r:", r)
    print("g:", g)
    print("b:", b)
    print(" ")
    quadrat([r,g,b],2, 100)
    fred.right(10)






