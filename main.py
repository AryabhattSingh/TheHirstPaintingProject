import random
import turtle
import extract_colors

# setting the color mode to RGB values
turtle.colormode(255)

# assigning the list of rgb colors to color_list
color_list = extract_colors.rgb_colors

# Making an instance of Turtle class
timmy = turtle.Turtle()
# Setting a shape for turtle
timmy.shape("turtle")

# Setting the pensize, it affects the thickness of a line drawn
timmy.pensize(20)
timmy.up()
# Setting the initial position to start drawing
timmy.setposition(-225, -250)


# creating an instance of Screen such that turtle work is visible and only closes on mouse click
screen = turtle.Screen()
screen.exitonclick()
