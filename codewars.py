# CODEWARS TASKS ON PYTHON

# TASK - Number of People in the Bus

# There is a bus moving in the city, and it takes and drop some people in each bus stop.
#
# You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which
# represent number of people get into bus (The first item) and number of people get off the bus (The second item)
# in a bus stop.

def number(bus_stops):
    people_in = 0
    people_out = 0
    for stops in bus_stops:
        people_in += stops[0]
        people_out += stops[1]

    return people_in - people_out


# TASK - String ends with?

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument
# (also a string).

def solution(string, ending):
    if string[int(len(ending) * -1):] == ending:
        return True
    else:
        if ending == "":
            return True
        else:
            return False


# TASK - Sum of the first nth term of Series

# Your task is to write a function which returns the sum of following series upto nth term(parameter).

def series_sum(n):
    if n == 0:
        return "0.00"
    elif n == 1:
        return "1.00"
    else:
        result = []
        for i in range(n-1):
            result.append(1 / (3 * i + 4))

        res = str(round(1 + sum(result), 2))
        if len(res) == 3:
            return res + "0"
        else:
            return res


# TASK - Remove the minimum

# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are
# multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return
# an empty array/list.
# Don't change the order of the elements that are left.

def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    else:
        res = []
        for i in numbers:
            res.append(i)
        res.remove(min(numbers))
        return res


# TASK - Breaking chocolate problem

# Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1
# and unbreakable. Implement a function that will return minimum number of breaks needed.

def breakChocolate(n, m):
    res = (n * m) - 1
    if res < 0:
        return 0
    else:
        return res


# TASK - The highest profit wins!

# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    return [min(lst), max(lst)]

# TASK - Odd or Even?

# Given a list of numbers, determine whether the sum of its elements is odd or even.

def odd_or_even(arr):
    if sum(arr) % 2 == 0 or sum(arr) == 0:
        return "even"
    else:
        return "odd"


# TASK - Money, Money, Money

# The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 'T' for the year
# the new sum is re-invested.

def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        year += 1
        income = principal * interest
        pay_taxes = principal * interest * tax
        principal += income
        principal -= pay_taxes
    if principal == desired:
        return 0
    else:
        return year


# TASK - Find the stray number

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.

def stray(arr):
    if arr[0] == arr[1]:
        num = arr[0]
    else:
        if arr[1] == arr[2]:
            num = arr[1]
        else:
            num = arr[2]
    for i in arr:
        if i != num:
            return i


# TASK - Don't give me five!

# n this kata you get the start number and the end number of a region and should return the count of all numbers
# except numbers with a 5 in it. The start and the end number are both inclusive!

def dont_give_me_five(start, end):
    arr = []
    for i in range(start, end + 1):
        arr.append(i)
    count = 0
    for i in arr:
        if "5" in str(i):
            count += 1
    return len(arr) - count


# TASK - Largest 5 digit number in a series

# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number
# given. The number will be passed in as a string of only digits. It should return a five digit integer. The
# number passed may be as large as 1000 digits.

def solution_two(digits):
    sl = 0
    res_list = []
    for count in range(len(digits) - 1):
        res_list.append(int(digits[sl: sl + 5]))
        sl += 1
    return max(res_list)


# TASK - Triangular Treasure

# You need to return the nth triangular number. You should return 0 for out of range values

def triangular(n):
    if n < 0:
        return 0
    else:
        return n * (n + 1) // 2


# TASK - Sum of a sequence

# Your task is to make function, which returns the sum of a sequence of integers.
# The sequence is defined by 3 non-negative values: begin, end, step.
# If begin value is greater than the end, function should returns 0

def sequence_sum(begin_number, end_number, step):
    res = 0
    for i in range(begin_number, end_number + 1, step):
        res += i
    return res


# TASK -

# def factorial(n):
#     print(n)
#     f = n
#     res = n
#     try:
#         if n in range(0, 13):
#             if n == 0:
#                 return 1
#             else:
#                 for i in range(n):
#                     res *= n
#                     n -= 1
#                 return int(res / f)
#     except:
#
#
# print(factorial(3)) #6

