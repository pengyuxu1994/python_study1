import turtle


length=50
step=50
num=0
while num<10:
    print(num)
    num+=1

    turtle.penup()
    turtle.goto(length, length)
    turtle.pendown()
    turtle.goto(length, -1 * length)
    turtle.goto(-1 * length, -1 * length)
    turtle.goto(-1 * length, length)
    turtle.goto(length, length)
    length+=step

else:
    print("out",num)

turtle.done()