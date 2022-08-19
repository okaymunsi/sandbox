"""
Create a Python function that accepts a string. 
The function should return a string, with each character in the original string doubled.
If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
"""
#get input string with no restrictions
#split string into characters (either through the split method or turning it into a list)
#for every iteration through the list, append the character twice to a new list
#join the new list into a string with no delimiter (or delimiter = '')

def munty():
    entry = input("Give me a string and i'll double it for you!")
    separated_entry = list(entry)
    doubled_entry = []

    for elem in separated_entry:
        for i in range(2):
            doubled_entry.append(elem)

    print(''.join(doubled_entry))

def solution(singular=''):
    doubled = ''
    for character in singular:
        doubled += 2*character
    return doubled

def munsi():
    answer = solution('who')
    print(answer)

munsi()