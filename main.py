import random
import turtle

import colorgram as cg

colors = cg.extract('palette.jpg', 10)
RGB_COLORS = []

for color in colors:
    # save extracted colors in the RGB_COLORS list
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    RGB_COLORS.append(new_color)


# sets the colormode for the turtle graphics library
turtle.colormode(255)

# basic settings for the turtle object
T = turtle.Turtle()
T.speed("fastest")
T.ht()
T.penup()
T.goto(-225, -225)


def draw_lines(n_lines, y_pos):
    for _ in range(n_lines):
        y_pos += 50  # this updates the vertical position of the turtle

        for _ in range(n_lines):  # this draws the line of dots
            T.dot(20, random.choice(RGB_COLORS))
            T.fd(50)

        # this updates the position for the drawing of a new line
        T.goto(-225, y_pos)


draw_lines(10, -225)

SCREEN = turtle.Screen()
SCREEN.exitonclick()
