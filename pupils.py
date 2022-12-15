import csv
from pprint import pprint


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    try:

        # Call the read_compound_list function 
        # to read the pupils.csv file into a 
        # list named students_list.
        students_list = read_compound_list("pupils.csv")

        # pprint(students_list)

        sorted_list_oldest_youngest = sort_oldest_to_youngest(students_list)
        print_list(sorted_list_oldest_youngest)

        sorted_list_given_name = sort_by_given_name(students_list)
        print_list(sorted_list_given_name)

        sorted_list_month_day = sort_by_birth_month_day(students_list)
        print_list(sorted_list_month_day)



    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=":")    


def sort_oldest_to_youngest(students_list):
    # Write a lambda function that will 
    # extract the birthdate from a student.
    extract_birthdate = lambda student: student[BIRTHDATE_INDEX]
    
    # Write a call to the Python built-in 
    # sorted function that will sort the students_list 
    # by birthdate from oldest to youngest
    sorted_birthdate = sorted(students_list, key=extract_birthdate)

    return sorted_birthdate


def sort_by_given_name(students_list):

    extract_given_name = lambda student: student[GIVEN_NAME_INDEX]

    sorted_given_name = sorted(students_list, key=extract_given_name)

    return sorted_given_name

def sort_by_birth_month_day(students_list):

    def extract_month_and_day(student):
        birthdate_string = student[BIRTHDATE_INDEX]
        month_and_day = birthdate_string[5:]
        return month_and_day
    sorted_month_and_day = sorted(students_list, key=extract_month_and_day)

    return sorted_month_and_day



def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(compound_list):
    for element in compound_list:
        print(element)
    print()    


if __name__ == "__main__":
    main()