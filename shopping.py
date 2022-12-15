def main():
    try:
        print('''Welcome to the Shopping Cart Program!
Please select an action to perform:
1. Add item to cart
2. View cart
3. Remove item from cart
4. Compute total        
5. Quit''')
        while True:    
            choice = input("Please make a choice: ").strip()

            if choice == "1":
                add_items()

            elif choice == "2":
                view_cart_items()

            elif choice == "3":
                remove_item()

            elif choice == "4":
                compute_total()

            elif choice == "5":
                print("Thank you for shopping with us, Goodbye!")
                quit()

            else:
                if choice != "1" or "2" or "3" or "4" or "5":
                    print("Invalid choice!")

    except ValueError as val_err:
        print("Error:", val_err)
        print("Run the program again and enter valid input")

# Create a empty list to contain
# all the items added. 
cart_list = []

# Create empty list for the price of each added item.
price_list = []
 
# Define add_items function that will prompt the user
# to add items and the price for each item
# and append them to the lists that are given.
def add_items():
    item_add = str(input("Add Item! ")).capitalize().strip()
    cart_list.append(item_add)
    item_price = float(input(f"What is the price for {item_add}? "))
    price_list.append(item_price)
    print()
    print(f"Added to cart, '{item_add}' ")


# Define view_cart_items function that will enable the user to
# view their shopping cart.
def view_cart_items():
    print("The contents of your shopping cart are: ")
    for i in range(len(cart_list)):
        item_add = cart_list[i]
        item_price = price_list[i]
        print(f"{i+1}. {item_add} - ${item_price}")  


# Define remove_item function for the user to be able to
# remove items by their index number not by their names.
# function removes both the item and it's price.
def remove_item():
    remove_item = int(input("Which item would you like to remove? "))
    cart_list.pop(remove_item-1)
    price_list.pop(remove_item-1)
    remove_item = cart_list 
    print("Item removed")


# Define compute_total function for the user
# to able to calculate how much the items
# in their shopping cart will total to.
def compute_total():
    total_amount = 0
    for item_price in price_list:
        total_amount += item_price
    print(f"Total for all your items is ${total_amount:.2f}")


# Call the main function for the program to start executing.
if __name__ == "__main__":
    main()