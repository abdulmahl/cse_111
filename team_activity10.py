from os import remove

import sys
# Create main menu and loop around it till the user selects quit
def main_menu():
    while True:
        print()    
        print('''Welcome to the Shopping Cart Program!\n
        Please select one of the following:
        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Quit''')

        action = input("Please enter an action: ").strip()
        if action == "1":
            addItem()
        elif action == "2": 
            viewCart_items()
        elif action == "3":
            removeItem()
        elif action == "4":
            computeTotal_sum()
        elif action == "5":
            print("Thank you, please proceed to checkout.""\nGoodbye, please visit again soon.")
            print()
            sys.exit()
        else:
            print("Sorry, that is not a valid item number.")

# Creat empty list to store user inputs
cartList = []
priceList = []

# Add items to the list/cart
def addItem():
    add_item = input("What item would you like to add? ")
    cartList.append(add_item)    
    add_price = float(input(f"What is the price of the {add_item}? "))
    priceList.append(add_price)
    print(f"{add_item.capitalize()} has been added to the cart.")

# Views item/s added to the cart
def viewCart_items():
    print("The contents of your shopping cart are:")
    for i in range(len(cartList)):
        add_item = cartList[i]
        add_price = priceList[i]
        print(f"{i+1}. {add_item.capitalize().strip()} - ${add_price}")

# Removes item/s added to or item that is already in the cart
def removeItem():
    remove_item = int(input("Which item would you like to remove? "))
    cartList.pop(remove_item-1)
    remove_item = cartList
    print("Item removed.")

# Computes the total amount of the items in the cart
def computeTotal_sum():
    total_amount = 0
    for add_price in priceList:
        total_amount += add_price
    print(f"The total price of the items in your shopping cart is ${total_amount:.2f}.")    
# Main menu fuction
main_menu() 





