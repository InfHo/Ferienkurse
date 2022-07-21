import turtle

raph = turtle.Turtle()
raph.shape("turtle")
raph.speed(8)

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


for o in range(30):
    polygon(50,"DarkTurquoise", 5)
    raph.right(15)
    raph.forward(20)
