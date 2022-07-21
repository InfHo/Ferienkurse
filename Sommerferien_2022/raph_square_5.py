import turtle

raph = turtle.Turtle()
raph.shape("turtle")

def quadrat(farbe, laenge):
    raph.color(farbe)
    for zahl in range(4):
        raph.forward(laenge)
        raph.left(90)

    
for i in range(5):    
    quadrat("red", 100)

