
"""
A common task for many knowledge workers is to use a number, key,
or ID to look up information about a person. For example, a
knowledge worker may use a phone number or e-mail address as a key
to find (or look up) additional information about a customer.
During this activity, your team will write a Python program that
uses a student's I-Number to look up the student's name.
"""

import csv

def main():
    # Column headings and indexes.
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    # Read the comtents of the csv file called students.csv
    # into a dictionary named students_dict. Use the
    # I-Number as the key in the dictionary.
    students_dict = read_dict("students.csv", I_NUMBER_INDEX)

    # Get the I-Number from the user.
    inumber = input("Please enter I-number (xx-xxx-xxxx): ")

    # The I-Number is stored as digits only and have no dashes, so
    # we will remove all the dashes from the user input. 
    inumber = inumber.replace("-", "")

    # Determine if user input is formatted correctly.
    if not inumber.isdigit():
        print("Invalid character in I-number" )
    else:
        if len(inumber) < 9:
            print("Invaid I-Number: too few digits" )
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # If user input is a valid number, find the
            # I-Number in the list if I-Numbers.
            if inumber not in students_dict:
                print("No such student")
            else:
                # Retrieve the name of the student and check if
                # the I-Number corresponds to the I-Number that the user entered. 
                value = students_dict[inumber]
                name = value[NAME_INDEX]

                # Print the name.
                print(name)


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

    # Create empty dictionary to store 
    # the data from the csv file.
    dictionary = {}

    # Open the csv file for reading and store a reference
    # for the opened csv file in a variable called csv_file.
    with open (filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the open csv file.
        reader = csv.reader(csv_file)

        # This line of code skips the first row of 
        # the csv file.
        next(reader)

        # Read the rows from the csv file one row at a time.
        # The reader object returns the each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

        # Return dictionary.
        return dictionary

if __name__ == "__main__":
    main()