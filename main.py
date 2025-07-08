import random
import turtle as t

import colorgram as cg

colors = cg.extract('pallete.jpg', 10)
rgb_colors = []
t.colormode(255)
tur = t.Turtle()
tur.speed("fastest")
tur.ht()
tur.penup()
tur.goto(-225, -225)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


def draw_lines(n_lines, y_pos):
    for _ in range(n_lines):
        y_pos += 50
        for _ in range(n_lines):
            tur.dot(20, random.choice(rgb_colors))
            tur.fd(50)
        tur.goto(-225, y_pos)


draw_lines(10, -225)
screen = t.Screen()
screen.exitonclick()
