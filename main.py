#####Turtle Intro######
import turtle
import turtle as t
from random import *

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)


# for _ in range(4):
#     tim.forward(100)
#     tim.right(450)

# for _ in range(25):
#     tim.forward(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()


def rand_color():
    # tim.pencolor(choice(COLORS))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


# def rand_angle():
#     rand_side = [90, 180, 270, 0]
#     tim.setheading(choice(rand_side))


#
# for i in range(3, 11):
#     for j in range(i):
#         rand_color()
#         tim.forward(100)
#         tim.right(360 / i)

tim.speed("fastest")


# tim.pensize(8)
# for i in range(200):
#     tim.color(rand_color())
#     tim.fd(30)
#     rand_angle()


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(rand_color())
        tim.circle(100)
        angle = tim.heading()
        tim.setheading(angle + size_of_gap)


draw_spirograph(10)

screen = turtle.Screen()
screen.exitonclick()
