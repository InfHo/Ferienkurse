import turtle

bob = turtle.Turtle()
bob.shape("turtle")

#ändert liniendicke
bob.width(7)

#ändert farbe
bob.color("mediumpurple") 

#Und loops kombinieren geht auch
for zahl in range(5):
    for farbe in ("mediumpurple","blue","red","yellow"):
        bob.color(farbe)
        bob.forward(50) #geht vorwärts
        bob.left(30)
