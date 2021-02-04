import turtle #importiert das Turtle Modul zum Zeichnen

#hintergrundfarbe
turtle.bgcolor("blue")

#erstelle Turtle() zum Zeichnen nenne es "bob"
bob = turtle.Turtle()

#gibt der Turtle die Form eine Schildkröte
bob.shape("turtle")

#lässt bob um 100 Pixel vorwärts laufen
bob.forward(100)

#und hier macht es eine Drehung um 90 Grad nach rechts
bob.right(90)

#hier kann man die Dicke der Strichs einstellen
bob.width(7)

bob.forward(100)

#hier gibt es eine Linksdrehung
bob.left(39)

#Farbe ändern auf rot
#man kann im Internet auch nach "python turtle colors" suchen und die farben hier eingeben
bob.color("red")

bob.forward(100)

bob.right(270)

bob.forward(100)

bob.left(90)

bob.forward(200)

bob.left(90)
bob.forward(200)

