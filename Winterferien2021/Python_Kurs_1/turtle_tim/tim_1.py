import turtle #importiert das Turtle Modul zum Zeichnen

#hintergrundfarbe
turtle.bgcolor("black")


#erstelle Turtle() zum Zeichnen nenne es "tim"
tim = turtle.Turtle()

#gibt der Turtle die Form eine Schildkröte
tim.shape("turtle")

#Farbe ändern auf rot
#man kann im Internet auch nach "python turtle colors" suchen und die farben hier eingeben
tim.color("darkviolet")

#hier kann man die Dicke der Strichs einstellen
tim.width(9)

#gehe um 100 pixel vorwärts, drehe dich um 90 grad nach rechts und nochmam 100 pixel vorwärts
tim.forward(100)
tim.right(90)
tim.forward(100)

#man kann die strecken, winkel etc auch als variable bennen und später in tim.forward() einfügen
#hier "zahl_1" und "zahl_winkel_1" (die namen kann man frei wählen).
zahl_1 = 50
zahl_winkel_1 = 40

#anstatt mehrmals etwas auszuführen kann man es auch in einen Loop packen
#hier wiederholt es sich dann 3x 
for i in range(3):
    tim.forward(zahl_1)
    tim.left(zahl_winkel_1)


