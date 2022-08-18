"""
Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent "4444444444444444", then it should return "4444".
"""

def input_credit_card():
    card_num = input("Enter your credit card number:")

    while len(card_num) != 16:
        print("Not enough numbers! Please enter 16 digits")
        card_num = input("Enter your credit card number:")

    return card_num

def privitize_num(card_num):

    split_num = list(card_num)
    for i in range(12):
        split_num[i] = "*" 

    priv_num = ''.join(split_num)
    print(f"privitized credit card number: {priv_num}")

    return

privitize_num(input_credit_card())