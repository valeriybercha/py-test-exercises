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

# TASK - Write Number in Expanded Form

# You will be given a number and you will need to return it as a string in Expanded Form.

def expanded_form(num):
    str_num = str(num)
    l = []
    count = 0
    for i in range(len(str_num)):
        if str_num[count] != "0":
            l.append(str_num[count] + ("0" * (len(str_num[count:]) - 1)))
            count += 1
        else:
            count += 1
    return " + ".join(l)


# TASK - How many lightsabers do you own?

# The only person who owns lightsabers is Zach, by the way. He owns 18, which is an awesome number of 
# lightsabers. Anyone else owns 0.
# Note: your function should have a default parameter.

def how_many_light_sabers_do_you_own(name=0):
    return 18 if name == "Zach" else 0


# TASK - Exclusive "or" (xor) Logical Operator

# In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). 
# The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise.

def xor(a,b):
    return False if (a and b) or (not a and not b) else True


# TASK - All Star Code Challenge #18

# Create a function called that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

def str_count(strng, letter):
    return strng.count(letter)


# TASK - Switch it Up!

# When provided with a number between 0-9, return it in words.

def switch_it_up(number):
    d = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return d[number]


# TASK - Reversed Strings
# Complete the solution so that it reverses the string value passed into it.


def solution(string):
    if len(string) > 1:
        new_string_l = list(reversed(string))
        return ''.join(new_string_l)
    else:
        return string


# TASK - Convert number to reversed array of digits
# Given a random number:
#     C#: long;
#     C++: unsigned long;
# You have to return the digits of this number within an array in reverse order.


def digitize(n):
    return list(map(int, (reversed(str(n)))))


# TASK - Mumbling
# This time no story, no theory. The examples below show you how to write function accum
# The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(s):
    result = list()
    for elem in range(len(s)):
        res = s[elem] * (elem+1)
        result.append(res.capitalize())
    return '-'.join(result)


# TASK - Tribonacci Sequence
# Well met with Fibonacci bigger brother, AKA Tribonacci.
# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers
# of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian
# speakers trying to pronounce it :(
# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this
# sequence:
# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts
# the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted
# by 2 places, but that is not the case and we would get:
# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a
# signature array/list, returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty
# array (except in C return NULL) and be ready for anything else which is not clearly specified ;)


def tribonacci(signature, n):
    final_list = list()
    if n < 3:
        if n == 0:
            return final_list
        else:
            if n == 1:
                final_list = [signature[0]]
                return final_list
            else:
                final_list = [signature[0], signature[1]]
                return final_list
    if len(final_list) == 0:
        for item in signature:
            final_list.append(item)
    while len(final_list) != n:
        res = final_list[-1] + final_list[-2] + final_list[-3]
        final_list.append(res)

    return final_list


# TASK - Find the smallest integer in the array
# Given an array of integers your solution should find the smallest integer.


def find_smallest_int(arr):
    return min(arr)


# TASK - Welcome!
# Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding
# countries. Marketing thinks it would be great to welcome visitors to the site in their own language. Luckily you
# already use an API that detects the user's location, so this is an easy win.
# The Task
# Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy
# and paste!
# Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have
# it in your database. It should default to English if the language is not in the database, or in the event of an
# invalid input.


def greet(language):
    greetings = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }

    if language in greetings.keys():
        return greetings[language]
    else:
        return greetings['english']


# TASK - Get Planet Name By ID
# The function is not returning the correct values. Can you figure out why?


def get_planet_name(id):
    name = {
            1: "Mercury",
            2: "Venus",
            3: "Earth",
            4: "Mars",
            5: "Jupiter",
            6: "Saturn",
            7: "Uranus",
            8: "Neptune"
        }
    if id in name.keys():
        return name[id]


# TASK - Vowel Count
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def getCount(inputStr):
    vowel_count = {}
    for vowel in "aeiou":
        count = inputStr.count(vowel)
        vowel_count[vowel] = count

    vowels_sum = sum(vowel_count.values())
    return vowels_sum


# TASK - Bus Timer
# It's been a tough week at work and you are stuggling to get out of bed in the morning.
# While waiting at the bus stop you realise that if you could time your arrival to the nearest minute you could
# get valuable extra minutes in bed.
# There is a bus that goes to your office every 15 minute, the first bus is at 06:00, and the last bus is at 00:00.
# Given that it takes 5 minutes to walk from your front door to the bus stop, implement a function that when given
# the curent time will tell you much time is left, before you must leave to catch the next bus.
# Notes
# Return the number of minutes till the next bus
# Input will be formatted as HH:MM (24-hour clock)
# The input time might be after the buses have stopped running, i.e. after 00:00


def bus_timer(current_time):
    hour_time = int(current_time[:2])
    minute_time = int(current_time[3:5])

    if hour_time in range(6, 24):
        if hour_time == 23 and minute_time > 55:
            return 360 - (minute_time + 5 - 60)
        else:
            if minute_time + 5 <= 15:
                return 15 - (minute_time + 5)
            elif minute_time + 5 <= 30:
                return 30 - (minute_time + 5)
            elif minute_time + 5 <= 45:
                return 45 - (minute_time + 5)
            elif minute_time + 5 > 60:
                return 15 - ((minute_time - 60) + 5)
            else:
                return 60 - (minute_time + 5)

    else:
        if hour_time == 5 and minute_time > 55:
            return 15 - (minute_time + 5 - 60)
        else:
            return (6 - hour_time - 1) * 60 - 10 + (60 - minute_time + 5)


# TASK - Get the Middle Character
# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
# return the middle character. If the word's length is even, return the middle 2 characters.

def get_middle(s):
    if len(s) % 2 == 0:
        slicing = int(len(s) / 2)
        return s[slicing - 1] + s[slicing]
    else:
        slicing = int(len(s) / 2)
        return s[slicing]


# TASK - You're a square!
# You like building blocks. You especially like building blocks that are squares. And what you even like more, is
# to arrange them into a square of square building blocks!
# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those
# blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just
# have to check if your number of building blocks is a perfect square.
# Given an integral number, determine if it's a square number.

import math


def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        r = math.sqrt(n)
        if str(r)[-1] == "0":
            return True
        else:
            return False


