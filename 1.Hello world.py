import turtle
uu = ''
cc = ''
stone = [(-200, -200),(-100, -100), (0, 0), (100, 100),  (200, 200)]
stone2 = [(-200, -200),(-100, -100), (0, 0), (100, 100),  (200, 200)]
#stone = [{-200, -200},{-100, -100}, {0, 0}, {100, 100},  {200, 200}]
def draw_board() :
    global stone, stone2
    turtle.clear()
    stone = []
    stone = stone2.copy()
    turtle.color("black")
    uu = ''
    cc = ''
    for i in range(0, len(stone)) :
        x, y = stone[i]
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.circle(100)
    user()

def user_increase(character) :
    global uu 
    uu += character
    if len(uu) == 2 :
        erase()
        uu = ''
        computer()

def computer_increase(character) :
    global cc 
    cc += character
    if len(cc) == 2 :
        erase()
        cc = ''
        user()
    return


def erase() :
    x, y = stone[-1]
    stone.pop()
    turtle.color("green")
    turtle.up()
    turtle.setpos(x, y)
    turtle.down()
    turtle.circle(100)
    if len(stone) == 0 :
        turtle.color("black")
        draw_board()

def computer() :
    if len(stone) :
        draw_board
    screen.listen()
    for i in range(65, 91) :
        ch = chr(i)
        screen.onkeypress(lambda ch = ch : computer_increase(ch), ch)
    screen.onkeypress(draw_board, "Return")

def user() :
    if len(stone) :
        draw_board
    screen.listen()
    for i in range(65, 91) :
        ch = chr(i)
        screen.onkeypress(lambda ch = ch : user_increase(ch), ch)
    screen.onkeypress(draw_board, "Return")

screen = turtle.Screen()
turtle.screensize(canvwidth = 700, canvheight = 700, bg = "green")
turtle.hideturtle()
turtle.speed(500)
turtle.width(3)

draw_board()


turtle.done()