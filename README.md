# The Hirst Painting Project

## Introduction

This Python program creates a digital version of the iconic "Spot Paintings" made famous by contemporary artist Damien Hirst. The Spot Paintings are a series of artworks consisting of rows and columns of colored dots on a canvas. With this program, you can generate your own spot paintings using Python's Turtle graphics library. 

## Modules Used

This program relies on three modules:

1. **random**: This is a built-in Python module used for generating random values. It's used here to pick a random tuple containing RGB values, from a list of multiple such tuples.

2. **turtle**: Another built-in Python module, Turtle, is employed to create the graphical user interface for drawing the spot painting.

3. **colorgram**: This module is not built-in and needs to be installed separately. It's used to extract RGB values representing different colors from an image.

## Project Structure

The project is organized as follows:

- **main.py**: This is the main Python script responsible for creating the spot painting. It utilizes the Turtle graphics library and the color information extracted from the image.

- **extract_colors.py**: This script imports the colorgram module and uses it to extract different RGB values representing various colors from an image. These color values are then used in the main.py script to create the spot painting.

- **hirst-painting.jpg**: This is an image file containing the reference colors used in Damien Hirst's spot paintings.

## How It Works

1. In **extract_colors.py**, the colorgram module is imported. The `extract(image-name, noOfColors)` function of the colorgram module is used to extract different RGB values representing different colors from the provided image. Each RGB value is stored as a tuple, and these tuples are added to a list called `rgb_colors`.

2. In **main.py**, we set the colormode to RGB by invoking `turtle.colormode(255)`. The `rgb_colors` list extracted in the previous step is assigned to a new list called `color_list`.

3. We create an object of the Turtle class from the Turtle module. This turtle object is used to draw on the graphical user interface.

4. The initial position of the turtle is set, and two essential functions are defined:
   - `draw_a_spot()`: This function is responsible for drawing a single spot on the screen with a color from the `color_list`.
   - `shift_turtle_to_next_line()`: This function moves the turtle to the next line in an upward direction.

5. Using the `draw_a_spot()` and `shift_turtle_to_next_line()` functions within a nested for loop, the program generates a spot painting that resembles Damien Hirst's iconic artwork.

## Getting Started

1. Ensure you have Python installed on your system.

2. Install the `colorgram` module by running the following command:
   ```shell
   pip install colorgram.py
   ```

3. Place the image file you want to use as a color reference (e.g., `hirst-painting.jpg`) in the project folder.

4. Run the `main.py` script to generate your own spot painting.

Enjoy creating your unique spot paintings inspired by Damien Hirst's famous artwork!
