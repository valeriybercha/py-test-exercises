# Python Programming Challenges - https://pythonprinciples.com/challenges/


# TASK - Capital indexes

# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function 
# should return a list of all the indexes in the string that have capital letters.

def capital_indexes(arg):
    res = []
    for i in range(len(arg)):
        if arg[i].isupper():
            res.append(i)
    return res


# TASK - Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the 
# middle letter. If there is no middle letter, your function should return the empty string.

def mid(arg):
    return arg[int((len(arg) - 1) / 2)] if len(arg) % 2 != 0 else ""


# TASK - Online status

# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from 
# strings of names to the string "online" or "offline", as seen above.

def online_count(arg):
    c = 0
    for i in arg.values():
        if i == "online":
            c += 1
    return c


# TASK - Randomness

# Define a function, random_number, that takes no parameters. The function must generate a random integer 
# between 1 and 100, both inclusive, and return it.

import random

def random_number():
    return random.randint(1, 100)


# TASK - Type check

# Write a function named only_ints that takes two parameters. Your function should return True if 
# both parameters are integers, and False otherwise.

def only_ints(arg1, arg2):
    if type(arg1) == int and type(arg2) == int:
        return True
    else:
        return False


# TASK - Double letters

# Define a function named double_letters that takes a single parameter. The parameter is a 
# string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(arg):
    c = 0
    count = []
    for i in range(len(arg) - 1):
        if arg[c] == arg[c+1]:
            count.append(1)
            c += 1
        else:
            count.append(0)
            c += 1
    return True if 1 in count else False


# TASK - Adding and removing dots

# Write a function named add_dots that takes a string and adds "." in between each letter. 
# For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes 
# all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

def add_dots(arg):
    return ".".join(i for i in arg)

def remove_dots(arg):
    string = ""
    for i in arg:
        if i == ".":
            string += ""
        else:
            string += i
    return string


# TASK - Counting syllables

# Define a function named count that takes a single parameter. The parameter is a string.
# The string will contain a single word divided into syllables by hyphens

def count(arg):
    return len(arg.split("-"))


# TASK - Anagrams

# Write a function named is_anagram that takes two strings as its parameters. Your function 
# should return True if the strings are anagrams, and False otherwise.

def is_anagram(arg1, arg2):
    return sorted([i for i in arg1]) == sorted([i for i in arg2])


# TASK - Flatten a list

# Write a function that takes a list of lists and flattens it into a one-dimensional list.

def flatten(arr):
    res = []
    for i in arr:
        for e in i:
            res.append(e)
    return res


# TASK - Min-maxing

# Your function should compute and return the difference between the largest and smallest number in the list.

def largest_difference(arr):
    return max(arr) - min(arr)


# TASK - Divisible by 3

# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and 
# False otherwise.

def div_3(arg):
    return arg % 3 == 0


# TASK - Tic tac toe input

# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). 
# Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

def get_row_col(arg):
    d = {"A": 0,
         "B": 1,
         "C": 2}
    return (int(arg[1]) - 1, d[arg[0]])


# TASK - Palindrome

# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a 
# palindrome, and False otherwise.

def palindrome(arg):
    return arg == arg[::-1]


# TASK - Up and down

# Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; 
# the first should be one lower than the parameter, and the second should be one higher.

def up_down(par):
    return (par - 1, par + 1)


# TASK - Consecutive zeros

# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest 
# number of consecutive zeros in the string.

def consecutive_zeros(str):
    if "1" in str:
        res = []
        c = 0
        for i in str:
            if i == "0":
                c += 1
            else:
                res.append(c)
                c = 0
        return max(res)
    else:
        return str.count("0")


# TASK - All equal

# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

def all_equal(arr):
    if len(arr) > 0:
        res = []
        x = arr[0]
        for i in arr:
            if i == x:
                res.append("y")
            else:
                res.append("n")
        if "n" in res:
            return False
        else:
            return True
    else:
        return True


# TASK - Boolean and

# Define a function named triple_and that takes three parameters and returns True only if they are all True 
# and False otherwise.

def triple_and(arg1, arg2, arg3):
    return arg1 and (arg2 and arg3)


# TASK - Writing short code

# Define a function named convert that takes a list of numbers as its only parameter and returns a 
# list of each number converted to a string.

def convert(arr):
    return [str(i) for i in arr]


# TASK - Custom zip

# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the 
# a list and one from b.

def zap(a, b):
    res = []
    for i in range(len(a)):
        res.append((a[i], b[i]))
    return res


# TASK - Solution validation

# The aim of this challenge is to write code that can analyze code submissions. We'll 
# simplify things a lot to not make this too hard.
# Write a function named validate that takes code represented as a string as its only parameter.

def validate(str):
    if not "def" in str:
        return "missing def"
    elif not ":" in str:
        return "missing :"
    elif not ("(" or ")") in str:
        return "missing paren"
    elif "(" + ")" in str:
        return "missing param"
    elif not "    " in str:
        return "missing indent"
    elif not "validate" in str:
        return "wrong name"
    elif not "return" in str:
        return "missing return"
    else:
        return True


# TASK - List xor

# Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
# Your function must return whether n is exclusively in list1 or list2.
# In other words, if n is in both lists or in none of the lists, return False. If n is in only one 
# of the lists, return True.

def list_xor(n, list1, list2):
    return False if n in list1 and n in list2 else (True if n in list1 or n in list2 else False)


# TASK - Counting parameters

# Define a function param_count that takes a variable number of parameters. The function should 
# return the number of arguments it was called with.

def param_count(*args):
    return len(args)


# TASK - Thousands separator

# Write a function named format_number that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousands separator.

def format_number(num):
    conv = str(num)[::-1]
    return ",".join([conv[i:i+3] for i in range(0, len(conv), 3)])[::-1]