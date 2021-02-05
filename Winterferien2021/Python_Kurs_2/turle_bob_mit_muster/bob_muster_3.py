import turtle

bob = turtle.Turtle()

bob.width(7)


#zeichnet 3 Dreiecke
bob.color("red")
for zahl in range(3):
    bob.forward(50) 
    bob.left(120)

bob.color("green")
for zahl in range(3):
    bob.forward(100) 
    bob.left(120)

bob.color("blue")
for zahl in range(3):
    bob.forward(150) 
    bob.left(120)
