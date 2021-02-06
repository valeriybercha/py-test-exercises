# Coding challenges solutions on Edabit platform


# TASK - How Edabit Works

def hello():
	return "hello edabit.com"


# TASK - Return the Sum of Two Numbers

# Create a function that takes two numbers as arguments and return their sum.

def addition(num1, num2):
    return num1 + num2


# TASK - Return the Next Number from the Integer Passed

# Create a function that takes a number as an argument, increments the number by +1 and returns the result.

def addition(num):
    return num + 1


# TASK - Buggy Code (Part 1)

# Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to 
# get an idea of what the function should do.

def cubes(a):
	return a ** 3


# TASK - Find the Perimeter of a Rectangle

# Create a function that takes length and width and finds the perimeter of a rectangle.

def find_perimeter(l, w):
    return 2 * (l + w)


# TASK - Convert Minutes into Seconds

# Write a function that takes an integer minutes and converts it to seconds.

def convert(min):
    return min * 60


# TASK - Area of a Triangle

# Write a function that takes the base and height of a triangle and return its area.

def tri_area(base, height):
    return (base * height) / 2


# TASK - Convert Hours into Seconds

# Write a function that converts hours into seconds.

def how_many_seconds(hours):
    return hours * 60 * 60


# TASK - Maximum Edge of a Triangle

# Create a function that finds the maximum range of a triangle's third edge, where 
# the side lengths are all integers.

def next_edge(side1, side2):
    return (side1 + side2) - 1


# TASK - Return the Remainder from Two Numbers

# There is a single operator in Python, capable of providing the remainder of a 
# division operation. Two numbers are passed as parameters. The first parameter 
# divided by the second parameter will have a remainder, possibly zero. Return that value.

def remainder(num1, num2):
    return num1 % num2


# TASK - Return a String as an Integer

# Create a function that takes a string and returns it as an integer.

def string_int(str):
    return int(str)


# TASK - Convert Age to Days

# Create a function that takes the age and return the age in days.

def calc_age(num):
    return num * 365


# TASK - Power Calculator

# Create a function that takes voltage and current and returns the calculated power.

def circuit_power(voltage, current):
    return voltage * current


# TASK - Sum of Polygon Angles

# Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

def sum_polygon(n):
    return (n - 2) * 180


# TASK - To the Power of _____

# Create a function that takes a base number and an exponent number and returns the calculation

def calculate_exponent(base, exponent):
    return base ** exponent


# TASK - Word without First Character

# Create a function that takes a word and returns the new word without including the first character.

def new_word(str):
    return str[1:]


# TASK - Reverse the Case

# Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.

def reverse_case(message):
    res = []
    for i in message:
        if i.islower():
            res.append(i.upper())
        else:
            res.append(i.lower())
    return "".join(res)


# TASK - Hiding the Card Number

# Write a function that takes a credit card number and only displays the last four characters. The rest of the 
# card number must be replaced by ************.

def card_hide(card):
    return "*" * len(card[:-4]) + card[-4:]


# TASK - Alphabet Soup

# Create a function that takes a string and returns a string with its letters in alphabetical order.

def alphabet_soup(word):
    return "".join(sorted([i for i in word]))


# TASK - Letters Only

# Write a function that removes any non-letters from a string, returning a well-known film title.

def letters_only(str):
    l = [chr(i) for i in range(97, 122)]
    res = []
    for i in str:
        if i.lower() in l:
            res.append(i)
    return "".join(res)


# TASK - Sort Numbers in Descending Order

# reate a function that takes any non-negative number as an argument and returns it with its digits in descending order. 
# Descending order is when you sort from highest to lowest.

def sort_descending(num):
    return int("".join(sorted([i for i in str(num)])[::-1]))


# TASK - Return the Middle Character(s) of a String

# Create a function that takes a string and returns the middle character(s). If the word's length is odd, return the middle
# character. If the word's length is even, return the middle two characters.

def get_middle(word):
    if len(word) % 2 == 0:
        return word[len(word) // 2 - 1 : len(word) // 2 + 1]
    else:
        return word[(len(word) - 1) // 2]

    
# TASK - Finding Nemo

# You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found 
# Nemo at [the order of the word you find nemo]!".
# If you can't find Nemo, return "I can't find Nemo :(".

def find_nemo(sentence):
    if "Nemo" in sentence.split():
        return "I found Nemo at {}!".format(sentence.split().index("Nemo") + 1)
    else:
        return "I can't find Nemo :("


# TASK - Reverse the Odd Length Words

# Given a string, reverse all the words which have odd length. The even length words are not changed.

def reverse_odd(text):
    res = []
    for i in text.split():
        if len(i) % 2 != 0:
            res.append(i[::-1])
        else:
            res.append(i)
    return " ".join(res)


# TASK - Game of Thrones: Character Titles

# Write a function that takes a string and returns a string with the correct case for character titles in the Game of Thrones series.
# The words and, the, of and in should be lowercase.
# All other words should have the first character as uppercase and the rest lowercase.

def correct_title(sentence):
    res = []
    sntnc = ""
    not_titled = ["and", "the", "of", "in"]
    
    for i in sentence:
        if not i.islower():
            sntnc += i.lower()
        else:
            sntnc += i
    
    for i in sntnc.split():
        if "-" in i:
            new_i = []
            x = i.split("-")
            for n in x:
                if n in not_titled:
                    new_i.append(n)
                else:
                    new_i.append(n.title())
            res.append("-".join(new_i))
        else:
            if i in not_titled:
                res.append(i)
            else:
                res.append(i.title())
    
    pre_res = " ".join(res)
    f = 0
    final_res = ""
    
    if "'" in pre_res:
        f += pre_res.index("'")
        final_res = pre_res.replace(pre_res[f + 1], pre_res[f + 1].lower())
    else:
        final_res = pre_res

    return final_res