# TASK - Convert boolean values to strings 'Yes' or 'No'

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


# TASK - Remove String Spaces

# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(" ", "")


# TASK - Grasshopper - Summation

# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer
# greater than 0.

def summation(num):
    return sum(int(i) for i in range(1, num + 1))


# TASK - Counting sheep...

# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that
# counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s:
            count += 1
    return count


# TASK - Square(n) Sum

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    l = []
    for n in numbers:
        l.append(n ** 2)
    return sum(l)


# Function 1 - hello world

# Make a simple function called greet that returns the most-famous "hello world!".

def greet():
    return "hello world!"


# TASK - Basic Mathematical Operations

# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2


# TASK - Keep Hydrated!

# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the
# smallest value.

def litres(time):
    return int(time * 0.5)


# TASK - Century From Year

# The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and
# including the year 200, etc.

def century(year):
    if year % 100 == 0:
        return year / 100
    else:
        return int(year / 100) + 1


# TASK - Is n divisible by x and y?

# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive,
# non-zero digits.

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


# TASK - Convert a String to a Number!

# We need a function that can transform a string into a number. What ways of achieving this do you know?

def string_to_number(s):
    return int(s)


# TASK - A Needle in the Haystack

# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle

def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))


# TASK - Jenny's secret message

# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like
# to greet him slightly different. She added a special case to her function, but she made a mistake.

