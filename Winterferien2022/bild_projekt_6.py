import turtle

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(5)

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

vieleck()


dreieck()

quadrat("blue", 3, 50)

fred.right(20)

quadrat("red",7,200)

##for i in range(12):
##    abcdef("blue")
##    fred.right(30)

