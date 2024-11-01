#necessary module
import random
import turtle

#global section:
gru = []
stone = []
rem = []
location = []
n, m = (0, 0)
radius = 10

#user defined function
def take_stone() :
    stone.clear()
    stone.append(0)
    for i in range(1, n + 1) :
        rn = random.randint(2, mx)
        stone.append(rn)

def board_drawing() :
    a = int(-(n / 2) * 35)
    b = -200   
    location.append([(0, 0)])
    for i in range(1, n + 1) :
        one = [(0, 0)]
        for j in range(1, stone[i] + 1) :
            one.append((a, b + (j - 1) * 28))
        location.append(one)
        a = a + 35

    col = ["aliceblue","black","antiquewhite","aqua","aquamarine","azure","beige","bisque","black","blanchedalmond","blue","blueviolet"]
    col_len = len(col)
    turtle.screensize(canvwidth = 800, canvheight = 800, bg = 'green')
    turtle.width(3)
    turtle.color('white')
    turtle.left(90)
    turtle.speed(1000)
    ind = 0
    for i in range(1, n + 1) :
        ind = ind % col_len
        turtle.color(col[ind])
        turtle.width(10)
        x, y = location[i][1]
        turtle.up()
        turtle.setpos(x - 12, y - 18)
        turtle.down()
        turtle.right(90)
        turtle.forward(25)
        turtle.width(3)
        turtle.left(90)
        for j in range(1, stone[i] + 1) :
            x, y = location[i][j]
            turtle.up()
            turtle.setpos(x + radius, y)
            turtle.down()
            turtle.circle(radius)
        ind = ind + 1

def erase_stone(pl, st) :
    for i in range(1, st + 1) :
        x, y = location[pl][-1]
        turtle.up()
        turtle.setpos(x + radius, y)
        turtle.down()
        turtle.color("green")
        turtle.circle(radius)
        location[pl].pop()
        stone[pl] -= 1

def calculate_grundy() :
    gru.append(0)
    for i in range(1, mx + 1) :
        poss = []
        for x in rem :
            if x > i :
                break
            else :
                poss.append(gru[i - x])
        inc = 0
        while True:
            flag = 0
            for x in poss :
                if x == inc :
                    flag = 1
                    break
            if flag == 0 or len(poss) == 0:
                break
            else :
                inc = inc + 1
        gru.append(inc)
def impossible() :
    mn = rem[0]
    flag = 0
    for i in range(1, n + 1) :
        if stone[i] >= mn :
            flag = 1
            break
    if flag == 0 :
        return True
    else :
        return False

def computer_turn() :
    if impossible() == True :
        return False
    xr = [0]
    for i in range(1, n + 1) :
        tmp = xr[i - 1] ^ gru[stone[i]]
        xr.append(tmp)
    mn, pl, st = [100, 100, 100] #100 for any max value 
    for x in rem :
        for i in range(1, n + 1) :
            if stone[i] < x :
                continue
            else :
                tmp = xr[n] ^ gru[stone[i]] ^ gru[stone[i] - x]
                if tmp < mn :
                    mn = tmp
                    pl = i 
                    st = x 
    erase_stone(pl, st)
    return True

def user_turn() :
    if impossible() == True :
        return False
    while True :
        pl, st = list(map(int, screen.textinput("User","Pile Stone").split()))
        if stone[pl] >= st :
            break
    erase_stone(pl, st)
    return True

def game_start() :
    while True :
        if user_turn() == False :
            turtle.clear()
            turtle.color("black")
            turtle.up()
            turtle.setpos(0, 0)
            turtle.down()
            turtle.write("SORRY!! YOU HAVE LOST,TRY AGAIN", align = "center", font = ("arial", 30, "bold"))
            break
        if computer_turn() == False :
            turtle.clear()
            turtle.color("black")
            turtle.up()
            turtle.setpos(0, 0)
            turtle.down()
            turtle.write("CONGRATULATIONS!! YOU HAVE TRIUMPHED!", align = "center", font = ("arial", 30, "bold"))
            break


#main function():
screen = turtle.Screen()
turtle.hideturtle()
turtle.screensize(canvwidth = 800, canvheight = 800, bg = 'green')
n, mx = list(map(int, screen.textinput("n", "mx").split())) #number of piles and maximum number of stone


take_stone()

board_drawing()

rem = [2, 3]
calculate_grundy()

game_start()
turtle.done()
