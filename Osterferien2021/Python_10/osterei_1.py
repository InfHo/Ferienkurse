import turtle
turtle.colormode(255)

tim = turtle.Turtle()
##for i in range(25):
##    turtle.color(255-i*10, 255-i*5, 5+i*9)
##    turtle.circle(1+i,180)

tim.speed(6)


def ellipse(schnitzel,remoulade):
        tim.color(remoulade)
        tim.left(45)
        for i in range(2):    
                tim.circle(schnitzel,90)
                tim.circle(schnitzel/2,90)
        tim.right(45)


for i in range(13):
    ellipse(20,"red")
    tim.pu()
    tim.forward(30)
    tim.right(55)
    tim.pd()

