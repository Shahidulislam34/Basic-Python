import turtle
screen = turtle.Screen()
turtle.screensize(canvwidth = 700, canvheight = 700, bg = 'blue')
turtle.width(3)
turtle.color('red')
turtle.speed(5)

ln = int(screen.textinput("User Move", "Lenth of square:"))

for i in range(1, 4 + 1) :
    turtle.left(90)
    turtle.forward(ln)



turtle.done()