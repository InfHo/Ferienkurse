import turtle

bob = turtle.Turtle()

bob.width(7)


#zeichnet 1 Dreieck
bob.color("red")
for zahl in range(3):
    bob.forward(100) 
    bob.left(120)
