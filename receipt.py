import csv
from datetime import datetime


# Index of particular column in
# the products.csv file.
PRODUCT_KEY_NUM_INDEX = 0

def main():
    try:
        # Call read_dict fuction and store it's 
        # in a variable called products_dict.
        products_dict = read_dict("products.csv", PRODUCT_KEY_NUM_INDEX)

        # Print the returned dictionary.
        # print(products_dict)

        # Store the store name in a variable
        # and print it at the top of the
        # store receipt.
        store_name = "Inkom Emporium"
        print(store_name)
        print()

        # Index for a particular column in the
        # resquest.csv file.
        QUANTITY_INDEX = 1

        # Open the request.csv file and store a reference to
        # the opened file variable called request_file.
        with open ("request.csv", "rt") as request_file:

            # Use the csv module to create a reader
            # object to read the opened file.
            reader = csv.reader(request_file)

            # Skip the first line of the file
            # since it cotains headings and not data. 
            next(reader)

            total_items = 0
            tax_rate = .06
            total = 0
            subtotal = 0
            # Read each row one at a time
            # as a list.
            for row_list in reader:
                
                # If the current row is not blank
                # append it to the dictionary.
                if row_list != 0:

                    # Retrieve particular values from both the products.csv
                    # and the request.csv files.
                    prod_key = row_list[0]
                    value = products_dict[prod_key]
                    quantity = row_list[QUANTITY_INDEX]
                    prod_name = value[1]
                    prod_price = value[2]

                    # Sum up the total number of products.
                    total_items += int(quantity)

                    # Sum up the subtotal, multiply each
                    # product price by it's quantity.
                    total_amount = float(prod_price) * int(quantity)

                    # Compute the final total of
                    # all the requested products. 
                    subtotal += total_amount

                    # Compute the sales tax at 6%.
                    sales_tax = subtotal * tax_rate

                    # Sum up the total after adding the
                    # sales tax.
                    total = subtotal + sales_tax

                    # Call the datetime module, use .now
                    # to get the current time as per your
                    # computer's operating system.
                    current_date_time = datetime.now()
                    disc_rate = .10
                    discount = 0
                    disc_total = 0
                    weekday = current_date_time.weekday()

                    # Print out the results on the terminal.
                    print(f"{prod_name} {quantity} @ {prod_price}")
            print()
            print(f"Number of items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")

            # Check if weekday is Tue or Wed
            # if so, apply 10% discount to the total
            # then print it out on the terminal.
            if weekday == 1 or weekday == 2:
                discount = (subtotal * disc_rate)
                subtotal -= discount
                print(f"Discount amount: ${discount:.2f}")
                # Sum the discounted total after 
                # adding the sales tax.
                total = subtotal + sales_tax
            print(f"Sales tax: ${sales_tax:.2f} ")
            print(f"Total: ${total:.2f}")
            print()
            print("Thank you for shopping at the Inkom Emporium.")
            print(f"{current_date_time:%A %H:%M %b %d %Y}")

    except(FileNotFoundError, PermissionError) as error:
        print("Error: missing file.") 
        print(error)

    except KeyError as error:
        print(f"Error: unknown product ID in the request.csv file {error}"  ) 
    print()      


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create empty dictionery to store data from the csv file.
    dictionary = {}

    # Open the csv file for reading and store
    # the refeference to the opened file as csv_file.
    with open (filename, "rt") as csv_file:

        # Use the csv module to create a reader 
        # object that will from the opened csv file.
        reader = csv.reader(csv_file) 

        # Skip the first row of reader (csv_file)
        # since the it contains column headings and not 
        # any data.
        next(reader)

        # Read the rows in the csv file one row at a time.
        # The reade object returns each row as a list.
        for row_list in reader:

            # If current row is not blank
            # add data from it to the dictionary
            if row_list != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                prod_key = row_list[key_column_index]

            # Store data from the current row into
            # the dictionary.
            dictionary[prod_key] = row_list

    # Return the dictionary.
    return dictionary 

if __name__ == "__main__":
    main()
        

