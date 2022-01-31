import turtle

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(5)

def abcdef(farbe, linienstaerke, laenge):
    fred.width(linienstaerke)
    fred.color(farbe)
    for i in range(4):
        fred.forward(laenge)
        fred.right(90)



abcdef("blue", 3, 50)

fred.right(20)

abcdef("red",7,200)

##for i in range(12):
##    abcdef("blue")
##    fred.right(30)

