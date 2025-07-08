import random
import turtle

import colorgram as cg

colors = cg.extract('pallete.jpg', 10)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


turtle.colormode(255)

t = turtle.Turtle()
t.speed("fastest")
t.ht()
t.penup()
t.goto(-225, -225)


def draw_lines(n_lines, y_pos):
    for _ in range(n_lines):
        y_pos += 50
        for _ in range(n_lines):
            t.dot(20, random.choice(rgb_colors))
            t.fd(50)
        t.goto(-225, y_pos)


draw_lines(10, -225)

screen = turtle.Screen()
screen.exitonclick()
