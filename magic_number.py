# Import random module to use in this program.
import random

def main():
    try:
        guess_count = 0
        guess = -1
        print("""Think of a magic number, use your imagination to guess the number.
Good thing about this game is that, you will get hints as you try to guess the number.
If you guess lower than the magic number, you will get a hint to guess higher if you guess
higher you will get a hint to guess lower.
Good luck.""")
        print()

        # Since this is number guessing game
        # we want to check fisrt if the user
        # would still want to play the 
        # game after their fisrt round.
        play_again = "yes"
        while play_again == "yes".lower():
            magic_number = random.randint(0, 100)
            guess_count += 1
            # print(f"The magic number is: {magic_number}")

            # Using a while loop, get
            # user to geuss the magic number,
            # until they guess the number, user
            # must continue to guess until 
            # they guess the number.
            guess_count = 0
            guess = -1
            while guess != magic_number:
                guess = int(input("Guess the magic number: "))
                guess_count += 1
                # Give a hint to the user if their guess
                # was higher, give them
                # a hint to guess lower.
                if guess > magic_number:
                    print("Lower") 

                # If the user guesses lower give them
                # a hint to guess higher.
                elif guess < magic_number:
                    print("Higher")   

                # If the user guesses the magic number
                # print a message telling them that they
                # guessed it and count how many guesses
                # it took for them to guess the magic number. 
                else:
                    if guess == magic_number:
                        print()
                        print(f"You guessed it! The magic number is {magic_number}.")
                        if guess_count == 1:
                            print(f"It took you {guess_count} guess.")
                        else:
                            if guess_count >= 2:
                                print(f"It took you {guess_count} guesses.")  

            # Ask the user if they want to contnue playing
            # check if they reply yes or no.
            # If they reply yes, program must automatically
            # start from scratch.
            # If they reply no print a message thanking them
            # playng the game.
            print()                    
            play_again = input("Do you want to play again? [Yes/No]: ").lower()
            if play_again == "No".lower():
                print("Thank you for playing, Goodbye!!!")

    # Check for any value errors that the user might enter
    # and handle the (error/s) as simple as you can,
    # for user understand.
    except ValueError as val_err:
        print(f"Error: run program again enter a valid integer")

if __name__ == "__main__":
    main()
