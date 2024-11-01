import turtle

def circle_drawing() :
    turtle.circle(100)

def line_drawing() :
    turtle.forward(100)

turtle.hideturtle()
screen = turtle.Screen()
turtle.screensize(canvwidth = 500, canvheight = 500, bg = "blue")
turtle.speed(20)
turtle.width(3)

screen.listen()
screen.onkeypress(circle_drawing, "1")
screen.onkeypress(line_drawing, "2")
#val = screen.textinput("a", "b")
#turtle.write(val, aligh = "celter", fond = ("arial", 50, "bold"))
turtle.done()