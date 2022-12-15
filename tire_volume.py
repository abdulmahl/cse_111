'''
Many companies wish to understand the needs and wants of their customers more deeply 
so the company can create products that fill those needs and wants. 
One way to understand customers more deeply is to record the values entered by 
customers while they are using a program and then to analyze those values. 
One common way to record values is for a program to store them in a file.
'''

# import the math module to use pi in this program.
from cmath import pi

# Import datetime module to use in this program.
from datetime import datetime

# Get input from user and convert the numbers to floating points
w = int(input("Enter the width of the tire in mm (ex. 205): "))
a = int(input("Enter the aspect ratio of the tire (ex. 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex. 15): "))

# Compute the voliume in liters using the formula provided. 
volume = pi * w**2 * a * (2540 * d + w * a) / 10000000000

# Prints out the current date and or time.
current_date_and_time = datetime.now()

print()
# Prints out the volume results for the user to see. 
print(f"The approximate volume is {volume:.2f} liters")

# Add a set of if … elif … else statements in your program 
# that use the tire width,
#  tire aspect ratio, and wheel diameter that the user enters 
# to find a price and then print the price.
if w == 185 and a == 65 and d == 14:
    price = 109.99
    print(f'''The price for the tires with the dementions you entered is 
${price}''')
elif w == 195 and a == 60 and d == 15:
    price = 151.99
    print(f'''The price for the tires with the dementions you entered is 
${price}''')
elif w == 205 and a == 60 and d == 15:
    price = 156.99
    print(f'''The price for the tires with the dementions you entered is 
${price}''')
else: 
    if w == 215 and a == 55 and d == 17:
        price = 178.99 
        print(f'''The price for the tires with the dementions you entered is 
${price}''')

# program should ask the user if she wants to buy tires 
# with the dimensions that she entered. If the user answers "yes", 
# your program should ask for her phone number and store her phone number in 
# the volumes.txt file.
user_choice = input('''Would you like to buy the tires 
with the dimentions that you entered? ''').lower()
if user_choice == "yes".lower():
    phone_number = input("Please enter your phone number: ")
    print('''Thank you, our sales consultant will be 
in contact with you soon.''')
else:
    if user_choice == "No".lower():
        quit()

with open("volumes.txt" , "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d, %H:%M}, {w},", end=" ", file=volumes_file)
    print(f"{a}, {d}, {volume:.2f}, {phone_number}", file=volumes_file)
