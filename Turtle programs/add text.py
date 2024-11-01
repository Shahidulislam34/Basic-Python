import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphics")
screen.bgcolor("green")

# Create a turtle object
turtle.hideturtle()
turtle.penup()

turtle.goto(0, 0)
turtle.pendown()
turtle.width(3)
turtle.circle(100)
turtle.clear()

turtle.speed(100)
turtle.write("Hello, Turtle!", align = "center", font = ("arial", 40, "bold"))

turtle.penup()
turtle.goto(0, -40)
turtle.pendown()
turtle.write("Md. Shahidul Islam Shourov", align = "center", font = ("arial", 40, "bold"))



turtle.done()