# TASK - Highest and Lowest
# In this little assignment you are given a string of space separated numbers, and have to return the highest and
# lowest number.

def high_and_low(numbers):
    l = list(map(int, numbers.strip().split()))
    return str(max(l)) + " " + str(min(l))


# TASK - Even or Odd
# Create a function (or write a script in Shell) that takes an integer as an argument and
# returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# TASK - Opposite number
# Very simple, given a number, find its opposite.

def opposite(number):
    if number > 0:
        return number - (number * 2)
    else:
        return number + (-number * 2)


# TASK - Sum of positive
# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    positive_l = []
    for number in arr:
        if number > 0:
            positive_l.append(number)
    return sum(positive_l)


# TASK - Return Negative
# In this simple assignment you are given a number and have to make it negative. But maybe the number is
# already negative?

def make_negative(number):
    if number > 0:
        return number - (number * 2)
    else:
        return number


# TASK - Remove First and Last Character
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters
# of a string. You're given one parameter, the original string. You don't have to worry with strings with
# less than two characters.

def remove_char(s):
    return s[1:-1]


# TASK - String repeat
# Write a function called repeatString which repeats the given String src exactly count times.

def repeat_str(repeat, string):
    return repeat * string


# TASK - Reverse words

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the
# string should be retained.

import re


def reverse_words(text):
    text_split = re.split("(?<!\\s) ", text)
    final_list = []
    for word in text_split:
        if word != "":
            if word[0] == " ":
                final_word = word[1:]
                final_list.append(" " + final_word[::-1])
            else:
                final_list.append(word[::-1])
    return " ".join(final_list)


# TASK - Dubstep

# The input consists of a single non-empty string, consisting only of uppercase English letters, the string's
# length doesn't exceed 200 characters
# Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.


def song_decoder(song):
    d = song.replace("WUB", " ")
    list_d = d.split()
    return " ".join(list_d)


# TASK - Square Every Digit

# For example, if we run 9119 through the function, 811181 will come out, because 9**2 is 81 and 1**2 is 1.

def square_digits(num):
    num_l = []
    str_l = []
    for number in str(num):
        num_l.append(int(number)**2)
    for i in num_l:
        str_l.append(str(i))
    str_num = "".join(str_l)
    return int(str_num)


# TASK - Title Case

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words).
# The list of minor words will be given as a string with each word separated by a space. Your function should ignore
# the case of the minor words string -- it should behave in the same way even if the case of the minor word string
# is changed.

def title_case(title, minor_words=''):
    title_list = title.split(" ")
    words_list = minor_words.split(" ")
    words_list_lower = []
    for e in words_list:
        words_list_lower.append(e.lower())
    final_list = []
    if title == '':
        return ''
    for elem in title_list:
        if elem.lower() in words_list_lower:
            final_list.append(elem.lower())
        else:
            final_list.append(elem.capitalize())
    fin =  final_list[0].capitalize() + " " + " ".join(final_list[1:])
    if fin[-1] == " ":
        return fin[:-1]
    else:
        return fin


# TASK - Persistent Bugger

def persistence(n):
    if len(str(n)) != 1:
        result = n
        count = 0
        while len(str(result)) != 1:
            res = 1
            res_l = [int(i) for i in str(result)]
            for i in res_l:
               res *= i
            result = res
            count += 1
        return count
    else:
        return 0


# TASK - Descending Order

# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits
# in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    desc_list = []
    num_list = [int(i) for i in str(num)]
    for num in range(len(str(num))):
        desc_list.append(str(max(num_list)))
        num_list.remove(max(num_list))
    return int("".join(desc_list))


# TASK - Shortest word

# Simple, given a string of words, return the length of the shortest word(s).

def find_short(s):
    len_list = []
    s_list = s.split(" ")
    for word in s_list:
        len_list.append(len(word))
    return min(len_list)


# TASK - Isograms

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case

def is_isogram(string):
    if string == "":
        return True
    else:
        count = 0
        final_list = []
        string_list = [i for i in string.lower()]
        print(string_list)
        for i in string_list:
            final_list.append(string_list.count(i))
        print(final_list)
        if len(string) == sum(final_list):
            return True
        else:
            return False


# TASK - Disemvowel Trolls

# Your task is to write a function that takes a string and return a new string with all vowels removed.

def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return ''.join([l for l in string if l.lower() not in vowels])


# TASK - Detect Pangram

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
# Ignore numbers and punctuation.

import string


def is_pangram(s):
    lett = [i for i in string.ascii_lowercase]
    res = []
    for e in lett:
        if e in s.lower():
            res.append(1)
        else:
            res.append(0)
    if len(string.ascii_lowercase) == sum(res):
        return True
    else:
        return False


# TASK - Testing 1-2-3

# Write a function which takes a list of strings and returns each line prepended by the correct number.

def number(lines):
    row = 1
    new_list = []
    for line in lines:
        new_list.append(str(row) + ": " + line)
        row += 1
    return new_list


# TASK - Sum of the first nth term of Series - NOT WORKING! TO BE CHECKED LATER!

def series_sum(n):
    if n == 0:
        return "0.00"
    elif n == 1:
        return "1.00"
    else:
        result = []
        for i in range(1, n + 1):
            if i == 1:
                result.append(1)
            elif i == 2:
                result.append(round(1 / (i * 2), 2))
            else:
                result.append(round(1 / ((i * 2) + (i - (i - 1))), 2))

        return str(round(sum(result), 2))


# TASK - Exes and Ohs

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char.

def xo(s):
    x = s.lower().count("x")
    o = s.lower().count("o")
    if x == o:
        return True
    else:
        return False


# TASK - Jaden Casing Strings

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from
# Jaden Smith, but they are not capitalized in the same way he originally typed them.

def to_jaden_case(string):
    result = []
    str_l = string.split()
    for i in str_l:
        result.append(i.capitalize())
    return " ".join(result)


# TASK - List Filtering

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a
# new list with the strings filtered out.

def filter_list(l):
    new_l = []
    for i in l:
        if type(i) == int:
            new_l.append(i)
    return new_l


# TASK - Beginner Series #3 Sum of Numbers

# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including
# them too and return it. If the two numbers are equal return a or b.

# VARIANT 1

