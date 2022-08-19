"""
Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
The function should return a list with only the integers in the original list in the same order.

"""

import random

def input_list():
    # input a list of elements into a variable
    # if the type of the variable isn't a list, keep on looping (use while)
    # check if elements that are numbers, are not negative
    
    mix_elements = input("Enter a list of elements mixed with numbers and strings (please separate by \",\"):")
    mix_elements = mix_elements.split(",")

    for i in range(len(mix_elements)):
        mix_elements[i] = mix_elements[i].strip()
    
        if mix_elements[i][0] == '-':
            mix_elements[i] = input(f"{mix_elements[i]} is a negative number! Please input a positive number:")
        if mix_elements[i][0].isdigit() == True:
            mix_elements[i] = int(mix_elements[i])
    
    return mix_elements

def input_list_pythonic():
    # input a list of elements into a variable
    # if the type of the variable isn't a list, keep on looping (use while)
    # check if elements that are numbers, are not negative
    
    mix_elements = input("Enter a list of elements mixed with numbers and strings (please separate by \",\"):")
    mix_elements = mix_elements.split(",")

    integers = []
    for element in mix_elements:
        element = element.strip()
        if element == '':
            continue

        if element.startswith('-'):
            print(f"Warning: {element} is a negative number! Skipping..")
            continue

        if element.isdigit():
            integers.append(int(element))
    return integers

def num_list(elem):
    numbers_only = []
    for i in elem:
        if type(i) == int:
            numbers_only.append(i)
    
    print(numbers_only)
    return

def munty():
    num_list(input_list())

def solution(input_list=[]):
    answer = []

    for element in input_list:
        if isinstance(element, int):
            answer.append(element)

    return answer

def munsi():
    answer = solution(['a', 1, '1', 'b', 'c', 3, -2, 'z', 0])
    print(answer)

#munsi()
munty()