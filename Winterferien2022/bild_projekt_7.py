import turtle

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(0)

def quadrat(farbe, linienstaerke, laenge):
    fred.width(linienstaerke)
    fred.color(farbe)
    for i in range(4):
        fred.forward(laenge)
        fred.right(90)


def dreieck():
    for i in range(3):
        fred.forward(100)
        fred.right(120)

def vieleck():
    for i in range(6):
        fred.forward(100)
        fred.right(60)

for i in range(18):
    quadrat("blue", 1, 50)
    fred.right(20)

for i in range(12):
    quadrat("Aqua", 2, 150)
    fred.right(30)

for i in range(12):
    vieleck()
    fred.right(30)
    
fred.color("red")

for i in range(15):
    dreieck()
    fred.right(24)