def greet_two(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# TASK - Weight for weight - NOT WORKING! TO BE CHECKED LATER!

# from collections import OrderedDict

# def order_weight(strng):
#     res_dict = {}
#     for i in strng.split():
#         l = []
#         for num in i:
#             l.append(int(num))
#         res_dict[i] = sum(l)
#     #od = {k: v for k, v in sorted(res_dict.items(), key=lambda item: item[1])}
#     od = OrderedDict(sorted(res_dict.items(), key=lambda t: t[1]))
#     print(od)
#     res_list = []
#     for i in od.keys():
#         res_list.append(i)
#     return " ".join(res_list)

# print(order_weight("103 123 4444 99 2000"))
# print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")) # "11 11 2000 10003 22 123 1234000 44444444 9999"


# TASK - Summing a number's digits

# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

def sum_digits(number):
    n = int()
    if number < 0:
        n = abs(number)
    else:
        n = number

    return sum([int(i) for i in str(n)])


# TASK - No oddities here

# Write a small function that returns the values of an array that are not odd. 

def no_odds(values):
    l = []
    for i in values:
        if i % 2 == 0:
            l.append(i)
    return l


# TASK - Count the divisors of a number

# Count the number of divisors of a positive integer n.

def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


# TASK - Sum of all the multiples of 3 or 5

# Your task is to write function findSum. Upto and including n, this function will return the sum of all multiples of 3 and 5.

def find(n):
    count = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count


# TASK - Anagram Detection

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

def is_anagram(test, original):
    w = {}
    for i in test.lower():
        w[i] = test.lower().count(i)
    if len(test) == len(original):
        res_l = []
        for i in original.lower():
            if i in test.lower() and original.lower().count(i) in w.values():
                res_l.append(True)
            else:
                res_l.append(False)
        if False in res_l:
            return False
        else:
            return True
    else:
        return False


# TASK - String incrementer - NOT WORKING!!!!!

# import string

# def increment_string(strng):
#     l = []
#     for i in strng:
#         if i in string.digits:
#             l.append(i)
#     if len(l) >= 1:
#         res = strng[:len(l) * -1] + str(int("".join(l)) + 1)
#         if len(strng) == len(res):
#             return res
#         else:
#             return strng[:len(l) * -1] + str("0" * (len(strng) - len(res))) + str(int("".join(l)) + 1)
#     else:
#         return strng + "1"


# print(increment_string("foo001"))
# print(increment_string("foo"))


# TASK -Is he gonna survive?

# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon 
# takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward 
# to fight another specific given number of dragons, will he survive?
#Return True if yes, False otherwise :)


def hero(bullets, dragons):
    return True if bullets / 2 >= dragons else False


# TASK - Reversed sequence 

# Get the number n (n>0) to return the reversed sequence from n to 1.

def reverse_seq(n):
    return [int(i) for i in range(1, n + 1)][::-1]


# TASK - Convert a Boolean to a String

# Implement a function which convert the given boolean value into its string representation.
 
def boolean_to_string(b):
    return "True" if b else "False"


# TASK - MakeUpperCase

# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    return s.upper()


# TASK - altERnaTIng cAsE <=> ALTerNAtiNG CaSe

# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected 
# language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.

def to_alternating_case(string):
    return "".join([i.upper() if i.islower() else i.lower() for i in string])


# TASK - Sum Mixed Array

# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

def sum_mix(arr):
    return sum([int(i) if isinstance(i, str) else i for i in arr])


# TASK - Calculate BMI

# Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

def bmi(weight, height):
    res = weight / height ** 2
    if res <= 18.5:
        return "Underweight"
    elif res <= 25.0:
        return "Normal"
    elif res <= 30.0:
        return "Overweight"
    else:
        return "Obese"


# TASK - Rock Paper Scissors!

# Let's play! You have to return which player won! In case of a draw return Draw!.

def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    
    else:
        return "Draw!"


# TASK - Function 3 - multiplying two numbers

# Implement a function which multiplies two numbers.

def multiply(a, b):
    return a * b


# TASK - Beginner Series #1 School Paperwork

# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need.

def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m


# TASK - Grasshopper - Messi goals functions

# Messi is a soccer player with goals in three leagues:
# LaLiga
# Copa del Rey
# Champions
# Complete the function to return his total number of goals in all three leagues.

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


# TASK - Find the first non-consecutive number

# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.

def first_non_consecutive(arr):
    for i in arr:
        if i != arr.index(i) + arr[0]:
            return i 


# TASK - L1: Set Alarm

# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, 
# vacation is true whenever you are on vacation.
# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It 
# should return false otherwise.

def set_alarm(employed, vacation):
    return True if employed and not vacation else False


# TASK - Double Char

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    return "".join([i * 2 for i in s])


# TASK - Short Long Short

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty ( length 0 ).

def solution_23(a, b):
    return b + a + b if len(a) > len(b) else a + b + a


# TASK - Beginner Series #4 Cockroach

# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the 
# integer (= floored).

def cockroach_speed(s):
    return int(s * 27.7777777778)


# TASK - Decode the Morse code

# In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, 
# it still has its use in some applications around the world.
# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 
# is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used 
# to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

def decodeMorse(morse_code):
    morse_code_dict = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', 'SOS': '...---...',
                    '!': '-.-.--'}
    
    decoded = []
    decoded_res = []
    for i in morse_code.split("   "):
        decoded.append(i)
        decoded.append(" ")
    for i in decoded:
        if i == " ":
            decoded_res.append(" ")
        else:
            for w in i.split():
                for k, v in morse_code_dict.items():
                    if w == v:
                        decoded_res.append(k)
        
    return "".join(decoded_res).lstrip().rstrip()


# TASK - Maximum Multiple

# Given a Divisor and a Bound , Find the largest integer N

def max_multiple(divisor, bound):
    return max(i for i in range(1, bound + 1) if i % divisor == 0)


# TASK - Sort the Gift Code

# Write a function called sortGiftCode/sort_gift_code/SortGiftCode that accepts a string containing up to 26 unique alphabetical characters, 
# and returns a string containing the same characters in alphabetical order.

def sort_gift_code(code):
    return "".join(sorted([i for i in code]))


# TASK - Simple Fun #176: Reverse Letter

# Given a string str, reverse it omitting all non-alphabetic characters.

import string

def reverse_letter(string1):
    return "".join([i for i in string1 if i in string.ascii_letters])[::-1]


# TASK - Palindrome chain length

# Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. 
# The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome, repeat the procedure with the 
# sum until the resulting number is a palindrome.

