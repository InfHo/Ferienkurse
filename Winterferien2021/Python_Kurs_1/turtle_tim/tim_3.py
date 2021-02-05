import turtle

turtle.bgcolor("black")

tim = turtle.Turtle()
tim.goto(-200,0)
tim.shape("turtle")
tim.color("darkviolet")

tim.width(3)

tim.speed(180)

zahl_1 = 10
zahl_winkel_1 = 40

#oder den farbloop in einem anderen loop ausführen
#und hier wird  "zahl" die durchzählt noch in den winkel bei tim.left() reingepackt
for zahl in range(20):
    for farbe in ("darkkhaki", "orchid", "cyan","tomato", "lawngreen"):
        tim.color(farbe)
        tim.forward(zahl_1)
        tim.left(zahl_winkel_1-(zahl*5))

#pu = pen up (stift hoch), damit geht es weiter ohne zu zeichnen
tim.pu()
tim.forward(300)
#pd = pen down (stift wieder runter) und dann zeichnet es weiter
tim.pd()

#hier noch der Befehl einen Kreis zu zeichnen mit Radius 40
#(wenn man schreibt tim.cicle(40,70) macht er noch einen 70 grad kreis mit radius 40
tim.circle(40)
#tim.circle(40,70)


#und hier kann man text schreiben, font ist die Schriftart, 100 die Grösse
tim.write("Hallo", font=("Forte",100))
