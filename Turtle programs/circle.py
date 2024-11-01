import turtle
turtle.screensize(canvwidth = 700, canvheight = 700, bg = 'green')
turtle.left(90)
turtle.width(3)
turtle.speed(1)
turtle.color('white')

points = [{0, 0}]
n = int(input("Enter the number of stones: "))
rad = int(input("Enter the radius of each circle: "))
print("Enter the circles center:")
for i in range(1, n + 1) :
    pos = list(map(int, input().split()))
    points.append(pos)


for i in range (1, n + 1) :
    turtle.up()
    turtle.setpos(points[i][0] + rad, points[i][1])
    turtle.down()
    
    turtle.circle(rad)








turtle.done()