import turtle

bob = turtle.Turtle()
bob.shape("turtle")

bob.width(7)

#ändert farbe
bob.color("mediumpurple") 

#man kann auch durch Farben loopen
for farbe in ("mediumpurple","blue","red","yellow"):
    bob.color(farbe)
    bob.forward(50) #geht vorwärts
    bob.left(30)