def palindrome_chain_length(n):
    count = 0
    while str(n) != str(n)[::-1]:
        res = n + int(str(n)[::-1])
        n = res
        count += 1

    return count


# TASK - Gravity Flip

# Given the initial configuration of the cubes in the box, find out how many cubes are in each of the n columns after Bob switches the gravity.

def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a, reverse=True)


# TASK - N-th Power

# You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is 
# outside of the array, then return -1. Don't forget that the first element has the index 0.

def index(array, n):
    try:
       return array[n] ** n
    except:
        return -1


# TASK - Hello, Name or World!

# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

def hello(name=0):
    return f"Hello, {name.capitalize()}!" if name != 0 and name != "" else "Hello, World!"


# TASK - Can we divide it?

# Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.

def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0


# TASK - The falling speed of petals

# Write a function that receives the speed (in cm/s) of a petal as input, and returns the time it takes for that petal to reach the ground from the same branch.

def sakura_fall(v):
    return 80 / (v / 5) if v > 0 else 0


# TASK -

def min_max_odd_even(arr):
    return [min(int(i) for i in arr if int(i) % 2 != 0), max(int(i) for i in arr if int(i) % 2 == 0)]

l = ["1", "4554", "6", "345"]


# TASK - Is the string uppercase?

# Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

def is_uppercase(inp):
    return False if False in [i.isupper() for i in inp.split()] else True


# TASK - Count Odd Numbers below n

# Given a number n, return the number of positive odd numbers below n, EASY!

def odd_count(n):
    return n//2


# TASK - Find numbers which are divisible by given number

# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor == 0]


# TASK - Unfinished Loop - Bug Fixing #1

# Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res.append(i)
        i += 1
    return res


# TASK - Functional Addition

#  Create a function add(n)/Add(n) which returns a function that always adds n to any number

def add(n):
    def summ(x):
        return x + n
    return summ


# TASK - Fizz Buzz

# Replace certain values however if any of the following conditions are met:
# If the value is a multiple of 3: use the value 'Fizz' instead
# If the value is a multiple of 5: use the value 'Buzz' instead
# If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead


def fizzbuzz(n):
    l = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        
        else:
            l.append(i)
    return l
    

# TASK - Remove exclamation marks

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

import re

def remove_exclamation_marks(s):
    return re.sub('[.?!]', '', s)


# TASK - Number toString

# The code gives an error!

a = str(123)


# TASK - Grasshopper - Grade book

# Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    score = int((s1 + s2 + s3) / 3)
    print(score)

    if score in range(0, 60):
        return "F"
    elif score in range(60, 70):
        return "D"
    elif score in range(70, 80):
        return "C"
    elif score in range(80, 90):
        return "B"
    else:
        return "A"


# TASK - Watermelon

# Given an integral number of watermelons w (1 ≤ w ≤ 100; 1 ≤ w in Haskell), check whether Pete and Billy can divide the melons so that each of them 
# gets an even amount.

def divide(weight):
    return weight % 2 == 0 and weight > 2


# TASK - Grasshopper - Messi Goals

# Create these three variables and store the appropriate values
# Create a fourth variable named total_goals that stores the sum of all of Messi's goals for this year

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


# TASK - Grasshopper - Personalized Message

# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
# Use conditionals to return the proper message

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


# TASK - The Feast of Many Beasts

# Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish 
# to the feast.

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


# TASK - Opposites Attract

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    return (flower1 % 2 != 0 and flower2 % 2 == 0) or (flower1 % 2 == 0 and flower2 % 2 != 0)


# TASK - Is it even?

# Your code will determine if the number passed is even (or not). 

def is_even(n): 
    return n % 2 == 0


# TASK - Correct the mistakes of the character recognition software

# Your task is correct the errors in the digitised text.

def correct(string):
    dic = {
        "5": "S",
        "0": "O",
        "1": "I"
    }

    for k, v in dic.items():
        string = string.replace(k, v)
    return string


# TASK - Parse nice int from char problem

# For correct answer program should return int from 0 to 9. Assume 
# test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.

