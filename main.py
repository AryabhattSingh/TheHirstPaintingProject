import random
import turtle
import extract_colors


def draw_a_spot(turtle_obj, thickness, spacing):
    """This function draws a spot and moves forward. It takes 3 parameters - a turtle object, thickness of spot
    and spacing between spots"""
    turtle_obj.up()
    turtle_obj.dot(thickness, random.choice(color_list))
    turtle_obj.forward(spacing)


def shift_turtle_to_next_line(turtle_obj, row_number, spacing):
    """This function shifts the turtle to the next line. It takes 3 arguments - turtle object, row number and
    spacing between spots"""
    turtle_obj.up()
    for _ in range(0, 2):
        turtle_obj.left(90) if row_number % 2 == 0 else turtle_obj.right(90)
        turtle_obj.forward(spacing)


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

# drawing a 10 X 10 grid with random colors
for i in range(0, 10):
    for j in range(0, 10):
        draw_a_spot(timmy, 20, 50)
    shift_turtle_to_next_line(timmy, i, 50)

# creating an instance of Screen such that turtle work is visible and only closes on mouse click
screen = turtle.Screen()
screen.exitonclick()
