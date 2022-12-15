import random

def main():
    try:
        numbers = [16.2, 75.1, 52.3]
        print(f"numbers {numbers}")

        append_random_numbers(numbers)
        print(f"numbers {numbers}")

        append_random_numbers(numbers, 3)
        print(f"numbers {numbers}")

        words = []

        append_random_words(words)
        print(f"words {words}")

        append_random_words(words, 5)
        print(f"words {words}")
        
    except ValueError as val_err:
        print(f"Error: {val_err}")


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        new_number = random.uniform(0, 100)
        rounded = round(new_number, 1)
        numbers_list.append(rounded) 

def append_random_words(words_list, quantity=1):
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]

    for _ in range(quantity):
        new_word = random.choice(candidates)
        words_list.append(new_word)

if __name__ == "__main__":
    main()