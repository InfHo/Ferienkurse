import turtle

raph = turtle.Turtle()
raph.shape("turtle")

def quadrat(farbe, laenge):
    raph.color(farbe)
    for zahl in range(4):
        raph.forward(laenge)
        raph.left(90)


    
    
    
quadrat("red", 100)

raph.goto(90,90)

quadrat("green", 50)


raph.goto(-200,-200)

quadrat("blue",200)
