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


for i in range(36):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    hexagon([r,g,b],2)
    fred.right(10)






