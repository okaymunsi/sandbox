"""
Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""

name = input("Give me a single word:")
whitespace = " "

while whitespace in name:
    name = input("Too many words, give me a single word:")

characters = list(name)
count = 0

for num in characters:
    if num == 'a' or num == 'e' or num == 'i' or num == 'o' or num == 'u':
        count += 1

print(f"The number of vowels are: {count}")