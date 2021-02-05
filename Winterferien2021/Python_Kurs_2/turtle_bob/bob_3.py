import turtle

##turtle.bgcolor("blue")

bob = turtle.Turtle()
bob.shape("turtle")

bob.width(7)

bob.color("blue")

#das kann man auch abkürzen, mit einem "Loop" bzw "Schleife"
#statt "zahl" kann hier auch etwas anderes stehen
for zahl in range(4):
    bob.forward(50)
    bob.right(50)

