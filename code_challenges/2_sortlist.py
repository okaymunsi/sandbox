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

    return numbers

def munty():
    final_number, final_order = userinput()
    sortlist(final_number, final_order)

def solution(numbers=[], order=None):
    answer = None
    if order == 'asc':
        answer = sorted(numbers)
    elif order == 'desc':
        answer = sorted(numbers, reverse=True)
    elif order is None:
        answer = numbers
    else:
        print(f'Warning: "{order}" is not one of "asc", "desc", or None')
        exit(1) # Typically raise exception
    return answer

def munsi():
    # Random Testing
    random_order = random.choice(['asc', 'desc', None, 0])
    random_numbers = [random.randint(-100, 100) for i in range(0, random.randint(0, 100))]
    print(f'Order: {random_order}')
    print(f'Original Number: {random_numbers}')
    answer = solution(random_numbers, random_order)
    print()
    print(answer)

munsi()