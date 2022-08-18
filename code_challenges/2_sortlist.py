"""
Create a function in Python that accepts two parameters. 
The first will be a list of numbers.
 The second parameter will be a string that can be one of the following values: asc, desc, and none.
If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
 If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.
"""
import random

def userinput():
    order_set = ["asc", "desc", "none"]
    order = ""
    while order not in order_set:
        order = input("Choose how the numbers should be ordered (asc, desc, none):")
    
    numbers = [random.randint(0,num) for num in range(1,40,2)]

    return numbers, order

def sortlist(numbers, order):
    print(f"original: {numbers}")

    if order == "asc":
        numbers.sort()
        print(f"ascending: {numbers}")
    elif order == "desc":
        numbers.sort(reverse = True)
        print(f"descending: {numbers}")
    elif order == "none":
        print(f"no change: {numbers}")

    return

final_number, final_order = userinput()
sortlist(final_number, final_order)