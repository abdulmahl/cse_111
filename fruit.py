def main():
    try:

        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        fruit_list.reverse()
        print(f"reverse: {fruit_list}")

        fruit_list.append("orange")
        print(f"orange append: {fruit_list}")
        
        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"insert cherry: {fruit_list}")

        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")

        last = fruit_list.pop()
        print(f"pop {last}: {fruit_list}")

        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        fruit_list.clear()
        print(f"cleared: {fruit_list}")

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")
    

if __name__ == "__main__":
    main()    