def get_sum(a, b):
    result = []
    rev = []
    if a > b:
        rev.append(b)
        rev.append(a)
        for i in range(rev[0], rev[-1] + 1):
            result.append(i)
    elif a == b:
        return a
    else:
        for i in range(a, b + 1):
            result.append(i)
    print(result)
    return sum(result)

# VARIANT 2

def get_sum(a, b):
    result = []
    if a == b:
        return a
    else:
        l = [a, b]
        l.sort()
        for i in range(l[0], l[-1] + 1):
            result.append(i)

    return sum(result)


# TASK - Growth of a Population

# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases
# by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does
# the town need to see its population greater or equal to p = 1200 inhabitants?

def nb_year(p0, percent, aug, p):
    count = 1
    percentage = (percent + 100) / 100
    population_per_year = p0 * percentage + aug
    while population_per_year < p:
        population_per_year = population_per_year * percentage + aug
        print(population_per_year)
        count += 1
    return count


# TASK - Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23.

def solution_1(number):
    l = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
    return sum(l)


# TASK - Find the odd int

# Given an array of integers, find the one that appears an odd number of times. There will always be only one
# integer that appears an odd number of times.

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


# TASK - Sum of Digits / Digital Root

# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this
# way until a single-digit number is produced. This is only applicable to the natural numbers.

def digital_root(n):
    res = [int(i) for i in str(n)]
    if len(str(sum(res))) > 1:
        result = sum(res)
        while len(str(result)) != 1:
            resi = sum([int(i) for i in str(result)])
            result = resi
        return result
    else:
        return sum(res)


# TASK - Who likes it?

# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people
# who like an item

def likes(names):
    res = [1 for i in names]
    if sum(res) >= 1:
        if sum(res) == 1:
            return names[0] + " likes this"
        elif sum(res) == 2:
            return names[0] + " and " + names[1] + " like this"
        elif sum(res) == 3:
            return names[0] + ", " + names[1] + " and " + names[2] + " like this"
        else:
            return names[0] + ", " + names[1] + " and " + str((sum(res) - 2)) + " others like this"
    else:
        return "no one likes this"


# TASK - Create Phone Number

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in
# the form of a phone number.

def create_phone_number(n):
    n_string = "".join(str(x) for x in n)
    return "(" + n_string[:3] + ") " + n_string[3:6] + "-" + n_string[6:]


# TASK - Stop gninnipS My sdroW!

# Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters
# and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    sentence_list = sentence.split()
    resulted_list = []
    for word in sentence_list:
        if len(word) >= 5:
            resulted_list.append(word[::-1])
        else:
            resulted_list.append(word)

    return " ".join(resulted_list)


# TASK - Bit Counting

# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
# representation of that number. You can guarantee that input is non-negative.

def count_bits(n):
    bin_num = [int(i) for i in list('{0:0b}'.format(n))]
    return sum(bin_num)


# TASK - Sum of two lowest positive integers

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
# integers. No floats or non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    res = []
    for i in range(2):
        m = min(numbers)
        res.append(m)
        numbers.remove(m)
    return sum(res)


# TASK - Two to One

# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible,
# containing distinct letters.

def longest(s1, s2):
    return "".join(sorted(set(s1 + s2)))


# TASK - Is this a triangle?

# Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built
# with the sides of given length and false in any other case.

def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and a + c > b:
            return True
        else:
            return False
    else:
        return False


# TASK - Credit Card Mask

# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most
# secret question is still correct. However, since someone could look over your shoulder, you don't want that shown
# on your screen. Instead, we mask it.

def maskify(cc):
    mask = "".join(["#" for i in range(len(str(cc[:-4])))])
    return cc.replace(cc[:-4], mask)


# TASK - Printer Errors

# n a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for
# the sake of simplicity, are named with letters from a to m. Sometimes there are problems: lack of colors, technical
# malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

def printer_error(s):
    let_ascii = []
    res = []
    for i in string.ascii_lowercase[:13]:
        let_ascii.append(i)
    for i in s:
        if i not in let_ascii:
            res.append(1)
    return str(sum(res)) + "/" + str(len(s))


# TASK - Regex validate PIN code

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or
# exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        l = []
        for i in pin:
            if i.isdigit():
                l.append(1)
            else:
                l.append(0)
        if sum(l) == len(pin):
            return True
        else:
            return False
    else:
        return False


# TASK - Binary Addition

# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done
# before, or after the addition.
# The binary number returned should be a string.

def add_binary(a, b):
    return str(bin(a + b)[2:])


# TASK - Sum of odd numbers

# Given the triangle of consecutive odd numbers. Calculate the row sums of this triangle from the row index
# (starting at index 1)

def row_sum_odd_numbers(n):
    l = []
    for i in range(1, 1000000):
        if i % 2 != 0:
            l.append(i)
    sum_l = []
    for i in range(1, n):
        sum_l.append(i)
    return sum(l[sum(sum_l): sum(sum_l) + n])


# TASK - Friend or Foe?

# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can
# be sure he's not...

def friend(x):
    return list(i for i in x if len(i) == 4)


# TASK - Categorize New Members

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club,
# handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
    l = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            l.append("Senior")
        else:
            l.append("Open")
    return l


# TASK - Ones and Zeros

# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

def binary_array_to_number(arr):
    return int(str(''.join(map(str, arr))), 2)


# TASK - Find the divisors!

# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's
# divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the
# string '(integer) is prime'

def divisors(integer):
    l = []
    for n in range(2, integer):
        if integer % n == 0:
            l.append(n)
    if l == []:
        return str(integer) + " is prime"
    return l


# TASK - Find The Parity Outlier

# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a
# single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    o_l = []
    e_l = []
    for n in integers:
        if n % 2 == 0:
            e_l.append(n)
        else:
            o_l.append(n)
    if len(e_l) > len(o_l):
        return o_l[0]
    else:
        return e_l[0]


# TASK - Array.diff

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns
# the result. It should remove all values from list a, which are present in list b.

def array_diff(a, b):
    l = []
    for i in a:
        if i not in b:
            l.append(i)
    return l


# TASK - Counting Duplicates

# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    count = set()
    for e in text.lower():
        if text.lower().count(e) > 1:
            count.add(e)
    return len(count)


# TASK - Simple Pig Latin

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation
# marks untouched.

