import turtle

screen = turtle.Screen()
while True :
    a, b = list(map(int,screen.textinput("File:", "Input:").split()))
    turtle.circle(a)
    turtle.circle(b)

turtle.done()