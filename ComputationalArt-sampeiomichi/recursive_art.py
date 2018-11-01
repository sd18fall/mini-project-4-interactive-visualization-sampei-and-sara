"""
Mini Project 2: Computational Art
@author: Sampei Omichi
"""

from random import *
from math import *
from PIL import Image
import PIL.ImageOps


def build_random_function(min_depth, max_depth):
    """Build a random function.

    Builds a random function of depth at least min_depth and depth at most
    max_depth. (See the assignment write-up for the definition of depth
    in this context)

    Args:
        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function

    Returns:
        The randomly generated function represented as a nested list.
        (See the assignment writ-eup for details on the representation of
        these functions)
    """
    # TODO: implement this
    bas = ['x','y', 't']
    func = ['x','y','t','cos_pi','sin_pi','prod','avg']
    if max_depth == 1:
        return bas[randint(0,2)]
    else:
        block = func[randint(3,6)]
        if block == 'prod' or 'avg': # When Block needs two inputs
            return [block, build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
        elif not block == 'prod':
            return [block, build_random_function(min_depth-1, max_depth-1)]


def evaluate_random_function(f, x, y, t):
    """Evaluate the random function f with inputs x,y.

    The representation of the function f is defined in the assignment write-up.

    Args:
        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function

    Returns:
        The function value
    """
    # Complete
    if f[0] == 'x':
        return x
    elif f[0] == 'y':
        return y
    elif f[0] == 't':
        return t
    elif f[0] == 'avg':
        return (evaluate_random_function(f[1],x,y,t)+evaluate_random_function(f[2],x,y,t))/2
    elif f[0] == 'cos_pi':
        return cos(pi*evaluate_random_function(f[1],x,y,t))
    elif f[0] == 'sin_pi':
        return sin(pi*evaluate_random_function(f[1],x,y,t))
    elif f[0] == 'prod':
        return evaluate_random_function(f[1],x,y,t)*evaluate_random_function(f[2],x,y,t)

def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """Remap a value from one interval to another.

    Given an input value in the interval [input_interval_start,
    input_interval_end], return an output value scaled to fall within
    the output interval [output_interval_start, output_interval_end].

    Args:
        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values

    Returns:
        The value remapped from the input to the output interval

    Examples:
        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # Complete
    scale = (val - input_interval_start) / \
            (input_interval_end - input_interval_start)
    scale = abs(scale)
    output_val = (scale * (output_interval_end - output_interval_start)) \
                + output_interval_start
    return output_val

def color_map(val):
    """Maps input value between -1 and 1 to an integer 0-255, suitable for use as an RGB color code.

    Args:
        val: value to remap, must be a float in the interval [-1, 1]

    Returns:
        An integer in the interval [0,255]

    Examples:
        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # Complete
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)

def generate_functions():
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(4, 6)
    green_function = build_random_function(4, 6)
    blue_function = build_random_function(4, 6)
    return([red_function, green_function, blue_function])


def generate_art(filename, t, red_function, green_function, blue_function, x_size=1000, y_size=1000):
    """Generate computational art and save as an image file.

    Args:
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """

    # Create image and loop over all pixels

    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                color_map(evaluate_random_function(red_function, x, y, t)),
                color_map(evaluate_random_function(green_function, x, y, t)),
                color_map(evaluate_random_function(blue_function, x, y, t))
            )
    if filename[:6] == 'movie1':
        im.save(filename)
    if filename[:6] == 'movie2':
        inverted_im = PIL.ImageOps.invert(im)
        inverted_im.save(filename)
    if filename[:6] == 'movie3':
        grayscale_im = PIL.ImageOps.grayscale(im)
        grayscale_im.save(filename)

def generate_movie(frames):
    functions = generate_functions()
    red_function = functions[0]
    green_function = functions[1]
    blue_function = functions[2]

    for movie_num in range(4):
        for frame_number in range(1, frames):
            filename = 'movie'+ str(movie_num) +'_' + str(frame_number) + '.png'
            generate_art(filename, frame_number, red_function, green_function, blue_function)

if __name__ == '__main__':
    generate_movie(24)