def pig_it(text):
    l = []
    t_split = text.split()
    punctuation = [".", "!", ",", "?"]
    for word in t_split:
        if word not in punctuation :
            l.append(word[1:] + word[0] + "ay")
        else:
            l.append(word)
    return " ".join(l)


# TASK - Human Readable Time

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
# format (HH:MM:SS)
#
#     HH = hours, padded to 2 digits, range: 00 - 99
#     MM = minutes, padded to 2 digits, range: 00 - 59
#     SS = seconds, padded to 2 digits, range: 00 - 59
#
# The maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    hh = int(seconds / 3600)
    mm = int(((seconds - (hh * 3600)) / 60))
    ss = seconds - ((hh * 3600) + (mm * 60))
    if seconds < 60:
        if len(str(seconds)) == 1:
            return "00:00:0" + str(seconds)
        else:
            return "00:00:" + str(seconds)
    elif seconds in range(60, 3600):
        if seconds == 60:
            return "00:01:00"
        else:
            mm = int(seconds / 60)
            ss = seconds - (mm * 60)
            if len(str(mm)) == 1:
                mm_f = "0" + str(mm)
            else:
                mm_f = str(mm)
            if len(str(ss)) == 1:
                ss_f = "0" + str(ss)
            else:
                ss_f = str(ss)
            return "00:" + mm_f + ":" + ss_f

    else:
        if len(str(hh)) == 1:
            hh_f = "0" + str(hh)
        else:
            hh_f = str(hh)
        if len(str(mm)) == 1:
            mm_f = "0" + str(mm)
        else:
            mm_f = str(mm)
        if len(str(ss)) == 1:
            ss_f = "0" + str(ss)
        else:
            ss_f = str(ss)
        return hh_f + ":" + mm_f + ":" + ss_f


# TASK - Moving Zeros To The End

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
# elements.

def move_zeros(array):
    l_one = []
    l_two = []
    for i in array:
        if i == 0 and not isinstance(i, bool):
            l_two.append(0)
        else:
            l_one.append(i)
    return l_one + l_two


# TASK - Valid Parentheses

# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.

def valid_parentheses(string):
    p_list = []
    for p in string:
        if p == "(" or p == ")":
            p_list.append(p)
    if string == "":
        return True
    else:
        if len(p_list) % 2 == 0:
            res = 0
            res_l = []
            for p in p_list:
                if p == "(":
                    res += 1
                else:
                    res -= 1

                res_l.append(res)
            print(res_l)
            count = 0
            for i in res_l:
                if i < 0:
                    count += 1

            if count > 0:
                return False
            else:
                if res_l[-1] == 0:
                    return True
                else:
                    return False
        else:
            return False


# TASK - RGB To Hex Conversion

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

def rgb(r, g, b):
    rgb_l = [r, g, b]
    res_l = []
    for c in rgb_l:
        if c <= 0:
            res_l.append("00")
        else:
            if c > 255:
                res_l.append(hex(255).upper()[2:])
            else:
                res_l.append(hex(c).upper()[2:])
    r_l = []
    for i in res_l:
        if len(i) == 1:
            r_l.append("0" + i)
        else:
            r_l.append(i)

    return r_l[0] + r_l[1] + r_l[2]


# TASK - Directions Reduction - NOT WORKING! TO BE CHECKED LATER!

def dirReduc(arr):

    for i in range(len(arr)):
        count = 0
        for direction in range(len(arr)-1):
            if arr[count] == "NORTH" and arr[count + 1] == "SOUTH":
                arr.remove(arr[count])
                arr.remove(arr[count + 1])
                arr.append(0)
                arr.append(0)
            elif arr[count] == "SOUTH" and arr[count + 1] == "NORTH":
                arr.remove(arr[count])
                arr.remove(arr[count + 1])
                arr.append(0)
                arr.append(0)
            elif arr[count] == "EAST" and arr[count + 1] == "WEST":
                arr.remove(arr[count])
                arr.remove(arr[count + 1])
                arr.append(0)
                arr.append(0)
            elif arr[count] == "WEST" and arr[count + 1] == "EAST":
                arr.remove(arr[count])
                arr.remove(arr[count + 1])
                arr.append(0)
                arr.append(0)
            count += 1

    return arr

# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# u=["NORTH", "WEST", "SOUTH", "EAST"]
# print(dirReduc(a))


# TASK - Where my anagrams at?

# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an
# array with words. You should return an array of all the anagrams or an empty array if there are none.

def anagrams(word, words):
    word_dict = {}
    for l in word:
        word_dict[l] = word.count(l)

    res_list = []
    for anagram in words:
        words_dict = {}
        for letter in anagram:
            words_dict[letter] = anagram.count(letter)

        if len(word) == len(anagram):
            isequal = word_dict == words_dict
            if isequal:
                res_list.append(anagram)

    return res_list


# TASK - Rot13

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
# characters included in the string, they should be returned as they are. Only letters from the latin/english
# alphabet should be shifted, like in the original Rot13 "implementation".

def rot13(message):
    l = [i for i in string.ascii_letters]
    res = []
    for i in message:
        if i.islower():
            if i in l[:27]:
                if 26 - l.index(i) <= 13:
                    res.append(l[13 - (26 - l.index(i))])
                else:
                    res.append(l[l.index(i) + 13])
        else:
            if i in l[26:]:
                if 52 - l.index(i) <= 13:
                    res.append(l[26 + (13 - (52 - l.index(i)))])
                else:
                    res.append(l[l.index(i) + 13])
            else:
                res.append(i)
    return "".join(res)


# TASK - Calculating with Functions
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by
# in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:


def zero(x=None):
    if not x:
        return 0
    else:
        return x(0)

def one(x=None):
    if not x:
        return 1
    else:
        return x(1)

def two(x=None):
    if not x:
        return 2
    else:
        return x(2)

def three(x=None):
    if not x:
        return 3
    else:
        return x(3)

def four(x=None):
    if not x:
        return 4
    else:
        return x(4)

def five(x=None):
    if not x:
        return 5
    else:
        return x(5)

def six(x=None):
    if not x:
        return 6
    else:
        return x(6)

def seven(x=None):
    if not x:
        return 7
    else:
        return x(7)

def eight(x=None):
    if not x:
        return 8
    else:
        return x(8)

def nine(x=None):
    if not x:
        return 9
    else:
        return x(9)

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: int(x / y)


