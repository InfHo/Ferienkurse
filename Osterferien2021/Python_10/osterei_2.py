import turtle
turtle.colormode(255)

tim = turtle.Turtle()


tim.speed(200)


def ellipse(schnitzel,remoulade):
        tim.begin_fill()
        tim.color(remoulade)
        tim.left(45)
        for i in range(2):    
                tim.circle(schnitzel,90)
                tim.circle(schnitzel/2,90)
        tim.end_fill()
        tim.right(45)
        


for i in range(100):
    
    x = 255-((i*10)%255), 255-((i*5)%255), 5+((i*9)%250)
    ellipse(i,x)
    tim.pu()
    tim.forward(30+i*3.5)
    tim.right(45)
    tim.pd()
    print(i)

