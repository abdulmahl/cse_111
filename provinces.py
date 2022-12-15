

def main():
    # Read the contents of the text file named 
    # provinces.txt into a list.
    provinces_list = read_list("provinces.txt")

    # print the contents of the list.
    print(provinces_list)

    # Remove the first element from the list
    provinces_list.pop(0)

    # remove the last element from the list
    provinces_list.pop()

    # Replace all occurances of "AB" in the list with "Alberta".
    for i in range (len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    # Count the number of occurances for "Alberta".
    alberta_count = provinces_list.count("Alberta")

    print()
    # print the number occurances for "Alberta".
    print(f"Alberta occurs {alberta_count} times in the modified list.")


def read_list(filename):

    # Create empty list that will store the 
    # lines of text from the text file.
    text_list = []

    # Open the text file for reading and store the reference 
    # to the opened file in a variable called provinces_file.
    with open (filename, "rt") as provinces_file:

        # Read the contents of the text file
        # one line at a time.
        for line in provinces_file:

            # Remove whitespace from each line 
            # from the beginning and the end of the line.
            clean_line = line.strip()

            # Append the clean line of text onto 
            # the the end of the list.
            text_list.append(clean_line)

    return text_list

if __name__=="__main__":
    main()    