# TASK - Duplicate Encoder

# The goal of this exercise is to convert a string to a new string where each character in the new string
# is "(" if that character appears only once in the original string, or ")" if that character appears more
# than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    word_l = word.lower()
    l = []
    for e in word_l:
        print(e)
        if word_l.count(e) > 1:
            l.append(")")
        else:
            l.append("(")
    return "".join(l)


# TASK - Take a Ten Minute Walk

# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too
# early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides
# its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an
# array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only
# a single block for each letter (direction) and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes
# (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

def is_valid_walk(walk):
    n_count = walk.count("n")
    s_count = walk.count("s")
    w_count = walk.count("w")
    e_count = walk.count("e")
    if len(walk) == 10:
        if n_count == s_count and w_count == e_count:
            return True
        else:
            return False
    else:
        return False


# TASK - Unique In Order

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
# any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    l = [i for i in iterable]
    count = 1
    if len(l) == 0:
        return []
    else:
        res_l = [l[0]]
        temp = l[0]
        for i in range(len(l) - 1):
            if l[count] == temp:
                count += 1
            else:
                res_l.append(l[count])
                temp = l[count]
                count += 1
        return res_l


# TASK - Abbreviate a Two Word Name

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    return "{}.{}".format(name.split()[0][0].upper(), name.split()[1][0].upper())


# TASK - Beginner - Lost Without a Map

# Given an array of integers, return a new array with each value doubled.

def maps(a):
    return [(i + i) for i in a]


# TASK - Count of positives / sum of negatives

# Return an array, where the first element is the count of positives numbers and the second element is sum of
# negative numbers.

def count_positives_sum_negatives(arr):
    count_pos = 0
    count_neg = 0
    if len(arr) == 0:
        return []
    else:
        for i in arr:
            if i > 0:
                count_pos += 1
            else:
                count_neg += i
        return [count_pos, count_neg]


# TASK - Invert values

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives
# become positives.

def invert(lst):
    res_l = []
    if len(lst) == 0:
        return []
    else:
        for i in lst:
            if i > 0:
                res_l.append(i * -1)
            else:
                res_l.append(abs(i))
    return res_l


# TASK - Count the Monkeys!

#unique_in_orderYou take your son to the forest to see the monkeys. You know that there are a certain number
# there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

def monkey_count(n):
    return [int(i) for i in range(1, n + 1)]


# TASK - You Can't Code Under Pressure #1

# Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    return i * 2


# TASK - Calculate average

# Write function avg which calculates average of numbers in given list.

def find_average(num):
    return int(sum(num) / len(num))


# TASK - Fake Binary

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return
# the resulting string.

def fake_bin(x):
    res_l = []
    for i in x:
        if int(i) < 5:
            res_l.append("0")
        else:
            res_l.append("1")
    return "".join(res_l)


# TASK - Count the Digit

# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. Square all numbers k (0 <= k <= n)
# between 0 and n. Count the numbers of digits d used in the writing of all the k**2. Call nb_dig (or nbDig or ...)
# the function taking n and d as parameters and returning this count.

def nb_dig(n, d):
    count = 0
    l = []
    for i in range(n + 1):
        l.append(i ** 2)

    for i in l:
        c = [int(l) for l in str(i)].count(d)
        count += c

    return count


# TASK - Make a function that does arithmetic!

# Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers
# having that operator used on them.

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b


# TASK - Your order, please

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the
# position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

import string

def order(sentence):
    l_dig = []
    l = sentence.split()
    for i in l:
        for k in i:
            if k in string.digits:
                l_dig.append(k)
    r_dict = dict(zip(l, l_dig))
    res_dirt = {k: v for k, v in sorted(r_dict.items(), key=lambda item: item[1])}
    res_l = []
    for i in res_dirt.keys():
        res_l.append(i)
    return " ".join(res_l)


# TASK - IQ Test

# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given
# numbers differs from the others. Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different
# in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start
# from 1 (not 0)

def iq_test(numbers):
    l = []
    for i in numbers.split():
        l.append(int(i))
    c_odd = 0
    c_even = 0
    for i in l:
        if i % 2 == 0:
            c_even += 1
        else:
            c_odd += 1
    if c_even > c_odd:
        for i in l:
            if i % 2 != 0:
                return l.index(i) + 1
    else:
        for i in l:
            if i % 2 == 0:
                return l.index(i) + 1


# TASK - Playing with digits

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find
# a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is
# equal to k * n.

def dig_pow(n, p):
    res_l = []
    l = [int(i) for i in str(n)]
    for i in l:
        res_l.append(i ** p)
        p += 1
    if sum(res_l) % n == 0:
        return int(sum(res_l) / n)
    else:
        return -1


# TASK - Beginner Series #2 Clock

# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make 'Past' function which returns time converted to milliseconds.

def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)


# TASK - Do I get a bonus?

# Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.
# If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money
# and must receive only his stated salary.

def bonus_time(salary, bonus):
    return f"${salary * 10}" if bonus else f"${salary}"


# TASK - Are You Playing Banjo?

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

def areYouPlayingBanjo(name):
    return f"{name} plays banjo" if name.lower()[0] == "r" else f"{name} does not play banjo"


# TASK - DNA to RNA Conversion

# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic 
# acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
#Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure 
# and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
#Create a function which translates a given DNA string into RNA.

def dna_to_rna(dna):
    return "".join(["U" if i == "T" else i for i in dna])


# TASK - Get the mean of an array

# Return the average of the given array rounded down to its nearest integer.

def get_average(marks):
    return int(sum(marks) / len(marks))


# TASK - Returning Strings

# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> 
# how are you doing today?".

def greet_2(name):
    return f"Hello, {name} how are you doing today?"


# TASK - Sum Arrays

# Write a method sum (sum_array in python, sumarray in julia, SumArray in C#) that takes an array of numbers and returns 
# the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers 
# can also be negative. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    return 0 if len(a) == 0 else sum(a)


# TASK - You only need one - Beginner

# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

def check(seq, elem):
    return True if elem in seq else False


# TASK - Total amount of points

# Our football team finished the championship. The result of each match look like "x:y". Results of all matches 
# are recorded in the collection.

def points(games):
    count = 0
    for game in games:
        if int(game[0]) > int(game[2]):
            count += 3
        elif int(game[0]) == int(game[2]):
            count += 1
    return count


