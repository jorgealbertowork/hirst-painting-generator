import random
import turtle

import colorgram as cg

colors = cg.extract('palette.jpg', 10)
rgb_colors = []

for color in colors:
    # save extracted colors in the rgb_colors list
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


# sets the colormode for the turtle graphics library
turtle.colormode(255)

# basic settings for the turtle object
t = turtle.Turtle()
t.speed("fastest")
t.ht()
t.penup()
t.goto(-225, -225)


def draw_lines(n_lines, y_pos):
    for _ in range(n_lines):
        # this updates the vertical position of the turtle
        y_pos += 50

        for _ in range(n_lines):
            # this draws the line of dots
            t.dot(20, random.choice(rgb_colors))
            t.fd(50)

        # this updates the position for the drawing of a new line
        t.goto(-225, y_pos)


draw_lines(10, -225)

screen = turtle.Screen()
screen.exitonclick()
