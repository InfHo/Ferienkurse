import turtle

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(0)

def abcdef(farbe):
    fred.color(farbe)
    for i in range(4):
        fred.forward(100)
        fred.right(90)

for i in range(18):
    abcdef("blue")

    fred.right(20)