# TASK - Array plus array

# I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll 
# appreciate for your help.

def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


# TASK - Find Maximum and Minimum Values of a List

# Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector 
# of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


# TASK - Sort Numbers

# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty 
# array or null/nil value then it should return an empty array.

def solution_4(nums):
    if nums:
        nums.sort()
        return nums
    else:
        return []


# TASK - Two Oldest Ages

# The two oldest ages function/method needs to be completed. It should take an array of numbers as its 
# argument and return the two highest numbers within the array. The returned value should be an array 
# in the format [second oldest age, oldest age]. 

def two_oldest_ages(ages):
    a = []
    for i in range(2):
        a.append(max(ages))
        ages.remove(max(ages))
    return sorted(a)


# TASK - Maximum Length Difference

# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x 
# be any string in the first array and y be any string in the second array.
#Find max(abs(length(x) − length(y)))
# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

def mxdiflg(a1, a2):
    l_1 = [len(i) for i in a1]
    l_2 = [len(i) for i in a2]
    if len(l_1) == 0:
        return -1
    elif len(l_2) == 0:
        return -1
    else:
        x = abs(max(l_1) - min(l_2))
        y = abs(max(l_2) - min(l_1))
        if x > y:
            return x
        else:
            return y


# TASK - Reversed Words

# Complete the solution so that it reverses all of the words within the string passed in. 

def reverseWords(s):
    return " ".join(s.split()[::-1])


# TASK - Sum without highest and lowest number

# Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest 
# element (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge, even if there are more than one 
# with the same value!)

def sum_array_1(arr):
    if arr and len(arr) > 1:
        return sum(arr) - max(arr) - min(arr)
    else:
        return 0


# TASK - Find the capitals

# Write a function that takes a single string (word) as argument. The function must return an ordered list 
# containing the indexes of all capital letters in the string.

def capitals(word):
    count = 0
    l = []
    for i in word:
        if i.isupper():
            l.append(count)
        count += 1
    return l


# TASK - Are the numbers in order?

# In this Kata, your function receives an array of integers as input. Your task is to determine whether the numbers 
# are in ascending order. An array is said to be in ascending order if there are no two adjacent integers where 
# the left integer exceeds the right integer in value.

def in_asc_order(arr):
    a = sorted(arr)
    if arr == a:
        return True
    else:
        return False


# TASK - Sort array by string length

# Write a function that takes an array of strings as an argument and returns a sorted array containing the 
# same strings, ordered from shortest to longest.

def sort_by_length(arr):
    d = {}
    for i in arr:
        d[i] = len(i)
    s_d = sorted(d.items(), key=lambda x: x[1])
    res_l = []
    for i in s_d:
        res_l.append(i[0])
    return res_l


# TASK - Remove anchor from URL

# Complete the function/method so that it returns the url with anything after the anchor (#) removed. 

def remove_url_anchor(url):
    return url[:url.index("#")] if "#" in url else url           


# TASK - How good are you really?

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!

def better_than_average(class_points, your_points):
    return sum(class_points) / len(class_points) < your_points


# TASK - Beginner - Reduce but Grow

# Given a non-empty array of integers, return the result of multiplying the values together in order.

def grow(arr):
    s = 1
    for i in arr:
        s *= i
    return s


# TASK - Count by X

# Create a function with two arguments that will return an array of the first (n) multiples of (x).
# Assume both the given number and the number of times to count will be positive numbers greater than 0. 

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# TASK - Will you make it?

# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel 
# is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles 
# per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is 
# possible to get to the pump or not. Function should return true (1 in Prolog) if it is possible and false 
# (0 in Prolog) if not. The input values are always positive.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


# TASK - If you can't sleep, just count sheep!!

# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input 
# will always be valid, i.e. no negative integers.

def count_sheep(n):
    return "".join([f"{i} sheep..." for i in range(1, n + 1)])


# TASK - Volume of a Cuboid

# Bob needs a fast way to calculate the volume of a cuboid with three values: length, width and the height of the cuboid. 
# Write a function to help Bob with this calculation.

def getVolumeOfCubiod(length, width, height):
    return length * width * height


# TASK - Sentence Smash

# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, 
# there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    return " ".join(words)


# TASK - Transportation on vacation 

# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes 
# you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. 
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

def rental_car_cost(d):
    if d in range(3, 7):
        return d * 40 - 20
    elif d >= 7:
        return d * 40 - 50
    else:
        return d * 40


# TASK - Pete, the baker

# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns 
# the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of 
# flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

def cakes(recipe, available):
    d = {}
    for k in recipe.keys():
        if k in available.keys():
            for k_r in recipe.keys():
                for k_a in available.keys():
                    if k_r == k_a:
                        d[k_r] = int(available[k_a] / recipe[k_r])
        else:
            d[k] = 0
    print(d)
    return min(d.values())


# TASK - The Hashtag Generator

# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.


def generate_hashtag(s):
    l = ["#"]
    if len(s) > 0:
        for i in s.split():
                l.append(i.capitalize())
        if len("".join(l)) >= 140:
            return False
        else:
            return "".join(l)
    else:
        return False


# TASK - The Coupon Code

# Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
# A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this 
# format: "MONTH DATE, YEAR".

import calendar
import time
import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    c = {month: index for index, month in enumerate(calendar.month_abbr) if month}
    current_date_formatted = f"{c[current_date.split()[0][:3]]}:{current_date.split()[1][:-1]}:{current_date.split()[2]}"
    current_date_timestamp = time.mktime(datetime.datetime.strptime(current_date_formatted, "%m:%d:%Y").timetuple())
    expiration_date_formatted = f"{c[expiration_date.split()[0][:3]]}:{expiration_date.split()[1][:-1]}:{expiration_date.split()[2]}"
    expiration_date_timestamp = time.mktime(datetime.datetime.strptime(expiration_date_formatted, "%m:%d:%Y").timetuple())
    
    if entered_code is correct_code:
        if current_date_timestamp <= expiration_date_timestamp:
            return True
        else:
            return False
    else:
        return False


# TASK - Sum of numbers from 0 to N

# We want to generate a function that computes the series starting from 0 and ending until the given number.

