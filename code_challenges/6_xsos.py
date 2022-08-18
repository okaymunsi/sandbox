"""
Create a Python function that accepts a string. 
This function should count the number of Xs and the number of Os in the string. 
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. 
If the count isn't the same, it should return False. 
If there are no Xs or Os in the string, it should also return True because 0 equals 0. 
The string can contain any type and number of characters
"""

def user_input():
    xsos = input("Please enter a word/set of words and i'll count x's and o's for you:")
    xsos = list(xsos)

    return xsos

def count_xo(list):
    count_o = 0
    count_x = 0

    for i in list:
        if i == 'o':
            count_o += 1
        if i == 'x':
            count_x += 1
    
    if count_x == count_o:
        print(f"Number of x\'s and o\'s, respectively: {count_x}, {count_o}")
        return True
    else:
        print(f"Number of x\'s and o\'s, respectively: {count_x}, {count_o}")
        return False

print(count_xo(user_input()))

