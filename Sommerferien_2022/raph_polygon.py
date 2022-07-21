import turtle

raph = turtle.Turtle()
turtle.bgcolor("black")

raph.shape("turtle")
raph.speed(8)
turtle.colormode(255)

def sechzehneck(laenge, farbe):
    raph.color(farbe)
    for i in range(16):
        raph.forward(laenge)
        raph.left(22.5)

def polygon(laenge, farbe, ecken):
    raph.color(farbe)
    for i in range(ecken):
        raph.forward(laenge)
        raph.left(360/ecken)


##polygon(50,"green", 4)
##polygon(50,"green", 16)
##polygon(,"green", 40)
raph.width(2)

for o in range(60):
    polygon(50,[72+o,20+5*o,186-5*o], 5)
    raph.right(15-2*o)
    raph.forward(20)
