import turtle

#hintergrundfarbe
turtle.bgcolor("black")

bob = turtle.Turtle()
bob.shape("turtle")

#ändert liniendicke
bob.width(7)

#ändert farbe
bob.color("mediumpurple") 

#hier nochmal der Loop / Schleife
#statt "zahl" kann hier auch etwas anderes stehen
for zahl in range(4):
    bob.forward(50)
    bob.right(50)

#kurzer Einschub zum Farbe ändern und ein Stück weiterlaufen
bob.color("green")
bob.forward(200)


#Farbe ändern und noch ein Loop, diesmal mit andern Zahlen
#'dingsda' 
bob.color("red")
for dingsda in range(6):
    bob.forward(90)
    bob.left(70)

