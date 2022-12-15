# Import the functions from the Draw 2-D library
# so that they can be used in this program.

import random

from draw2d import (draw_arc, draw_line, draw_oval, draw_polygon,
                    draw_rectangle, draw_text, finish_drawing, start_drawing)


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_ground(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_grass(canvas, scene_width, scene_height, 3)
    draw_grass(canvas,scene_width, scene_height, 1)
    draw_grass(canvas,scene_width, scene_height, 2)
    draw_grass(canvas,scene_width, scene_height, 3)
    draw_pine_tree(canvas, 503, 100,217)
    draw_pine_tree(canvas, 400, 100, 255)
    draw_pine_tree(canvas, 700, 100, 310)
    draw_pine_tree(canvas, 25, 75, 175)
    draw_pine_tree(canvas, 156, 90, 237)
    draw_pine_tree(canvas, 289, 55, 310)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, 
        scene_width, scene_height, width=0, fill="sky blue")
    draw_oval(canvas, 223, 233, 444, 333,outline="white", fill="white")
    draw_oval(canvas, 222, 266, 477, 399,outline="white", fill="white")
    draw_oval(canvas, 77, 312, 144, 409, outline="white", fill="white")
    draw_oval(canvas, 88, 323, 176, 354, outline="white", fill="white")
    draw_oval(canvas, 50, 354, 90, 389, outline="white", fill="white")
    draw_oval(canvas, 377, 259, 677, 400, outline="white", fill="white")
    draw_oval(canvas, 550, 300, 850, 600, outline="black", fill="yellow")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, 
        scene_height / 3, width=0, fill="green")

def draw_grass(canvas, width, height, interval):
    for x in range(interval, height, interval):
        y1 = random.randint(interval,width)
        draw_line(canvas, y1, 5, y1, 175, fill="green")

def draw_pine_tree(canvas, center_x, bottom, height):
    # Draw tree trunk.
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    trunk_bottom = bottom
    right_trunk = center_x + trunk_width / 2
    top_trunk = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, trunk_bottom, right_trunk, top_trunk,outline="black", fill="tan2")

    # Draw skirt of the tree.
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    peak_x = center_x
    skirt_bottom = top_trunk
    peak_y = bottom + height 
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom,outline="black", fill="dark green" )

# Call the main function so that
# this program will start executing.
main()