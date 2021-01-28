# LEARNING PATH - Take your first steps with Python

# CHALLENGE - IF ... ELSE Statement

def challenge(msg):
    if msg == "no" or msg == "n":
        return "Exiting"
    elif msg == "yes" or msg == "y":
        return "Continuing ...\nComplete!"
    else:
        return "Please try again and respond with yes or no."

#message = input("Would you like to continue? ")


#  CHALLENGE - Manipulate and format string data for display in Python

first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge

f_v = []

for i in first_value.split():
    if i.isalpha():
        f_v.append(i.capitalize())

first_value = " " * 7 + " ".join(f_v)

# Second challenge

s_v = []

for i in second_value.split():
    if i.isalpha():
        s_v.append(i)

second_value = " ".join(s_v).capitalize()

# Third challenge

t_v_1 = third_value.replace(" ", "")
t_v_2 = t_v_1.replace("-", " ")
t_v_3 = []
for i in t_v_2.split():
    t_v_3.append(i)
third_value = " " * 15 + " ".join(t_v_3).capitalize()

#print(first_value)
#print(second_value)
#print(third_value)

# Fourth challenge - use only the print() function (no f-strings)

#print(fourth_value + "#" + fifth_value + "#" + sixth_value)

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.

#print(" " * 8 + fourth_value + "\n" + " " * 8 + fifth_value + "\n" + " " * 8 + sixth_value)


# CHALLENGE - Perform mathematical operations on numeric data in Python - Calculator

def calculator(f_num, oper, s_num):
    operators = "+-**/%"
    if not f_num.isnumeric() or not s_num.isnumeric():
        return "Please input a number."
    elif oper not in operators:
        return "Please enter one of the '+-*/**&' operators"
    else:
        if oper == "+":
            return f"Sum of {f_num} {oper} {s_num} equals {int(f_num) + int(s_num)}"
        elif oper == "-":
            return f"Difference of {f_num} {oper} {s_num} equals {int(f_num) - int(s_num)}"
        elif oper == "*":
            return f"Product of {f_num} {oper} {s_num} equals {int(f_num) * int(s_num)}"
        elif oper == "**":
            return f"Exponent of {f_num} {oper} {s_num} equals {int(f_num) ** int(s_num)}"
        elif oper == "%":
            return f"Modulus of {f_num} {oper} {s_num} equals {int(f_num) % int(s_num)}"
        else:
            if oper == "/" and s_num == "0":
                return "Division by 0 is not possible"
            else:
                if int(f_num) % int(s_num) == 0:
                    return f"Quotient of {f_num} {oper} {s_num} equals {int(f_num) // int(s_num)}"
                else:
                    return f"Quotient of {f_num} {oper} {s_num} equals {int(f_num) / int(s_num)}"

# first_number = input("First number? ")
# operation = input("Operation? ")
# second_number = input("Second number? ")

# print(calculator(first_number, operation, second_number))


# Challenge - Iterate through code blocks by using the while statement - Guess a number

import random

def guess_a_number():
    number = random.randint(1, 5)
    count = 1
    n = int(input("Guess a number between 1 and 5: "))
    while n != number:
        count += 1
        n = int(input("Guess a number between 1 and 5: "))
    return f"You guessed it in {count} tries!"

#print(guess_a_number())


# Challenge - Iterate through code blocks by using the while statement - Improved number guessing

import random

def imroved_number_guessing():
    number = str(random.randint(1, 10))
    n = "0"
    count = 1
    print("Guess a number between 1 and 10: ")
    while n != number:
        n = input(f"Enter guess #{count}: ")
        if n.isdigit():
            if int(n) < int(number):
                print("Your guess is too low, try again!")
            elif int(n) > int(number):
                print("Your guess is too high, try again!")
            elif int(n) == int(number):
                return f"You guessed it in {count} tries!"
        else:
            print("Numbers only, please!")
        count += 1
    
#print(imroved_number_guessing())


# CHALLENGE - Manage a sequence of data by using Python lists - Deal a deck of cards

import random

def deck_of_cards():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    cards_52 = []
    for suit in suits:
        for rank in ranks:
            cards_52.append(f'{rank} of {suit}')
    return cards_52

def player_hand():
    random_five = []
    for i in range(5):
        x = random.randint(0, 51)
        random_five.append(deck_of_cards()[x])
    return random_five

def play():
    player = player_hand()
    cards = deck_of_cards()

    print(f"There are {len(cards)} cards in the deck.")
    print("Dealing ...")

    for i in player:
        if i in cards:
            cards.remove(i)
    
    print(f"There are {len(cards)} cards in the deck.")
    print("Player has the following cards in their hand:")
    print(player)

#play()


# CHALLENGE -  Create reusable functionality with functions in Python - Fill in the missing functions

import processor # create a processor.py file first

my_list = [5, 'Dan', '4', 7, 'Steve', 'Amy', 'Rhonda', 4, '9', 'Jill', 7, 'Kim']
my_bad_list = 5

numbers = processor.process_numbers(my_list)
print(numbers)

names = processor.process_names(my_list)
print(names)

numbers = processor.process_numbers(my_bad_list)
print(numbers)

names = processor.process_names(my_bad_list)
print(names)