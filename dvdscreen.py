import turtle
import time
t = turtle.Turtle()
xmin = (0.0)
xmax = (480.0)
ymax = (270.0)
ymin = (0.0)
for x in range(2):
    t.fd(480)
    t.lt(90)
    t.fd(270)
    t.lt(90)
t.pu()
t.setpos((xmax/2),(ymax/2))
t.pd()
beginTime = time.time()
t.lt(45)
t.fd(10)
while True:
    if t.xcor() <= xmax and t.xcor() >= xmin and t.ycor() <= ymax and t.ycor() >= ymin:
        t.fd(1)
    else:
        if t.xcor() >= xmax or t.xcor() <= xmin:
            print("hit x")
            if t.heading() == 45.0:
                t.lt(90)
                t.fd(2)
            elif t.heading() == 135.0:
                t.rt(90)
                t.fd(2)
            elif t.heading() == 225.0:
                t.lt(90)
                t.fd(2)
            elif t.heading() == 315.0:
                t.rt(90)
                t.fd(2)
            else:
                print("how bartosz how")
        elif t.ycor() >= ymax or t.ycor() <= ymin:
            print("hit y")
            if t.heading() == 45.0:
                t.rt(90)
                t.fd(2)
            elif t.heading() == 135.0:
                t.lt(90)
                t.fd(2)
            elif t.heading() == 225.0:
                t.rt(90)
                t.fd(2)
            elif t.heading() == 315.0:
                t.lt(90)
                t.fd(2)
            else:
                print("how bartosz how")
        else:
            endTime = time.time()
            totalTime = endTime - beginTime
            print("either you've broken something, or you hit the corner")
            print("Total time:",totalTime)
            varContinue = input("would you like to continue: ")
            t.rt(180)
            t.fd(2)


