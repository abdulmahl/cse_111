# import math module to use ceil function
import math

# Get input from user and convert the numbers to integer points
num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
 
# Compute the number of items and boxes using the formula
# using the number of items divided by items per box
num_boxes = math.ceil(num_items / items_per_box)

#  Print out the results for user to see
print(f"For {num_items} items, packing {items_per_box} items in a box, you'll need {num_boxes} boxes.  ")