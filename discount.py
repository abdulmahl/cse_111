# Problem statement
'''
You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
which are the store's slowest sales days. On Tuesday and Wednesday, 
if a customer's subtotal is $50 or greater, 
the store will discount the customer's subtotal by 10%.
'''

# Import datetime module to be able to use datetime.now.
from datetime import datetime

# Assign the discount rate and the sales rate to variables disc_rate and sales_rate.
disc_rate = .10
sales_rate =.06

# Ask user for the subtotal, get input from user.
subtotal = float(input("Enter the subtotal: "))

# Assign datetime.now to a variable called current_date_and_time
current_date_and_time = datetime.now()

# Check for the days in the week.
weekday = current_date_and_time.weekday()

# Checks if the days are Tuesday or Wednesday, then applies the discount 
# if $50.00 or more is spent on the specified days,
# if the days are not specified
# the discount will not apply even if $50.00 or more was spent.
if subtotal >= 50 and weekday == 0 or weekday == 2:
    discount = round(subtotal * disc_rate, 2)
    print(f"Discount amount: {discount}")
    subtotal -= discount

# Compute the sales tax amount, and display it for the user to see.
sales_tax =  round(subtotal * sales_rate, 2)   
print(f"sales tax: {sales_tax:.2f}")

# Compute the total amount, then print it out for the user to see.
total = subtotal + sales_tax
print(f"Total: {total:.2f}")