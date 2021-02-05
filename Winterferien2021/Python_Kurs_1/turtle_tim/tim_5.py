import turtle

turtle.bgcolor("black")

tim = turtle.Turtle()
tim.goto(-200,0)
tim.shape("turtle")
tim.color("darkviolet")

tim.width(3)


#hier sind verschiedene vierecke, also mit verschiedenen längen
def viereck():
    tim.color("darkviolet")
    for j in range(4):
        tim.forward(50)
        tim.right(90)

def viereck_2():
    tim.color("light blue")
    for j in range(4):
        tim.forward(150)
        tim.right(90)

def viereck_3():
    tim.color("yellow")
    for j in range(4):
        tim.forward(250)
        tim.right(90)

viereck()
viereck_2()
viereck_3()