def get_age(age):
    return int(age.split()[0])


# TASK -

def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]


# TASK - Find the unique number


# METHOD 1 - NOT WORKING! - RUNTIME ERROR
# def find_uniq(arr):
#     d = {}
#     for i in arr:
#         d[i] = arr.count(i)
#     for k, v in d.items():
#         if v == 1:
#             return k


# TASK - Split Strings

# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of 
# characters then it should replace the missing second character of the final pair with an underscore ('_').

def solution(s):
    l = []
    c = 0
    for i in range(len(s) // 2):
        l.append(s[c : c + 2])
        c += 2

    return l if len(s) % 2 == 0 else l + [s[-1] + "_"]


# TASK - Sort the odd

# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

def sort_array(source_array):
    l = sorted([i for i in source_array if i % 2 != 0])
    for i in source_array:
        if i % 2 == 0:
            l.insert(source_array.index(i), i)
    return l


# TASK - Count the smiley faces!

# Given an array (arr) as an argument complete the function countSmileys that should return 
# the total number of smiling faces. 

def count_smileys(arr):
    count = 0
    for smile in arr:
        if ")" in smile or "D" in smile:
            if not "oD" in smile:
                count += 1
    return count


# TASK - Build Tower

# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

def tower_builder(n_floors):
    build_tower = []
    star = n_floors
    for i in range(n_floors):
        right_side = (star * "*") + (i * " ")
        left_side = (i * " ") + ((star - 1) * "*")
        build_tower.append(left_side + right_side)
        star -= 1
    return build_tower[::-1]


# TASK - Valid Braces

# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should
# return true if the string is valid, and false if it's invalid.

def validBraces(string):
    new_string = string
    for i in range(len(string) // 2):
        valid_string = new_string.replace("{}", "").replace("()", "").replace("[]", "")
        new_string = valid_string
        
    return len(new_string) == 0


# TASK - Highest Scoring Word

# Given a string of words, you need to find the highest scoring word.
# ach letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.

import string

import string

def high(x):
    l = []
    letters_dict = {}
    for i in string.ascii_lowercase:
        letters_dict[i] = string.ascii_lowercase.index(i) + 1
    for i in x.split():
        res_l = []
        for s in i:
            if s in letters_dict:
                res_l.append(letters_dict[s])
        l.append(sum(res_l))
    return x.split()[l.index(max(l))]


# TASK - I love you, a little , a lot, passionately ... not at all

# Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.

def how_much_i_love_you(nb_petals):
    result = nb_petals - ((nb_petals // 6) * 6)
    if result == 1:
        return "I love you"
    elif result == 2:
        return "a little"
    elif result == 3:
        return "a lot"
    elif result == 4:
        return "passionately"
    elif result == 5:
        return "madly"
    elif result == 0:
        return "not at all"


# TASK - Keep up the hoop

# Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)
# -If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# -If he doesn't get 10 hoops, return the string "Keep at it until you get it". 

def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"


# TASK - Stringy Strings

# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
# the string should start with a 1.
# a string with size 6 should return :'101010'.
# with size 4 should return : '1010'.
# with size 12 should return : '101010101010'.
# The size will always be positive and will only use whole numbers.

def stringy(size):
    result = []
    for i in range(1, size + 1):
        if i % 2 == 0:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


# TASK - Removing Elements

# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

def remove_every_other(my_list):
    l = []
    for i in range(len(my_list)):
        if (i + 1) % 2 != 0:
            l.append(my_list[i])
    return l


# TASK - Vasya - Clerk

# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 
# 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

def tickets(people):
    paydesk = []
    for person in people:
        if person == 25:
            paydesk.append(person)
        elif person == 50:
            try:
                paydesk.remove(25)
                paydesk.append(50)
            except:
                return "NO"
        elif person == 100:
            try:
                paydesk.remove(25)
                if 50 in people:
                    paydesk.remove(50)
                else:
                    paydesk.remove(25)
                    paydesk.remove(25)
                paydesk.append(100)
            except:
                return "NO"
    return "YES"



