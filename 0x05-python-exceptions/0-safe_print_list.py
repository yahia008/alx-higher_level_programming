#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in my_list:
            if counter < x:
                print(i, end="")
                counter += 1
        print()
        return counter
    except Exception as e:
        print(f"An error occurred: {e}")
        return counter