def show_sequence(n):
    l = [i for i in range(n + 1)]
    if n > 0:
        return "".join(str(i) + "+" for i in l)[:-1] + " = " + str(sum(l))
    elif n == 0:
        return "0=0"
    else:
        return f"{str(n)}<0"


# TASK - Alternate capitalization

# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. 
# Index 0 will be considered even.
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
# The input will be a lowercase string with no spaces.

def capitalize(s):
    l = []
    l_1 = []
    l_2 = []
    for i in range(len(s)):
        if i % 2 != 0:
            l_1.append(s[i].lower())
        else:
            l_1.append(s[i].upper())
    for i in l_1:
        if i.islower():
            l_2.append(i.upper())
        else:
            l_2.append(i.lower())
    return ["".join(l_1), "".join(l_2)]


# TASK - Third Angle of a Triangle

# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.

def other_angle(a, b):
        return 180 - a - b


# TASK - Expressions Matter 

# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and 
# brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained


def expression_matter(a, b, c):
    l = [a, b, c]
    
    attmpt_1 = a * b * c
    attmpt_2 = (a + b) * c
    attmpt_3 = a * (b + c)
    attmpt_4 = a + b + c
    
    return max(attmpt_1, attmpt_2, attmpt_3, attmpt_4)


# TASK - Convert a string to an array

# Write a function to split a string and convert it into an array of words.

def string_to_array(s):
    return s.split() if len(s) > 0 else [""]
    

# TASK - Simple multiplication

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9


# TASK - A function within a function

# Given an input n, write a function always that returns a function which returns n. Ruby should return a lambda or a proc.

def always(n=0):
    def transmitter():
        return 1 * n
    return transmitter


# TASK - Convert a Number to a String!

# We need a function that can transform a number into a string.

def number_to_string(num):
    return "".join([i for i in str(num)])


# TASK - Replace With Alphabet Position

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

import string

def alphabet_position(text):
    res_l = []
    l_string = string.ascii_letters
    for i in text.lower():
        if i in l_string:
            res_l.append(str(l_string.index(i) + 1))
    return " ".join(res_l)


# TASK - Complementary DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with 
# one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand 
# is never empty or there is no DNA at all (again, except for Haskell).

def DNA_strand(dna):
    l = []
    for i in dna:
        if i == "A":
            l.append("T")
        elif i == "T":
            l.append("A")
        elif i == "G":
            l.append("C")
        else:
            l.append("G")
    return "".join(l)


# TASK - Convert string to camel case

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known 
# as Upper Camel Case, also often referred to as Pascal case). 

def to_camel_case(text):
    s = ""
    for i in text:
        if i == "_" or i == "-":
            s += " "
        else:
            s += i
    #s = "".join(l)
    print(s)

    res_l = []
    for i in s.split():
        if s.split().index(i) == 0:
            res_l.append(i)
        else:
            res_l.append(i.capitalize())
    return "".join(res_l)


# TASK - Find the next perfect square!

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer. 

import math

def find_next_square(sq):
    if int(math.sqrt(sq) + 0.5) ** 2 != sq:
        return -1
    else:
        num = sq + 1
        while int(math.sqrt(num) + 0.5) ** 2 != num:
            num += 1
        return num


# TASK - Format a string of names like 'Bart, Lisa & Maggie'.

# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, 
# which should be separated by an ampersand.

def namelist(names):
    l = []
    for i in names:
        l.append(i['name'])
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return f"{l[0]} & {l[1]}"
    elif len(l) > 2:
        return f"{', '.join(l[:-1])} & {l[-1]}"
    else:
        return ""


# TASK - Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters as input and that returns 
# the missing letter in the array.

import string

def find_missing_letter(chars):
    l = [i for i in string.ascii_letters]
    
    begin = [l.index(i) for i in l if i == chars[0]][0]
    end = [l.index(i) for i in l if i == chars[-1]][0]

    for i in l[begin:end + 1]:
        if i not in chars:
            return i


# TASK - Form The Minimum

# Given a list of digits, return the smallest number that could be formed from these digits, using the digits 
# only once (ignore duplicates). 

def min_value(digits):
    return int("".join(str(i) for i in list(sorted(dict.fromkeys(digits)))))


# TASK - Row Weights

# Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, 
# where the first one is the total weight of team 1, and the second one is the total weight of team 2.

def row_weights(array):
    if len(array) == 1:
        return (array[0], 0)
    elif len(array) == 2:
        return (array[0], array[1])
    else:
        left = int()
        right = int()
        count = 0
        for i in array:
            count += 1
            if count % 2 == 0:
                right += i
            else:
                left += i
            
        l = (left, right)
        return l


# TASK - Filling an array (part 1)

# Write a function that produces an array with the numbers 0 to N-1 in it.

def arr(n=0): 
    return [i for i in range(n)] if n > 0 else []


# TASK - A wolf in sheep's clothing

# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of 
# the queue which is at the end of the array.
# If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! 
# Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

def warn_the_sheep(queue):
    return f"Oi! Sheep number {(len(queue) - queue.index('wolf')) - 1}! You are about to be eaten by a wolf!" if queue.index('wolf') != (len(queue)-1) else 'Pls go away and stop eating my sheep'


# TASK - WeIrD StRiNg CaSe

# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word 
# lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

def to_weird_case(string):
    str_l = []
    for word in string.split():
        count = 1
        res_letter = ""
        for letter in word:
            if count % 2 != 0:
                res_letter += letter.upper()
            else:
                res_letter += letter.lower()
            count += 1
        str_l.append(res_letter)
    return " ".join(str_l)


# TASK - Roman Numerals Decoder

# Create a function that takes a Roman numeral as its argument and returns its value 
# as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

def solution65(roman):
    decoder = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = int()
    count = 0
    res_minus = int()

    for i in roman:
        result += decoder[i]

    for i in range(len(roman) - 1):
        if decoder[roman[count]] < decoder[roman[count + 1]]:
            res_minus += decoder[roman[count]] * 2
        count += 1

    return result - res_minus


# TASK - Sorted? yes? no? how?

# Complete the method which accepts an array of integers, and returns one of the following:
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise

def is_sorted_and_how(arr):
    c = 0
    l = []
    for i in range(len(arr) - 1):
        if (arr[c] - arr[c + 1]) < 0:
            l.append("ascending")
        else:
            l.append("descending")
        c += 1
    print(l)

    if "ascending" in l and "descending" in l:
        return "no"
    else:
        return f"yes, {l[0]}"


