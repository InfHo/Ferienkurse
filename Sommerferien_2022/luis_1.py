import turtle

raph = turtle.Turtle()
raph.shape("turtle")

def turtle_controller(tun, wert) :
    tun = tun.upper()
    if tun == "V":
        raph.forward(wert)
    elif tun == "Z":
        raph.backward(wert)
    elif tun == "R":
        raph.right(wert)
    elif tun == "L":
        raph.left(wert)
    elif tun == "A":
        raph.penup()
    elif tun == "E":
        raph.pendown()
    elif tun == "N":
        raph.reset()
    else:
        print("Unbekannter Befehl")

def vorwaerts():
    raph.forward(100)
def rueckwaerts():
    raph.backward(100)

# turtle_controller("v", 100)

##a = input("Gib einen Buchstaben ein:" )

##turtle_controller(a, 100)
turtle.listen()

turtle.onkey(vorwaerts, "v")
turtle.onkey(rueckwaerts, "r")
turtle.mainloop()
