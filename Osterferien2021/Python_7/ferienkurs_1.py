import turtle # importiert das turtle Zeichenmodul

# aender die Hintergrundfarbe
turtle.bgcolor("DarkTurquoise")

# erstelle Turtle und nenne sie schiri
schiri =turtle.Turtle()

# Groesse der Schildkroete veraendern
schiri.turtlesize(2)

# form der Schildkroete veraendern
schiri.shape("turtle")

# aendere Farbe
schiri.color("red")

# geschwindigkeit aendern
schiri.speed(1)

# bewege schildkroete vorwaerts um 100 Schritte
schiri.forward(100)

# verstecke schildkroete
schiri.hideturtle()

schiri.forward(150)

# mache schildkroete wieder sichtbar
schiri.showturtle()

# rechtsdrehung um 90 grad nach rechts
#(andere zahlen auch moeglich)
# schiri.left auch moeglich
schiri.right(90)

schiri.forward(150)

# aendere Liniendicke
schiri.width(5)

# aendere Farbe
schiri.color("yellow")

schiri.forward(150)

schiri.right(115)

# pu = Pen Up = Stift hoch
schiri.pu()
schiri.forward(150)

# pd = Pen Down = Stift wieder runter 
schiri.pd()

schiri.right(115)
schiri.forward(150)

# gehe zu bestimmter Stelle
schiri.goto(200,50)

