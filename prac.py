import turtle

st = ""

def circle_drawing() :
    turtle.clear()
    turtle.width(3)
    turtle.circle(100)

def line_drawing() :
    turtle.clear()
    turtle.width(3)
    turtle.forward(200)
def add_character(char) :
    st += char

def user() :
    global st
    st = ""
    screen.listen()
    for i in range(32, 127) :
        ch = chr(i)
        screen.onkeypress(lambda c = ch : add_character(c), ch)

    screen.listen()
    for i in range(32, 127) :
        ch = chr(i)
        screen.onkeypress(lambda c = ch : add_character(c), ch)
    circle_drawing()
    #screen.onkeypress(enter_press, "Return")

def computer() :
    global st
    st = ""
    screen.listen()
    for i in range(32, 127) :
        ch = chr(i)
        screen.onkeypress(lambda c = ch : add_character(c), ch)

    screen.listen()
    for i in range(32, 127) :
        ch = chr(i)
        screen.onkeypress(lambda c = ch : add_character(c), ch)
    square_drawing()
    #screen.onkeypress(enter_press, "Return")
    

def game() :
    while True :
        user()
        computer()

screen = turtle.Screen()

game()

turtle.done()