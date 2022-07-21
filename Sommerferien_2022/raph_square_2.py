import turtle

raph = turtle.Turtle()
raph.shape("turtle")

def quadrat():
    raph.color("green")
    raph.forward(200)
    raph.left(90)
    raph.forward(200)
    raph.left(90)
    raph.forward(200)
    raph.left(90)
    raph.forward(200)
    raph.left(90)

def achteck():
    
    
    
quadrat()

raph.goto(90,90)

quadrat()


raph.goto(-200,-200)

quadrat()
