import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(250)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
#
#
#
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
# import turtle as t

# tim = t.Turtle()

# import heroes
# print(heroes.gen())
#
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
#
# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colours) #need to add a list with colours
#     draw_shape(shape_side_n)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    the_tuple = (r, g, b)
    return the_tuple


directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(100):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