# TASK - Number Of Occurrences

# Write a function that returns the number of occurrences of an element in an array.

def number_of_occurrences(element, sample):
    count = 0
    for i in sample:
        if i == element:
            count += 1
    return count


# TASK - Power of two

# Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language)
# that determines if a given non-negative integer is a power of two.

def power_of_two(x):
    if (x == 0):
        return False
    while x != 1:
            if (x % 2 != 0):
                return False
            x = x // 2      
    return True


# TASK - Most digits

# Find the number with the most digits.
# If two numbers in the argument array have the same number of digits, return the first one in the array.

def find_longest(arr):
    l = []
    for i in arr:
        l.append(len(str(i)))
    return arr[l.index(max(l))]


# TASK - Flatten

# Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

def flatten(lst):
    l = []
    for i in lst:
        if len(str(i)) == 1:
            l.append(i)
        else:
            for e in i:
                l.append(e)
    return l


# TASK - Basic Sequence Practice

# Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained 
# above. Whenn < 0 return the sequence with negative terms.

def sum_of_n(n):
    res_l = []
    res = 0
    if n < 0:
        c = n * -1
        for i in range(c + 1):
            res += i
            res_l.append(res * -1)
    else:
        for i in range(n + 1):
            res += i
            res_l.append(res)
    return res_l


# TASK - Thinkful - String Drills: Repeater

# Write a function named repeater() that takes two arguments (a string and a number), and returns a new string where the 
# input string is repeated that many times.

def repeater(string, n):
    return string * n


# TASK - Leap Years

# In this kata you should simply determine, whether a given year is a leap year or not

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


# TASK - Flatten and sort an array

# Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the 
# sorted (ascending) order.

def flatten_and_sort(array):
    res = []
    for i in array:
        for e in i:
            res.append(e)
    return sorted(res)


# TASK - Number to digit tiers

# Create a function that takes a number and returns an array of strings containing the number cut off at each digit.

def create_array_of_tiers(n):
    res = []
    for i in range(len(str(n))):
        res.append(str(n)[:i + 1])
    return res


# TASK - How sexy is your name?

# How sexy is your name? Write a program that calculates how sexy one's name is according to the criteria below.

def sexy_name(name):
    scores = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
              'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
              'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
              'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}
    score = 0
    for i in name:
        if i != " ":
            score += scores[i.upper()]
        else:
            score += 0

    if score <= 60:
        return "NOT TOO SEXY"
    elif score in range(61, 301):
        return "PRETTY SEXY"
    elif score in range(301, 600):
        return "VERY SEXY"
    else:
        return "THE ULTIMATE SEXIEST"


# TASK - Who Took The Car Key?

# Given an array of binary numbers, figure out and return the culprit's message to find out who took the missing car key.

def who_took_the_car_key(message):
    res = []
    res_l = []
    for i in message:
        res_l.append(int(i, 2))
    for i in res_l:
        res.append(chr(i))
    return "".join(res)


# TASK - Filter Long Words

# Write a function filter_long_words that takes a string sentence and an integer n.
#Return a list of all words that are longer than n.

def filter_long_words(sentence, n):
    return [i for i in sentence.split() if len(i) > n]


# TASK - JavaScript Array Filter

# In Python, there is a built-in filter function that operates similarly to JS's filter. For more information on how to use this function, 
# visit https://docs.python.org/3/library/functions.html#filter

def get_even_numbers(arr):
    return [i for i in arr if i % 2 == 0]


# TASK - Caffeine Script

# Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.
# If the integer is divisible by 3, return the string "Java".
# If the integer is divisible by 3 and divisible by 4, return the string "Coffee"
# If the integer is one of the above and is even, add "Script" to the end of the string.
# Otherwise, return the string "mocha_missing!"

def caffeine_buzz(n):
    if n % 3 == 0:
        if n % 4 == 0:
            if n % 2 == 0:
                return "CoffeeScript"
            else:
                return "Coffee"
        elif n % 2 == 0:
            return "JavaScript"
        else:
            return "Java"
    else:
        return "mocha_missing!"


# TASK - Boiled Eggs

# Implement a function, which takes a non-negative integer, representing the number of 
# eggs to boil. It must return the time in minutes (integer), which it takes to have all the eggs boiled.

def cooking_time(eggs):
    pot_capacity = eggs // 8
    if eggs % 8 == 0:
        return pot_capacity * 5
    else:
        return (pot_capacity + 1) * 5


# TASK - Parts of a list

# Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.

def partlist(arr):
    res = []
    count = 1
    for i in range(len(arr) - 1):
        res_one = " ".join(arr[:count])
        res_two = " ".join(arr[count:])
        res_final = (res_one, res_two)
        res.append(res_final)
        count += 1
    return res


# TASK - Area of a Circle

# Complete the function circleArea so that it will return the area of a circle with the given radius. Round the returned number 
# to two decimal places (except for Haskell). If the radius is not positive or not a number, return false.

import math

def circle_area(r):
    if not isinstance(r, str):
        if r > 0:
            return round(math.pi * r ** 2, 2)
        else:
            return False
    else:
        return False


# TASK - Complete The Pattern #1 

# You have to write a function pattern which returns the following Pattern(See Pattern & Examples) upto n number of rows. 

def pattern(n):
    res = []
    for i in range(1, n + 1):
        res.append(str(i) * i)
    return "\n".join(res)


# TASK - Mexican Wave

# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a 
# string and you must return that string in an array where an uppercase letter is a person standing up. 

def wave(people):
    res = []
    for i in range(len(people)):
        if i == 0:
            res.append(people[0].upper() + people[1:])
        elif i == len(people) - 1:
            res.append(people[:len(people) - 1] + people[-1].upper())
        else:
            res.append(people[:i] + people[i].upper() + people[i + 1:])
    for i in range(len(people)):
        if people in res:
            res.remove(people)
    return res


# TASK - Extract the domain name from a URL

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

def domain_name(url):
    res = []
    for i in url.split("."):
        res.append(i)
    if "www" in url:
        return res[1]
    elif "//" in url:
        return res[0][res[0].find("//") + 2:]
    else:
        return res[0]