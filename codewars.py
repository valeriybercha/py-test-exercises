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


# TASK - Simple Fun #1: Seats in Theater

# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the 
# row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the 
# left, assuming all seats are occupied.

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_rows - row) * (tot_cols - col + 1)


# TASK - Sort and Star

# You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) 
# and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.

def two_sort(array):
    return "***".join([i for i in sorted(array)[0]])


# TASK - Surface Area and Volume of a Box

# Write a function that returns the total surface area and volume of a box as an array: [area, volume]

def get_size(w,h,d):
    return [(2 * w * h + 2 * h * d + 2 * w * d), (w * h * d)]


# TASK - Dollars and Cents

# 39.99 becomes $39.99

def format_money(amount):
    if isinstance(amount, int):
        return f"${amount}.00"
    else:
        if str(amount)[-2] == ".":
            return f"${round(amount, 2)}0"
        else:
            return f"${round(amount, 2)}"
    

# TASK - Reverse List Order

# In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
  return l[::-1]


# TASK - Grasshopper - Debug

# Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. 
# Unfortunately his code has some bugs.

def weather_info (temp):
    c = convert_to_celsius(temp)
    if c < 0:
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert_to_celsius(temperature):
    var_celsius = (temperature - 32) * (5/9)
    return var_celsius


# TASK - Sleigh Authentication

# Your task is to implement the authenticate() method of the sleigh, which takes the name of the person, who wants to 
# board the sleigh and a secret password. If, and only if, the name equals "Santa Claus" and the password is 
# "Ho Ho Ho!" (yes, even Santa has a secret password with uppercase and lowercase letters and special characters :D), 
# the return value must be true. Otherwise it should return false.
 
class Sleigh(object):
    
    def authenticate(self, name, password):
        if ("Santa" or "Clause") in name:
            if "Ho" in password:
                if name == "Santa Claus" and password == "Ho Ho Ho!":
                    return True
                else:
                    return False
        else:
            return False


# TASK - Well of Ideas - Easy Version

# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are 
# one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no 
# good ideas, as is often the case, return 'Fail!'.

def well(x):
    count = 0
    for i in x:
        if i == "good":
            count += 1
    if count > 2:
        return "I smell a series!"
    elif count in range(1, 3):
        return "Publish!"
    else:
        return "Fail!"


# TASK - Student's Final Grade

# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a 
# grade for the exam and a number of completed projects.

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
            return 100
    elif exam in range(76, 91):
        if projects in range(2, 5):
            return 75
        elif projects in range(5, 11):
            return 90
        else:
            return 0
    elif exam in range(51, 76):
        if projects in range(2, 11):
            return 75
        else:
            return 0
    else:
        return 0


# TASK - Elapsed Seconds

# Complete the function so that it returns the number of seconds that have elapsed between the start and end times given. 

from datetime import datetime

def elapsed_seconds(start, end):
    s = start.timetuple()
    e = end.timetuple()
    return ((e[0] - s[0]) * 31536000) + ((e[1] - s[1]) * 2592000) + ((e[2] - s[2]) * 86400) + ((e[3] - s[3]) * 3600) + ((e[4] - s[4]) * 60) + (e[5] - s[5])


# TASK - Refactored Greeting

# Refactor the following code so that it belongs to a Person class/object. Each Person instance will have a greet 
# method. The Person instance should be instantiated with a name so that it no longer has to be passed into each greet method call. 

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)


# TASK - Grasshopper - Debug sayHello

#The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It 
# is your job to fix the code and get the program working again!

def say_hello(name):
    return f"Hello, {name}"


# TASK - Function 2 - squaring an argument

# Now you have to write a function that takes an argument and returns the square of it.

def square(n):
    return n * n


# TASK - Will there be enough space?

# You have to write a function that accepts three parameters:
# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus.
# wait is the number of people waiting to get on to the bus.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    return 0 if on + wait <= cap else (on + wait) - cap


# TASK - Area or Perimeter

# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

def area_or_perimeter(l , w):
    return l * w if l == w else l * 2 + w * 2


# TASK - Grasshopper - If/else syntax debug

# While making a game, your partner, Greg, decided to create a function to check if the user is still alive called 
# checkAlive/CheckAlive/check_alive. Unfortunately, Greg made some errors while creating the function.

def check_alive(health):
    return health > 0


# TASK - Squash the bugs

# Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. 
# Output should be the length of the longest word, as a number.

def find_longest(string):
    spl = string.split()
    print(spl)
    longest = 0
    i=0
    while i < len(spl):
        if (len(spl[i]) > longest): longest = len(spl[i])
        i += 1
    return longest


# TASK - Regular Ball Super Ball

# Create a class Ball.
# Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


# TASK - Round up to the next multiple of 5

# Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?

def round_to_next5(n):
    count = n
    for i in range(n, n + 100):
        if count % 5 == 0:
            return count
            break
        else:
            count += 1


# TASK - Find the middle element

# As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical 
# element that lies between the other two elements.

def gimme(input_array):
    l = [max(input_array), min(input_array)]
    return [input_array.index(i) for i in input_array if i not in l][0]


# TASK - Building Strings From a Hash

# Complete the solution so that it takes the object (JavaScript/CoffeeScript) or hash (ruby) passed in and generates a human 
# readable string from its key/value pairs.
# The format should be "KEY = VALUE". Each key/value pair should be separated by a comma except for the last pair.

def solution(pairs):
    l = []
    for k, v in pairs.items():
        l.append(f"{k} = {v}")
    return ",".join(sorted(l))


# TASK - Greet Me

# Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

def greet(name): 
    return f"Hello {name.title()}!"


# TASK - Predict your age!

# My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    l = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    res_l = []
    for i in l:
        res_l.append(i * i)
    return int(math.sqrt(sum(res_l)) // 2)


# TASK - Fix string case

# n this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert 
# that string to either lowercase only or uppercase only based on:
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

def solve(s):
    upper = 0
    lower = 0
    for i in s:
        if i.islower():
            lower += 1
        else:
            upper += 1
    if upper > lower:
        return s.upper()
    elif upper < lower:
        return s.lower()
    else:
        return s.lower()


# TASK - Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

# The number 89 is the first integer with more than one digit that fulfills the property partially introduced 
# in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

def sum_dig_pow(a, b):
    print(a, b)
    res_l = []
    for i in range(a, b + 1):
        bp = [int(b) for b in str(i)]
        bp_res = 0
        count = 1
        for a in bp:
            bp_res += (a ** count)
            count += 1
        if i == bp_res:
            res_l.append(i)
    return res_l


# TASK - Count characters in your string

# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the 
# result should be {'a': 2, 'b': 1}.

def count(string):
    res_dict = {}
    for i in string:
        res_dict[i] = string.count(i)
    return res_dict


# TASK - CamelCase Method

# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. 
# All words must have their first letter capitalized without spaces.

def camel_case(string):
    l = []
    for i in string.split():
        l.append(i.capitalize())
    return "".join(l)


# TASK - Thinkful - Logic Drills: Traffic light

# You're writing code to control your town's traffic lights. You need a function to handle each change 
# from green, to yellow, to red, and then to green again.

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"


# TASK - Quarter of the year

# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4


# TASK - No zeros for heros

# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.

def no_boring_zeros(n):
    s = []
    if n == 0:
        return 0
    else:
        for i in str(n):
            s.append(i)
        c = -1
        if s[c] == "0":
            while s[c] == "0":
                c += -1
            r = str(n)
            return int(r[:c + 1])
        else:
            return n


# TASK - Filter out the geese

# Write a function, gooseFilter / goose-filter / goose_filter /GooseFilter, that takes an array of 
# strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    return [i for i in birds if i not in geese]


# TASK - Check the exam

# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The 
# second one contains a student's submitted answers.
# The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for 
# each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] != arr2[i]:
            if arr1[i] == "" or arr2[i] == "":
                score += 0
            else:
                score -= 1
    if score <= 0:
        return 0
    else:
        return score


# TASK - Get Nth Even Number

# Return the Nth Even Number

def nth_even(n):
    return 2 * (n - 1)


# TASK - Is this my tail?

# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the 
# right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same 
# as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

def correct_tail(body, tail):
    return body[-1] == tail


# TASK - Capitalization and Mutability

# Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works 
# as intended (i.e. make the first character in the string "word" upper case).

def capitalize_word(word):
    return word.capitalize()


# TASK - Plural

# We need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural 
# should be used with that number or false if not. This would be useful when printing out a string such as 5 minutes, 14 apples, 
# or 1 sun. 

def plural(n):
    return n != 1


# TASK - Grasshopper - Check for factor

# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.

def check_for_factor(base, factor):
    return base % factor == 0


# TASK - Grasshopper - Terminal game move function

# In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by 
# the dice two times.

def move(position, roll):
    return roll * 2 + position


# TASK - Holiday VIII - Duty Free

# The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the saving 
# over the normal high street price would effectively cover the cost of your holiday. 

def duty_free(price, discount, holiday_cost):
    return holiday_cost // ((price * ((discount / 100) + 1)) - price)


# TASK - 101 Dalmatians - squash the bugs, not the dogs!

# By repairing the function provided, you will find out exactly how you should respond, depending on the number of 
# dogs he has.

def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <= 10:
        return dogs[0]
    elif n <= 50:
        return dogs[1]
    elif n == 101:
        return dogs[3]
    else:
        return dogs[2]


# TASK - Palindrome Strings

# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. 
# This includes capital letters, punctuation, and word dividers.

def is_palindrome(string):
    rev = str(string)[::-1]
    return int(rev) == string if type(string) == int else rev == string


# TASK - get character from ASCII Value

# Write a function which takes a number and returns the corresponding ASCII char for that value

def get_char(c):
    return chr(c)


# TASK - Simple validation of a username with regex

# Write a simple regex to validate a username. Allowed characters are:
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

import re

def validate_usr(username):
    res = re.match("^[a-z0-9_]{4,16}$", username)
    if res:
        return True
    else:
        return False


# TASK - Grasshopper - Terminal game combat function

# Create a combat function that takes the player's current health and the amount of damage recieved, and returns 
# the player's new health. Health can't be less than 0.

def combat(health, damage):
    return 0 if (health - damage) < 0 else health - damage


# TASK - Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence

# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

def replace_exclamation(s):
    vowels = "aeiouAEIOU"
    res = []
    for i in s:
        if i in vowels:
            res.append("!")
        else:
            res.append(i)
    return "".join(res)


# TASK - To square(root) or not to square(root)

#To square(root) or not to square(root)
# Write a method, that will get an integer array as parameter and will process every number from this array.

import math

def square_or_square_root(arr):
    res = []
    for i in arr:
        if int(math.sqrt(i)) ** 2 == i:
            res.append(int(math.sqrt(i)))
        else:
            res.append(i ** 2)
    return res


# TASK - Printing Array elements with Comma delimiters

def print_array(arr):
    return f'{",".join(str(i) for i in arr)}'


# TASK - Sum of Triangular Numbers

# Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.

def sum_triangular_numbers(n):
    count = 0
    res = 0
    for i in range(1, n+1):
        count += i
        res += count
    return res


# TASK - Sum of Minimums!

# Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.

def sum_of_minimums(numbers):
    count = 0
    for i in numbers:
        count += min(i)
    return count


# TASK - Form The Largest 

# Given a number , Return _The Maximum number _ could be formed from the digits of the number given . 

def max_number(n):
    return int("".join(sorted(i for i in str(n))[::-1]))


# TASK - Cat years, Dog years

# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years, human_years * 15, human_years * 15]
    elif human_years == 2:
        return[human_years, 15 + 9, 15 + 9]
    else:
        return [human_years, 15 + 9 + ((human_years - 2) * 4), 15 + 9 + ((human_years - 2) * 5)]


# TASK - Remove duplicates from list

# Define a function that removes duplicates from an array of numbers and returns it as a result.
# The order of the sequence has to stay the same.

def distinct(seq):
    res_d = dict()
    for i in seq:
        res_d[i] = seq.count(i)
    res = []
    for i in res_d:
        res.append(i)
    return res


# TASK - L1: Bartender, drinks!

# Complete the function that receives as input a string, and produces outputs accordingly

def get_drink_by_profession(param):
    if param.title() == "Jabroni":
        return "Patron Tequila"
    elif param.title() == "School Counselor":
        return "Anything with Alcohol"
    elif param.title() == "Programmer":
        return "Hipster Craft Beer"
    elif param.title() == "Bike Gang Member":
        return "Moonshine"
    elif param.title() == "Politician":
        return "Your tax dollars"
    elif param.title() == "Rapper":
        return "Cristal"
    else:
        return "Beer"


# TASK - noobCode 01: SUPERSIZE ME.... or rather, this integer! 

# Write a function that rearranges an integer into its largest possible value. 

def super_size(n):
    return int("".join(sorted(str(n))[::-1]))


# TASK - Reversing Words in a String

# You need to write a function that reverses the words in a given string. A word can also fit an empty string.

def reverse(st):
    res = []
    l = st.split()
    for i in l:
        x = i.replace(" ", "")
        res.append(x)
    return " ".join(res[::-1])


# TASK - Basic Training: Add item to an Array

# Add the value "codewars" to the websites array.
# After your code executes the websites array should == ["codewars"]
# The websites array has already been defined for you

websites = []
websites.append("codewars")


# TASK - Swap Values

# I would like to be able to pass an array with two elements to my swapValues function to swap the values.
# However it appears that the values aren't changing.

def swap_values(args): 
    [args[0], args[1]] = [args[1], args[0]]


# TASK - Training JS #7: if..else and ternary operator

# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accept 1 parameters:n, n is 
# the number of customers to buy hotdogs, different numbers have different prices (refer to the following table), 
# return a number that the customer need to pay how much money.

def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    elif n >= 10:
        return n * 90


# TASK - 5 without numbers !!

# Write a function that always returns 5
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/

import math

def unusual_five():
    l = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "b"]
    return math.sqrt(len(l))


# TASK - Twice as old

# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

def twice_as_old(dad_years_old, son_years_old):
    return dad_years_old - son_years_old * 2 if (son_years_old * 2) < dad_years_old else son_years_old * 2 - dad_years_old


# TASK - Difference of Volumes of Cuboids

# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist 
# of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' 
# volumes regardless of which is bigger.

def find_difference(a, b):
    res_a = 1
    for i in a:
        res_a *= i
    res_b = 1
    for i in b:
        res_b *= i
    return res_a - res_b if res_a > res_b else res_b - res_a


# TASK - Hex to Decimal

# Complete the function which converts hex number (given as a string) to a decimal number.

def hex_to_dec(s):
    return int(s, 16)


# TASK - Kata Example Twist

# Add the value "codewars" to the array websites/Websites 1,000 times.

websites = []
for i in range(1000):
    websites.append("codewars")


# TASK - Smallest unused ID

# You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

def next_id(arr):
    if len(arr)> 0:
        l = [i for i in range(0, max(arr) + 1)]
        print(arr)
        print(l)
        res = []
        for i in l:
            if i not in arr:
                res.append(i)
            else:
                res.append(max(arr) + 1)
        return min(res)
    else:
        return 0
    

# TASK - Averages of numbers

# Get the averages of these numbers
# Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and 
# his follower, if there is one.

def averages(arr):
    if arr != None:
        if len(arr) > 1:
            c = 0
            res = []
            for i in range(len(arr) - 1):
                x = (arr[c] + arr[c + 1]) / 2
                if x == int(x):
                    res.append(int(x))
                else:
                    res.append(x)
                c += 1
            return res
        else:
            return []
    else:
        return []


# TASK - Find the nth Digit of a Number

# Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).

def find_digit(num, nth):
    if nth > 0:
        return int([i for i in str(abs(num))[::-1]][nth - 1]) if len(str(num)) >= nth else 0
    else:
        return -1


# TASK - Ordered Count of Characters

# Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty 
# output return an empty list.

def ordered_count(inp):
    res = []
    res_d = {}
    for i in inp:
        res_d[i] = inp.count(i)
    for i in res_d:
        res.append((i, res_d[i]))
    return res


# TASK - Making Copies

# Write a function that takes a list (in Python) or array (in other languages) of numbers, and makes a copy of it.

def copy_list(l):
    return [i for i in l]


# TASK - Vowel remover

# Create a function called shortcut to remove all the lowercase vowels in a given string.

def shortcut(s):
    vowels = ["a", "e", "i", "o", "u"]
    return "".join([i for i in s if i not in vowels])


# TASK - Determine offspring sex based on genes XX and XY chromosomes

# Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a son.' if "Y" in sperm else 'Congratulations! You\'re going to have a daughter.'


# TASK - Drink about

# Make a function that receive age, and return what they drink.
# Rules:
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.

def people_with_age_drink(age):
    if age <= 13:
        return "drink toddy"
    elif age in range(14, 18):
        return "drink coke"
    elif age in range (18, 21):
        return "drink beer"
    else:
        return "drink whisky"
    

# TASK - Find the Difference in Age between Oldest and Youngest Family Members

# You will be given an array of all the family members' ages, in any order. The ages will be given in whole numbers, so a baby 
# of 5 months, will have an ascribed ‘age’ of 0. Return a new array (a tuple in Python) with [youngest age, oldest age, difference
#  between the youngest and oldest age].

def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))


# TASK - Return the Missing Element

# Write a function that accepts a sequence of unique integers between 0 and 9 (inclusive), and returns the missing element. 

def get_missing_element(seq): 
    compare = [i for i in range(0, 10)]
    res = 0
    for i in compare:
        if i not in seq:
            res += i
        else:
            res += 0
    return res


# TASK - Simple beads count

# Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the 
# number of red beads.

def count_red_beads(n):
    if n <= 2:
        return 0
    else:
        return (n-1) * 2


# TASK - Digitize

# Given a non-negative integer, return an array / a list of the individual digits in order.

def digitize(n):
    return [int(i) for i in str(n)]


# TASK - Maximum Product

# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

def adjacent_element_product(array):
    res = []
    c = 0
    for i in range(len(array) - 1):
        res.append(array[c] * array[c + 1])
        c += 1
    return max(res)


# TASK - Remove the time

# You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was made:
# Weekday Month Day, time e.g., Friday May 2, 7pm
# Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.

def shorten_to_date(long_date):
    return " ".join(long_date.split()[:3])[:-1]


# TASK - Convert to Binary

# Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.

def to_binary(n):
    return int(bin(n)[2:])


# TASK - Thinkful - Dictionary drills: Order filler

# You've decided to write a function fillable() that takes three arguments: a dictionary stock representing all the 
# merchandise you have in stock, a string merch representing the thing your customer wants to buy, and an integer n representing 
# the number of units of merch they would like to buy. Your function should return True if you have the merchandise in stock to 
# complete the sale, otherwise it should return False.You've decided to write a function fillable() that takes three arguments: 
# a dictionary stock representing all the merchandise you have in stock, a string merch representing the thing your customer wants 
# to buy, and an integer n representing the number of units of merch they would like to buy. Your function should return True if 
# you have the merchandise in stock to complete the sale, otherwise it should return False.

def fillable(stock, merch, n): 
    if merch in stock.keys():
        if stock[merch] >= n:
            return True
        else:
            return False
    else:
        return False


# TASK - Name Shuffler

# Write a function that returns a string in which firstname is swapped with last name.

def name_shuffler(str_):
    return " ".join(str_.split()[::-1])


# TASK - Last

# Find the last element of the given argument(s).

def last(*args):
    res_l = []
    for i in args:
        res_l.append(i)
    if len(res_l) == 1:
        if type(res_l[0]) == int:
            return res_l[0]
        else:
            return res_l[0][-1]
    else:
        return args[-1]


# TASK - Substituting Variables Into Strings: Padded Numbers

# Complete the solution so that it returns a formatted string. The return value should equal "Value is VALUE" 
# where value is a 5 digit padded number. 

def solution(value):
    return f"Value is {'0' * (5 - len(str(value)))}" + str(value)


# TASK - Sum of array singles

# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only 
# twice. Your task will be to return the sum of the numbers that occur only once. 

def repeats(arr):
    count_list = []
    c = 0
    for i in range(len(arr)):
        count_list.append(arr.count(arr[c]))
        c += 1
    position_list = []
    p = 0
    for i in count_list:
        if i == 1:
            position_list.append(p)
        p += 1
    res_l = []
    for i in position_list:
        res_l.append(arr[i])
    return sum(res_l)


# TASK - Find the vowels

# We want to know the index of the vowels in a given word, for example, there are two vowels in the 
# word super (the second and fourth letters).

def vowel_indices(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    count = 1
    res = []
    for i in word:
        if i.lower() in vowels:
            res.append(count)
        count += 1
    return res


# TASK - Triple Trouble

# Create a function that will return a string that combines all of the letters of the three inputed 
# strings in groups. Taking the first letter of all of the inputs and grouping them next to each 
# other. Do this for every letter, see example below!

def triple_trouble(one, two, three):
    res = ""
    for i in range(len(one)):
        res += one[i]
        res += two[i]
        res += three[i]
    return res


# TASK - Super Duper Easy

# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is 
# a string it should return "Error".

def problem(a):
    return a * 50 + 6 if type(a) == int or type(a) == float else "Error"


# TASK - Thinkful - Number Drills: Pixelart planning

# Your function should take two arguments: the size of the wall in millimeters and the size of a 
# pixel in millimeters. It should return True if you can fit an exact number of pixels on 
# the wall, otherwise it should return False. For example is_divisible(4050, 27) should 
# return True, but is_divisible(4066, 27) should return False.

def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


# TASK - Grasshopper - Function syntax debugging

# A student was working on a function and made some syntax mistakes while coding. 
# Help them find their mistakes and fix them.

def main(verb, noun):
    return verb + noun


# TASK - Grasshopper - Basic Function Fixer

# I created this function to add five to any number that was passed in to it and return the new 
# value. It doesn't throw any errors but it returns the wrong number.

def add_five(num):
    total = num + 5
    return total


# TASK - Exclamation marks series #1: Remove a exclamation mark from the end of string

# Remove a exclamation mark from the end of string. For a beginner kata, you can assume 
# that the input data is always a string, no need to verify it.

def remove(s):
    if len(s) > 0:
        if s[-1] == "!":
            return s[:-1]
        else:
            return s
    else:
        return ""


# TASK - Bin to Decimal

# Complete the function which converts a binary number (given as a string) to a 
# decimal number.

def bin_to_decimal(inp):
    return int(inp, 2)


# TASK - Sum The Strings

# Create a function that takes 2 positive integers in form of a string as an input, and 
# outputs the sum (also as a string)

def sum_str(a, b):
    if a == "":
        if b == "":
            a = 0
            b = 0
            return str(a + b)
        else:
            a = 0
            return str(a + int(b))
    else:
        if b == "":
            b = 0
            return str(int(a) + int(b))
        else:
            return str(int(a) + int(b))


# TASK - Formatting decimal places #0

# Each number should be formatted that it is rounded to two decimal places. You don't need 
# to check whether the input is a valid number because only valid numbers are used in the tests.

def two_decimal_places(n):
    return round(n, 2)


# TASK - Welcome to the City

# Create a method sayHello/say_hello/SayHello that takes as input a name, city, and state 
# to welcome a person. Note that name will be an array consisting of one or more values that 
# should be joined together with one space between each, and the length of the name array 
# in test cases will vary.

def say_hello(name, city, state):
    return f"Hello, {' '.join([i for i in name])}! Welcome to {city}, {state}!"


# TASK - What's the real floor?

# With the 1st floor being replaced by the ground floor and the 13th floor being removed, 
# the numbers move down to take their place. In case of above 13, they move down by 
# two because there are two omitted numbers below them.

def get_real_floor(n):
    if n in range(0, 2):
        return 0
    elif n in range(2, 14):
        return n - 1
    elif n >= 14:
        return n - 2
    else:
        return n


# TASK - Powers of 2

# Complete the function that takes a non-negative integer n as input, and returns a list 
# of all the powers of 2 with the exponent ranging from 0 to n (inclusive).

def powers_of_two(n):
    return [2 ** i for i in range(0, n + 1)]


# TASK - Lario and Muigi Pipe ProblemLario and Muigi Pipe Problem

# Given the a list of numbers, return the list so that the values increment by 1 for 
# each index up to the maximum value

def pipe_fix(nums):
	return [i for i in range(min(nums), max(nums) + 1)]


# TASK - SpeedCode #2 - Array Madness

# Given two integer arrays a, b, both of length >= 1, create a program that returns 
# true if the sum of the squares of each element in a is strictly greater than 
# the sum of the cubes of each element in b.

def array_madness(a,b):
    return sum([i ** 2 for i in a]) > sum([i ** 3 for i in b])


# TASK - Incorrect division method

# This method, which is supposed to return the result of dividing its first argument 
# by its second, isn't always returning correct values. Fix it.

def divide_numbers(x,y):
    return x // y if x % y == 0 else x / y


# TASK - Regexp Basics - is it a digit?

# Implement String#digit? (in Java StringUtils.isDigit(String)), which should return 
# true if given object is a digit (0-9), false otherwise.

def is_digit(n):
    if n.isdigit():
        if int(n) in range(0, 10):
            return True
        else:
            return False
    else:
        return False

    
# TASK - Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right

# Remove n exclamation marks in the sentence from left to right. n is positive integer.

def remove(s, n):
    res = ""
    count = 0
    for i in s:
        if i == "!":
            if count != n:
                res += ""
                count += 1
            else:
                res += i
        else:
            res += i
    return res


# TASK - Find Multiples of a Number

# n this simple exercise, you will build a program that takes a value, integer, 
# and returns a list of its multiples up to another value, limit . If limit is a multiple of integer

def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1) if i % integer == 0]


# TASK - Remove First and Last Character Part Two

# This is a spin off of my first kata. You are given a list of character sequences as a comma 
# separated string. Write a function which returns another string containing all the character sequences 
# except the first and the last ones, separated by spaces. If the input string is empty, or the 
# removal of the first and last items would cause the string to be empty, return a null value.

def array(string):
    if len(string.split(",")) > 2:
        return " ".join(string.split(",")[1:-1])


# TASK - The Wide-Mouthed frog! 

# Your goal in this kata is to create complete the mouth_size method this method take one argument 
# animal which corresponds to the animal encountered by frog. If this one is an alligator 
# (case insensitive) return small otherwise return wide. 

def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"


# TASK - Enumerable Magic #3 - Does My List Include This?

# Create a method that accepts a list and an item, and returns true if the item belongs to the list, 
# otherwise false.

def include(arr,item):
    return item in arr


# TASK - Enumerable Magic #25 - Take the First N Elements

# Create a method take that accepts a list/array and a number n, and returns a list/array 
# array of the first n elements from the list/array.

def take(arr,n):
    return arr[:n]


# TASK - How many stairs will Suzuki climb in 20 years?

# The sum of all the stairs logged in a year will be used for estimating the number he might climb in 20.
# 20_year_estimate = one_year_total * 20

def stairs_in_20(stairs):
    return sum([sum(i) for i in stairs]) * 20


# TASK - Tip Calculator

# Complete the function, which calculates how much you need to tip based on the total amount of 
# the bill and the service. 

def calculate_tip(amount, rating):
    tip_ratings = {
        "terrible": 1.0,
        "poor": 1.05,
        "good": 1.10,
        "great": 1.15,
        "excellent": 1.20
    }
    
    if rating.lower() in tip_ratings:
        tip = (amount * tip_ratings[rating.lower()]) - amount
        print(tip)
        return round(tip) if tip <= int(tip) else int(tip) + 1
    else:
        return "Rating not recognised"

 
# TASK - What is between?

# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers 
# between the input parameters, including them.

def between(a,b):
    return [i for i in range(a, b + 1)]


# TASK - Arithmetic Sequence!

# You're going to write a function that's going to return the value in the nth index of an arithmetic sequence.(That is, 
# adding a constant to move to the next element in the "set").

def nthterm(first, n, c):
    res = []
    count = first
    for i in range(n + 1):
        res.append(count)
        count += c
    return res[-1]


# TASK - Regexp Basics - is it a vowel?

# Implement the function which should return true if given object is a vowel (meaning a, e, i, o, u), and false otherwise.

def is_vowel(s): 
    return s.lower() in ("a", "e", "i", "o", "u")


# TASK - Halving Sum

# Given a positive integer n, calculate the following sum:
#n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.

def halving_sum(n): 
    res = n
    res_l = [n]
    c = 0
    while res >= 1:
        res = n // 2
        res_l.append(res)
        n = res
    return sum(res_l)


# TASK - Limit string length - 1

# The function must return the truncated version of the given string up to the given limit 
# followed by "..." if the result is shorter than the original. Return the same string if 
# nothing was truncated.

def solution(st, limit): 
    return st[:limit] + "..." if len(st) > limit else st


# TASK - Sort Out The Men From Boys 

# Given an array/list [] of n integers , Separate The even numbers from the odds , or Separate 
# the men from the boys

def men_from_boys(arr):
    even = sorted(set([i for i in arr if i % 2 == 0]))
    odd = sorted(set([i for i in arr if i % 2 != 0]), reverse=True)
    return even + odd


# TASK - Find the position!

# When provided with a letter, return its position in the alphabet.
#Input :: "a"
# Ouput :: "Position of alphabet: 1"

def position(alphabet):
    return f"Position of alphabet: {ord(alphabet) - 96}"


# TASK - Return the day 

# Complete the function which returns the weekday according to the input number

def whatday(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days[num] if num in range(1, 8) else "Wrong, please enter a number between 1 and 7"


# TASK - Replace all dots

# The code provided is supposed replace all the dots . in the specified String str with dashes -

def replace_dots(str):
    return str.replace(".", "-")


# TASK - For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre

# f the winner is George Saint Pierre he will obviously say:
# "I am not impressed by your performance."
# If the winner is Conor McGregor he will most undoubtedly say:
# "I'd like to take this chance to apologize.. To absolutely NOBODY!"

def quote(fighter):
    name = " ".join([i.lower() for i in fighter.split()])
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!" if name == "conor mcgregor" else "I am not impressed by your performance."


# TASK - Take the Derivative

# Your function should multiply the two numbers, and then subtract 1 from the exponent. 
# Then, it has to print out an expression (like 28x^7). "^1" should not be truncated when exponent = 2.

def derive(coefficient, exponent): 
    return f"{coefficient * exponent}x^{exponent - 1}"


# TASK - Regex count lowercase letters

# Your task is simply to count the total number of lowercase letters in a string.

def lowercase_count(strng):
    count = 0
    for i in strng:
        if i.islower():
            count += 1
    return count


# TASK - Is it a palindrome?

# Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.

def is_palindrome(s):
    return s.lower() == s[::-1].lower()


# TASK - Grasshopper - Array Mean

# Find the mean (average) of a list of numbers in an array.

def find_average(nums):
    return sum(nums) / len(nums) if len(nums) > 0 else 0


# TASK - Basic Calculator

# Write a function called calculate that takes 3 values. The first and third values are numbers. 
# The second value is a character. If the character is "+" , "-", "*", or "/", the function will 
# return the result of the corresponding mathematical function on the two numbers. If the string 
# is not one of the specified characters, the function should return null (throw an 
# ArgumentException in C#).

def calculate(num1, operation, num2): 
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/" and num2 != 0:
        return num1 / num2


# TASK - Regexp Basics - is it a letter?

# Complete the code which should return true if the given object is a single ASCII letter (lower 
# or upper case), false otherwise.

def is_letter(s):
    if len(s) == 1:
        if ord(s.lower()) in range(97, 123):
            return True
        else:
            return False
    else:
        return False


# TASK - Return the first M multiples of N

# Implement a function, multiples(m, n), which returns an array of the first m multiples of 
# the real number n. Assume that m is a positive integer.

def multiples(m, n):
    count = 0
    nbr = 1
    res = []
    while count != m:
        res.append(n * nbr)
        count += 1
        nbr += 1
    return res


# TASK - Smallest value of an array

# Write a function that can return the smallest value of an array or the index of that 
# value. The function's 2nd parameter will tell whether it should return the value or the index.

def find_smallest(numbers,to_return):
    return min(numbers) if to_return == "value" else numbers.index(min(numbers))


# TASK - How old will I be in 2099?

# Your task is to write a function that takes two parameters: the year of birth and the year to 
# count years in relation to. As Philip is getting more curious every day he may soon want to 
# know how many years it was until he would be born, so your function needs to work with both dates 
# in the future and in the past.

def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year:
        if current_year - year_of_birth == 1:
            return f"You are {current_year - year_of_birth} year old."
        else:
            return f"You are {current_year - year_of_birth} years old."
    elif year_of_birth > current_year:
        if year_of_birth - current_year == 1:
            return f"You will be born in {year_of_birth - current_year} year."
        else:
            return f"You will be born in {year_of_birth - current_year} years."
    else:
        return 'You were born this very year!'
    

# TASK - Grader

# Create a function that takes a number as an argument and returns a grade based on that number.

def grader(score):
    if score == 0.6:
        return "D"
    elif score == 0.7:
        return "C"
    elif score == 0.8:
        return "B"
    elif score >= 0.9 and score <= 1:
        return "A"
    else:
        return "F"


# TASK - Parse float

# Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.

def parse_float(string):
    if type(string) == list:
        return None
    elif string.isalpha():
        return None
    else:
        return float(string)


# TASK - Grasshopper - Combine strings

# Create a function named (combine_names) that accepts two parameters (first and last name). The function 
# should return the full name.

def combine_names(first, last):
    return first + " " + last


# TASK - Javascript filter - 1

# While developing a website, you detect that some of the members have troubles logging in. Searching through 
# the code you find that all logins ending with a "_" make problems. So you want to write a function that 
# takes an array of pairs of login-names and e-mails, and outputs an array of all login-name, e-mails-pairs 
# from the login-names that end with "_".

def search_names(logins):
        
    def search(x):
        if "_" in x[0][-1]:
            return True
        else:
            return False
    
    f = filter(search, logins)
    res = []
    for i in f:
        res.append(i)
    return res


# TASK - Factorial

# Yor task is to write function factorial

import math

def factorial(n):
    return math.factorial(n)


# TASK - Miles per gallon to kilometers per liter

# Create an application that will display the number of kilometers per liter (output) based on the number of miles 
# per imperial gallon (input).

def converter(mpg):
    return round((mpg / 4.54609188) * 1.609344, 2)


# TASK - UEFA EURO 2016

# Finish the uefaEuro2016() function

def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
    elif scores[0] < scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
    else:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."


# TASK - Are arrow functions odd?

# Time to test your basic knowledge in functions! Return the odds from a list

def odds(arr):
    def odd(x):
        if x % 2 != 0:
            return True
        else:
            return False
    l = list(filter(odd, arr))
    return l


# TASK - CSV representation of array

# Create a function that returns the CSV representation of a two-dimensional 
# numeric array.

def to_csv_text(array):
    res = []
    for i in array:
        res.append(",".join(str(k) for k in i))
    return "\n".join(res)


# TASK - NBA full 48 minutes average

# Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight 
# extrapolation of ppg per 48 minutes rounded to the nearest tenth. Return 0 if 0.

def nba_extrap(ppg, mpg):
    return round(ppg / mpg * 48, 1) if mpg != 0 else 0


# TASK - Hex Hash Sum

# Every character of the string should be converted to the hex value of its ascii code, then the result should 
# be the sum of the numbers in the hex strings (ignore letters).

def hex_hash(code):
    text_binary = code.encode(encoding='utf_8')
    text_hex = text_binary.hex()
    res = [int(i) for i in text_hex if i.isdigit()]
    return sum(res)


# TASK - Moves in squared strings (I)

# This kata is the first of a sequence of four about "Squared Strings".
# You are given a string of n lines, each substring being n characters long: For example:
# s = "abcd\nefgh\nijkl\nmnop"
# We will study some transformations of this square of strings.
# Vertical mirror: vert_mirror (or vertMirror or vert-mirror)
# vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"
# Horizontal mirror: hor_mirror (or horMirror or hor-mirror)
# hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"

def vert_mirror(strng):
    return "\n".join([i[::-1] for i in strng.split("\n")])
def hor_mirror(strng):
    return "\n".join(strng.split("\n")[::-1])
def oper(fct, s):
    return vert_mirror(s) if fct == vert_mirror else hor_mirror(s)


# TASK - Alphabet war

# Write a function that accepts fight string consists of only small letters and return who 
# wins the fight. When the left side wins return Left side wins!, when the right side wins 
# return Right side wins!, in other case return Let's fight again!.

def alphabet_war(fight):
    left_side = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }

    right_side = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }

    left_side_result = 0
    right_side_result = 0

    for letter in left_side:
        c = fight.count(letter)
        left_side_result += c * left_side[letter]

    for letter in right_side:
        c = fight.count(letter)
        right_side_result += c * right_side[letter]
    
    print(left_side_result)
    print(right_side_result)

    if left_side_result > right_side_result:
        return "Left side wins!"
    elif left_side_result < right_side_result:
        return "Right side wins!"
    else:
        return "Let's fight again!"


# TASK - Love vs friendship

# If　a = 1, b = 2, c = 3 ... z = 26
#Then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# So friendship is twice stronger than love :-)

def words_to_marks(s):
    letters_dict = {}
    for i in range(97, 123):
        letters_dict[chr(i)] = i - 96
    
    res = 0
    for i in letters_dict:
        c = s.count(i)
        res += c * letters_dict[i]
    return res


# TASK - Pre-FizzBuzz Workout #1

# This is the first step to understanding FizzBuzz.
# Your inputs: a positive integer, n, greater than or equal to one. n is provided,
# you have NO CONTROL over its value.
# Your expected output is an array of positive integers from 1 to n (inclusive).
# Your job is to write an algorithm that gets you from the input to the output.

def pre_fizz(n):
    return [i for i in range(1, n + 1)]


# TASK - Add Length

# Your task is to write a function that takes a String and returns an Array/list 
# with the length of each word added to each element .

def add_length(str_):
    res = []
    for i in str_.split():
        res.append(" ".join([i, str(len(i))]))
    return res


# TASK - Classic Hello World

# You are given a method called main, make it print Hello World! and don't return anything

class Solution:
    def main(self):
        print("Hello World!")
    

# TASK - repeatIt

# Create a function that takes a string and an integer (n).
# The function should return a string that repeats the input string n number of times.
# If anything other than a string is passed in you should return "Not a string".

def repeat_it(string,n):
    return string * n if type(string) == str else "Not a string"


# TASK - Thinkful - Number Drills: Blue and red marbles

# You've decided to write a function, guessBlue() to help automatically calculate whether you 
# should guess "blue" or "red". The function should take four arguments:
# the number of blue marbles you put in the bag to start
# the number of red marbles you put in the bag to start
# the number of blue marbles pulled out so far (always lower than the starting number of blue marbles)
# the number of red marbles pulled out so far (always lower than the starting number of red marbles)
# guessBlue() should return the probability of drawing a blue marble, expressed as a float.

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled) / ((blue_start - blue_pulled) + (red_start - red_pulled))


# TASK - Validate Credit Card Number

# Given a positive integer of up to 16 digits, return true if it is a valid credit card number, 
# and false if it is not.
# Here is the algorithm:
# Double every other digit, scanning from right to left, starting from the second digit (from the right).
# Another way to think about it is: if there are an even number of digits, double every other digit starting 
# with the first; if there are an odd number of digits, double every other digit starting with the second
# If a resulting number is greater than 9, replace it with the sum of its own digits (which is the same as subtracting 
# 9 from it)
# Sum all of the final digits
# Finally, take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid

def validate(n):
    scan = []
    for i in range(1, len(str(n)) + 1):
        if len(str(n)) % 2 == 0:
            if i % 2 == 0:
                scan.append(int(str(n)[i - 1]))
            else:
                if int(str(n)[i - 1]) * 2 >= 9:
                    scan.append((int(str(n)[i - 1]) * 2) - 9)
                else:
                    scan.append(int(str(n)[i - 1]) * 2)
        else:
            if i % 2 != 0:
                scan.append(int(str(n)[i - 1]))
            else:
                if int(str(n)[i - 1]) * 2 >= 9:
                    scan.append((int(str(n)[i - 1]) * 2) - 9)
                else:
                    scan.append(int(str(n)[i - 1]) * 2)
    return sum(scan) % 10 == 0


# TASK - IP Validation

# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered 
# valid if they consist of four octets, with values between 0 and 255, inclusive.
# Input to the function is guaranteed to be a single string.

def is_valid_IP(strng):
    res = []
    if len(strng.split(".")) == 4:
        for i in strng.split("."):
            if i.isdigit():
                if len(i) > 1 and i[0] == "0":
                    res.append("False")
                else:
                    if int(i) in range(0, 256):
                        res.append(int(i))
                    else:
                        res.append("False")
            else:
                res.append("False")
    else:
        return False

    if "False" in res:
        return False
    else:
        return True


# TASK - Multiple of index

# Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

def multiple_of_index(arr):
    res = []
    c = 1
    for i in arr[1:]:
        if i % c == 0:
            res.append(i)
        c += 1
    return res


# TASK - Alan Partridge II - Apple Turnover

# Your job is simple, if (x) squared is more than 1000, return 'It's hotter than the sun!!', else, return 
# 'Help yourself to a honeycomb Yorkie for the glovebox.'.

def apple(x):
    temp = 0
    if type(x) == str:
        temp += int(x)
    else:
        temp += x
    if temp ** 2 >= 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."


# TASK - String cleaning

# Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the 
# numbers. Your program will take in a string and clean out all numeric characters, and return a string
# with spacing and special characters ~#$%^&!@*():;"'.,? all intact.

def string_clean(s):
    """
    Function will return the cleaned string
    """
    cleaned_string = ""
    clean_from = "0123456789"
    for i in s:
        if i not in clean_from:
            cleaned_string += i
    return cleaned_string


# TASK - Leonardo Dicaprio and Oscars

# if oscar was (integer) 88, you have to return "Leo finally won the oscar! Leo is happy".
# if oscar was 86, you have to return "Not even for Wolf of wallstreet?!"
# if it was not 88 or 86 (and below 88) you should return "When will you give Leo an Oscar?"
# if it was over 88 you should return "Leo got one already!"

def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar == 87 or oscar < 86:
        return "When will you give Leo an Oscar?"
    else:
        return "Leo got one already!"


# TASK - Find the Integral

# Create a function that finds the integral of the expression passed.
# In order to find the integral all you need to do is add one to the exponent (the second argument), 
# and divide the coefficient (the first argument) by that new number.

def integrate(coefficient, exponent):
    return f"{coefficient // (exponent + 1)}x^{exponent + 1}"


# TASK - Object Oriented Piracy

# Taking into account that an average crew member on board adds 1.5 units to the draft, a ship that 
# has a draft of more than 20 without crew is considered worthy to loot. Any ship weighing that much must have a lot of booty!

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        res = self.draft - self.crew * 1.5
        if res >= 20:
            return True
        else:
            return False


# TASK - Name Your Python!

# For those of us who are not very familiar with Python, let's handle the very basic challenge of creating a class named Python. 
# We want to give our Pythons a name, so it should take a name argument that we can retrieve later. 

class Python:
    def __init__(self, name):
        self.name = name


# TASK - Sum of Multiples

# Find the sum of all multiples of n below m

def sum_mul(n, m):
    result = 0
    if n <= 0 or m <= 0:
        return "INVALID"    
    elif n < m:
        for i in range(n, m):
            if i % n == 0:
                result += i
        return result
    elif n == m and (n != 0 and m != 0):
        return 0
    elif n > m:
        return 0
    

# TASK - Collatz Conjecture Length

# The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2. If n is odd, multiply it by 3 
# and add 1. If you repeat the process continuously for n, n will eventually reach 1.

def collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            res = n // 2
        else:
            res = n * 3 + 1
        n = res
        count += 1
    return count


# TASK - Is it a number?

# Given a string s, write a method (function) that will return true if its a valid single integer or floating 
# number or false if its not.

def isDigit(string):
    try:
        if "." in string:
            return type(float(string)) == float
        else:
            return type(int(string)) == int
    except:
        return False


# TASK - How do I compare numbers?

# What could be easier than comparing integer numbers? However, the given piece of code doesn't recognize 
# some of the special numbers for a reason to be found. Your task is to find the bug and eliminate it.

def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


# TASK - Find The Duplicated Number in a Consecutive Unsorted List

# You are given an array of n+1 integers 1 through n. In addition there is a single duplicate integer.
# The array is unsorted.
# An example valid array would be [3, 2, 5, 1, 3, 4]. It has the integers 1 through 5 and 3 is 
# duplicated. [1, 2, 4, 5, 5] would not be valid as it is missing 3.
# You should return the duplicate value as a single integer.

def find_dup(arr):
    res = dict()
    for i in arr:
        res[i] = arr.count(i)
    for k, v in res.items():
        if v == 2:
            return k 


# TASK - Reverse a Number

# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

def reverse_number(n):
    if n > 0:
        return int(str(n)[::-1])
    else:
        return int(str(abs(n))[::-1]) * -1


# TASK - Find the Capitals

# Complete the method that takes a sequence of objects with two keys each: country or state, and capital. 
# Keys may be symbols or strings.
# The method should return an array of sentences declaring the state or country and its capital.

def capital(capitals): 
    res_l = []
    res = ""
    for i in capitals:
        if "state" in i.keys():
                res = "The capital of " + i["state"] + " is " + i["capital"]
        else:
            res = "The capital of " + i["country"] + " is " + i["capital"]
        res_l.append(res)
    return res_l


# TASK - get ascii value of character

# Get ASCII value of a character.

def get_ascii(c):
    return ord(c)


# TASK - Closest elevator

# Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write 
# a function elevator accepting 3 arguments (in order):
# left - The current floor of the left elevator
# right - The current floor of the right elevator
# call - The floor that called an elevator
# It should return the name of the elevator closest to the called floor ("left"/"right").

def elevator(left, right, call):
    if abs(left - call) < abs(right - call):
        return "left"
    else:
        return "right"


# TASK - simple calculator 

# You are required to create a simple calculator that returns the result of addition, subtraction, 
# multiplication or division of two numbers.
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.

def calculator(x,y,op):
    return eval(f"{x}{op}{y}") if op in "+-*/" and (type(x) == int and type(y) == int) else 'unknown value'


# TASK - No Loops 2 - You only need one

# You will be given an array (a) and a value (x). All you need to do is check whether the provided array 
# contains the value, without using a loop.

def check(a, x): 
    return x in a


# TASK - Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation 
# mark at the end of string

# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner 
# kata, you can assume that the input data is always a non empty string, no need to verify it.

def remove(s):
    res = ""
    for i in s:
        if i != "!":
            res += i
    return res + "!"


# TASK - Head, Tail, Init and Last

# Your job is to implement these functions in your given language. Make sure it doesn't edit the array; that 
# would cause problems! Here's a cheat sheet:Your job is to implement these functions in your given language. 
# Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:
# | HEAD | <----------- TAIL ------------> |
# [  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
# | <----------- INIT ------------> | LAST |

def head(arr):
    return arr[0]

def tail(arr):
    return arr[1:]

def init(arr):
    return arr[:-1]

def last(arr):
    return arr[-1]


# TASK - Remove Duplicates

# You are to write a function called unique that takes an array of integers and returns the array with 
# duplicates removed. It must return the values in the same order as first seen in the given array. Thus 
# no sorting should be done, if 52 appears before 10 in the given array then it should also be that 52 
# appears before 10 in the returned array.

def unique(integers):
    d = {}
    for i in integers:
        d[i] = integers.count(i)
    res = []
    for i in d:
        res.append(i)
    return res


# TASK - Vampire Numbers

# Create a function that can receive two 'fangs' and determine if the product of the two is a valid 
# vampire number.

def vampire_test(x, y):
    x_l = [i for i in str(abs(x))]
    y_l = [i for i in str(abs(y))]
    res_x_l = x_l + y_l
    d_x_l = {}
    for i in res_x_l:
        d_x_l[i] = res_x_l.count(i)
    
    res = str(abs(x * y))
    res_d = {}
    for i in res:
        res_d[i] = res.count(i)
    
    if x < 0 and y < 0:
        return False
    else:
        if d_x_l == res_d:
            return True
        else:
            return False
        

# TASK - Sum of Odd Cubed Numbers

# Find the sum of the odd numbers within an array, after cubing the initial integers. The function should 
# return undefined/None/nil/NULL if any of the values aren't numbers. 

def cube_odd(arr):
    res = 0
    for i in arr:
        try:
            if not type(i) == bool:
                if i % 2 != 0:
                    res += i ** 3
            else:
                return None
        except:
            return None
    return res


# TASK - FIX: Get Full Name

# The code provided is supposed return a person's Full Name given their first and last names.
# But it's not working properly.

class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self):
        if len(self.first_name) == 0:
            return self.last_name
        elif len(self.last_name) == 0:
            return self.first_name
        elif len(self.first_name) == 0 and len(self.last_name) == 0:
            return ""
        else:
            return self.first_name + ' ' + self.last_name


# TASK - Alphabet symmetry

# Consider the word "abode". We can see that the letter a is in position 1 and b is in position 
# 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode 
# occupy the positions they would occupy in the alphabet, which are positions 4 and 5.
# Given an array of words, return an array of the number of letters that occupy their positions 
# in the alphabet for each word. For example,

def solve(arr):
    res = []
    l = [chr(i) for i in range(97, 123)]
    for elem in arr:
        count = 0
        for i in range(len(elem)):
            if i == l.index(elem.lower()[i]):
                count += 1
        res.append(count)
    return res


# TASK - Milk and Cookies for Santa

# Complete the function function that accepts a Date object, and returns true if it's Christmas 
# Eve (December 24th), false otherwise.

from datetime import date

def time_for_milk_and_cookies(dt):
    return dt.day == 24 and dt.month == 12


# TASK - Balanced Number (Special Numbers Series #1 ) 

# Balanced number is the number that * The sum of all digits to the left of the middle digit(s) and the sum of all digits to the 
# right of the middle digit(s) are equal*.

def balanced_num(number):
    l_side = []
    r_side = []
    
    l_side = [int(i) for i in str(number)[:(len(str(number)) - 1) // 2]]
    r_side = [int(i) for i in str(number)[(len(str(number)) + 2) // 2:]]
    
    if sum(l_side) == sum(r_side):
        return "Balanced"
    else:
        return "Not Balanced"


# TASK - Number of Decimal Digits

# Determine the total number of digits in the integer (n>=0) given as input to the function. For example, 9 is a single digit, 
# 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

def digits(n):
    return len(str(n))


# TASK - Simple consecutive pairs

# In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:
# pairs([1,2,5,8,-4,-3,7,6,5]) = 3
# The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
# --the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
# --the second pair is (5,8) and are not consecutive
# --the third pair is (-4,-3), consecutive. Count = 2
# --the fourth pair is (7,6), also consecutive. Count = 3. 
# --the last digit has no pair, so we ignore.

def pairs(ar):
    l = []
    half = 0
    res_count = 0
    count = 0
    if len(ar) % 2 == 0:
        l = ar
        half = len(ar) // 2
    else:
        l = ar[:-1]
        half = (len(ar) - 1) // 2
    l_res = []
    for i in range(half):
        l_res.append((l[count], l[count + 1]))
        count += 2
    for i in l_res:
        if (i[0] == i[1] + 1) or (i[0] == i[1] - 1):
            res_count += 1
    return res_count


# TASK - Minimize Sum Of Array (Array Series #1) 

# Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product.

def min_sum(arr):
    res = []
    for i in range(len(arr) // 2):
        res.append(max(arr) * min(arr))
        arr.remove(max(arr))
        arr.remove(min(arr))
    return sum(res)


# TASK - Find out whether the shape is a cube

def cube_checker(volume, side):
    if side > 0:
        if volume > 0:
            return volume % side == 0
        else:
            return False
    else:
        return False


# TASK - STRONGN Strong Number (Special Numbers Series #2) 

# Strong number is the number that the sum of the factorial of its digits is equal to number itself.
# For example: 145, since
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# So, 145 is a Strong number.

def strong_num(number):
    l = [int(i) for i in str(number)]
    res_l = []
    for i in l:
        res = 1
        for e in range(1, i + 1):
            res *= e
        res_l.append(res)
    return "STRONG!!!!" if sum(res_l) == number else "Not Strong !!"


# TASK - Build a square

# I will give you an integer. Give me back a shape that is as long and wide as the integer. The integer 
# will be a whole number between 1 and 50.

def generateShape(integer):
    l = []
    for i in range(integer):
        l.append("+" * integer)
    return "\n".join(l)


# TASK - Divide and Conquer

# Given a mixed array of number and string representations of integers, add up the string integers 
# and subtract this from the total of the non-string integers.
# Return as a number.

def div_con(x):
    s = 0
    i = 0
    for e in x:
        if type(e) == str:
            s += int(e)
        else:
            i += e
    return i - s


# TASK - Array element parity

# In this Kata, you will be given an array of integers whose elements have both a negative and a 
# positive value, except for one integer that is either only negative or only positive. Your 
# task will be to find that integer. 

def solve(arr):
    res = []
    for i in range(len(arr)):
        if (arr[i] * -1) in arr:
            res.append(0)
        else:
            res.append(1)
    ind = 0
    for i in res:
        if i != 0:
            ind = res.index(i)
    return arr[ind]


# TASK - ToLeetSpeak

# Your task is to write a function toLeetSpeak that converts a regular english sentence to Leetspeak.
# More about LeetSpeak You can read at wiki -> https://en.wikipedia.org/wiki/Leet
# Consider only uppercase letters (no lowercase letters, no numbers) and spaces.

def to_leet_speak(str):
    leet = {
      "A" : '@',
      "B" : '8',
      "C" : '(',
      "D" : 'D',
      "E" : '3',
      "F" : 'F',
      "G" : '6',
      "H" : '#',
      "I" : '!',
      "J" : 'J',
      "K" : 'K',
      "L" : '1',
      "M" : 'M',
      "N" : 'N',
      "O" : '0',
      "P" : 'P',
      "Q" : 'Q',
      "R" : 'R',
      "S" : '$',
      "T" : '7',
      "U" : 'U',
      "V" : 'V',
      "W" : 'W',
      "X" : 'X',
      "Y" : 'Y',
      "Z" : '2'
    }
    
    res = ""
    for i in str:
        if i in leet:
            res += leet[i]
        else:
            res += i
    return res


# TASK - shorter concat [reverse longer]

# Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.
# In other words, the shortest string has to be put as prefix and as suffix of the reverse 
# of the longest.

def shorter_reverse_longer(a,b):
    if len(a) < len(b):
        return a + b[::-1] + a
    else:
        return b + a[::-1] + b 


# TASK - Filter the number

# Oh no! The number has been mixed up with the text. Your goal is to retreive the number 
# from the text, can you return the number back to it's original state?

def filter_string(string):
    num = ""
    for i in string:
        if i.isdigit():
            num += i
    return int(num)


# TASK - Sum of Cubes

# Write a function that takes a positive integer n, sums all the cubed values from 1 to n, 
# and returns that sum.
# Assume that the input n will always be a positive integer.

def sum_cubes(n):
    res = 0
    for i in range(1, n + 1):
        res += i ** 3
    return res


# TASK - Char Code Calculation

# Given a string, turn each character into its ASCII character code and join 
# them together to create a number - let's call this number total1:
# 'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
# Then replace any incidence of the number 7 with the number 1, and call this number 'total2':
# Then return the difference between the sum of the digits in total1 and total2.

def calc(x):
    total1 = ""
    total2 = ""
    for i in x:
        total1 += str(ord(i))
    total2 = total1.replace("7", "1")
    tot1 = [int(i) for i in total1]
    tot2 = [int(i) for i in total2]
    return sum(tot1) - sum(tot2)


# TASK - Automorphic Number (Special Numbers Series #6)

# A number is called Automorphic number if and only if its square ends in the same digits as the number itself. 

def automorphic(n):
    print(n ** 2)
    return "Automorphic" if str(n ** 2)[len(str(n)) * -1:] == str(n) else "Not!!"


# TASK - Birthday I - Cake

# You will work out the number of candles that will fall from the provided string (y). You must add up the 
# character ASCII code of each even indexed (assume a 0 based indexing) character in y, with the alphabetical 
# position of each odd indexed character in y to give the string a total.
# example: 'abc' --> a=97, b=2, c=99 --> y total = 198.
# If the carpet catches fire, return 'Fire!', if not, return 'That was close!'.

def cake(candles,debris):
    res = 0
    for i in range(len(debris)):
        if i % 2 == 0:
            res += ord(debris[i])
        else:
            res += ord(debris[i]) - 96
    if candles == 0:
        return "That was close!"
    else:
        num = (res / candles) * 100
        if num > 70:
            return "Fire!"
        else:
            return 'That was close!'


# TASK - Largest Elements

# Write a program that outputs the top n elements from a list.

def largest(n, xs):
    res = []
    for i in range(n):
        res.append(max(xs))
        xs.remove(max(xs))
    return sorted(res)


# TASK - Simple Fun #152: Invite More Women?

#  King Arthur and his knights are having a New Years party. Last 
# year Lancelot was jealous of Arthur, because Arthur had a date 
# and Lancelot did not, and they started a duel.
# To prevent this from happening again, Arthur wants to make sure 
# that there are at least as many women as men at this year's party. 
# He gave you a list of integers of all the party goers.
# Arthur needs you to return true if he needs to invite more women 
# or false if he is all set.

def invite_more_women(arr):
    return arr.count(1) > arr.count(-1)


# TASK - Sum even numbers

# Complete the function that takes a sequence of numbers as single parameter. 
# Your function must return the sum of the even values of this sequence.
# Only numbers without decimals like 4 or 4.0 can be even.
# The input is a sequence of numbers: integers and/or floats. 

def sum_even_numbers(seq): 
    return sum([i for i in seq if i % 2 == 0])


# TASK - Counting Array Elements

# Write a function that takes an array and counts the number of each unique element present.

def count(array):
    res = {}
    for i in array:
        res[i] = array.count(i)
    return res


# TASK - Lost number in number sequence

# An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, 
# then the remaining numbers were mixed. Find the number that was deleted.

def find_deleted_number(arr, mixed_arr):
    for i in arr:
        if not i in mixed_arr:
            return i
        else:
            return 0


# TASK - esreveR

# Write a function reverse which reverses a list (or in clojure's case, any list-like data 
# structure)

def reverse(lst):
    empty_list = list()
    count = -1
    for i in range(len(lst)):
        empty_list.append(lst[count])
        count -= 1
    return empty_list


# TASK - Even numbers in an array

# Given an array of digital numbers, return a new array of length number containing the last 
# even numbers from the original array (in the same order). The original array will be 
# not empty and will contain at least "number" even numbers.

def even_numbers(arr,n):
    return [i for i in arr if i % 2 == 0][::-1][:n][::-1]


# TASK - Search for letters

# Create a function which accepts one arbitrary string as an argument, and return a string of 
# length 26.
# The objective is to set each of the 26 characters of the output string to either '1' or '0' 
# based on the fact whether the Nth letter of the alphabet is present in the input (independent 
# of its case).
# So if an 'a' or an 'A' appears anywhere in the input string (any number of times), set the first
# character of the output string to '1', otherwise to '0'. if 'b' or 'B' appears in the string, 
# set the second character to '1', and so on for the rest of the alphabet.

def change(st):
    res = ""
    alphabet = []
    for i in range(97, 123):
        alphabet.append(chr(i))
    for i in alphabet:
        if i in st.lower():
            res += "1"
        else:
            res += "0"
    return res


# TASK - Currying functions: multiply all elements in an array

# To complete this Kata you need to make a function multiplyAll/multiply_all which takes an array 
# of integers as an argument. This function must return another function, which takes a single 
# integer as an argument and returns a new array.
# The returned array should consist of each of the elements from the first array multiplied by 
# the integer.

def multiply_all(arr):
    def second(num):
        return [i * num for i in arr]
    return second


# TASK - All unique

# Write a program to determine if a string contains only unique characters. Return true if it 
# does and false otherwise.
# The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 
# 'a' and 'A' are considered different characters.

def has_unique_chars(string):
    res = {}
    for i in string:
        res[i] = string.count(i)
    if 2 in res.values():
        return False
    else:
        return True


# TASK - Multiply characters

# Here we have a function that help us spam our hearty laughter. But is not working! I need you to 
# find out why...

def spam(number):
    return 'hue' * number


# TASK - Find Count of Most Frequent Item in an Array

# Complete the function to find the count of the most frequent item of an array. You can assume that
# input is an array of integers. For an empty array return 0

def most_frequent_item_count(collection):
    if len(collection) == 0:
        return 0
    else:
        d = {}
        for i in collection:
            d[i] = collection.count(i)
        res = []
        for i in d.values():
            res.append(i)
        return max(res)


# TASK - Monotone travel

# You're given a list of compareable elements
# Your job is to check whether for any x all successors are greater or equal to x

def is_monotone(heights):
    if len(heights) == 0:
        return True
    else:
        c = 1
        l = []
        for i in range(len(heights) - 1):
            if heights[c] >= heights[0]:
                l.append(1)
            else:
                l.append(0)
            c += 1
        if 0 in l:
            return False
        else:
            return True


# TASK - Word values

# Given a string "abc" and assuming that each letter in the string has a value equal to its position 
# in the alphabet, our string will have a value of 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.
# You will be given a list of strings and your task will be to return the values of the strings as explained above 
# multiplied by the position of that string in the list. For our purpose, position begins with 1.

def name_value(my_list):
    l = []
    c = 1
    for words in my_list:
        res = 0
        for letter in words:
            if letter.isalpha():
                res += (ord(letter) - 96)
        l.append(res * c)
        c += 1
    return l


# TASK - Twisted Sum

# Find the sum of the digits of all the numbers from 1 to N (both ends included).

def compute_sum(n):
    res = 0
    for i in range(1, n + 1):
        if len(str(i)) == 1:
            res += i
        else:
            for e in str(i):
                res += int(e)
    return res


# TASK - Small enough? - Beginner

# You will be given an array and a limit value. You must check that all values 
# in the array are below or equal to the limit value. If they are, return true. 
# Else, return false.

def small_enough(array, limit):
    res = []
    for i in array:
        if i <= limit:
            res.append(1)
        else:
            res.append(0)
    if 0 in res:
        return False
    else:
        return True


# TASK - Simple Fun #74: Growing Plant

# Each day a plant is growing by upSpeed meters. Each night that plant's height 
# decreases by downSpeed meters due to the lack of sun heat. Initially, plant 
# is 0 meters tall. We plant the seed at the beginning of a day. We want to 
# know when the height of the plant will reach a certain level.

def growing_plant(upSpeed, downSpeed, desiredHeight):
    days = 0
    grow = 0
    day_night = 1
    if desiredHeight == 0:
        return 1
    else:
        while grow < desiredHeight:
            if day_night % 2 != 0:
                grow += upSpeed
            else:
                grow -= downSpeed
            days += 1
            day_night += 1
        if days % 2 == 0:
            return days / 2
        else:
            return int(days / 2) + 1


# TASK - Squares sequence

# Complete the function that returns an array of length n, starting 
# with the given number x and the squares of the previous number. If n is negative 
# or zero, return an empty array/list.

def squares(x, n):
    res = [x]
    if n <= 0:
        return []
    for i in range(n - 1):
        c = x * x
        res.append(c)
        x = c    
    return res


# TASK - Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript 
# developers coming from Europe
# You will be given an array of objects (hashes in ruby) representing data about developers 
# who have signed up to attend the coding meetup that you are organising for the first time.
# Your task is to return the number of JavaScript developers coming from Europe.

def count_developers(lst):
    count = 0
    for elem in lst:
        if "Europe" in elem.values() and "JavaScript" in elem.values():
            count += 1
    return count


# TASK - max diff - easy

# You must implement a function that return the difference between the biggest and the smallest 
# value in a list(lst) received as parameter.
# The list(lst) contains integers, that means it may contain some negative numbers.
# If the list is empty or contains a single element, return 0.
# The list(lst) is not sorted.

def max_diff(lst):
    return max(lst) - min(lst) if len(lst) > 0 else 0


# TASK - Product Of Maximums Of Array (Array Series #2) 

# Given an array/list [] of integers , Find the product of the k maximal numbers.

def max_product(lst, n_largest_elements):
    l = []
    res = 1
    for i in range(n_largest_elements):
        l.append(max(lst))
        lst.remove(max(lst))
    for i in l:
        res *= i
    return res


# TASK - Indexed capitalization

# Given a string and an array of integers representing indices, capitalize 
# all letters at the given indices. 

def capitalize(s,ind):
    res = ""
    for i in range(len(s)):
        if i in ind:
            res += s[i].upper()
        else:
            res += s[i].lower()
    return res


# TASK - Nth power rules them all!

# You are provided with an array of positive integers and an additional integer n (n > 1).
# Calculate the sum of each value in the array to the nth power. Then subtract the sum 
# of the original array.

def modified_sum(a, n):
    res = 0
    for i in a:
        res += i ** n
        res -= i
    return res


# TASK - Maximum Triplet Sum (Array Series #7) 

# Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications.

def max_tri_sum(numbers):
    l_numbers = [i for i in set(numbers)]
    res = 0
    for i in range(3):
        res += max(l_numbers)
        l_numbers.remove(max(l_numbers))
    return res


# TASK - Person Class Bug

# The following code was thought to be working properly, however when the code tries to access the 
# age of the person instance it fails. 

class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name


# TASK - Float Precision

# Update the solution method to round the argument value to the closest precision of two. The argument will 
# always be a float.

def solution(number):
    return round(number, 2)


# TASK - Say hello!

# Write a function to greet a person. Function will take name as input and greet the person by 
# saying hello. Return null/nil/None if input is empty string or null/nil/None.

def greet(name):
    return f"hello {name}!" if name else None


# TASK - The old switcheroo

# Write a function
# vowel_2_index
# that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string. 

def vowel_2_index(string):
    res = ""
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            res += str(i + 1)
        else:
            res += string[i]
    return res


# TASK - Pluck

# Implement a function which takes a sequence of objects and a property name, and returns a sequence containing the named 
# property of each object.

def pluck(objs, name): 
    res = []
    for d in objs:
        if name in d:
            res.append(d[name])
        else:
            res.append(None)
    return res


# TASK - Longest vowel chain

# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string 
# that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel 
# substring. Vowels are any of aeiou. 

def solve(s):
    count = 0
    res = []
    for i in s:
        if i in "aeiou":
            count += 1
        else:
            res.append(count)
            count = 0
    return max(res)


# TASK - Disarium Number (Special Numbers Series #3)

# Disarium number is the number that The sum of its digits powered with their respective 
# positions is equal to the number itself.

def disarium_number(number):
    num_list = [int(i) for i in str(number )]
    res = 0
    for i in range(len(num_list)):
        res += (num_list[i] ** (i + 1))
    return "Disarium !!" if res == number else "Not !!"


# TASK - Counting in the Amazon

#  The Arara are an isolated tribe found in the Amazon who count in pairs. For example one to eight is as follows:
# 1 = anane
# 2 = adak
# 3 = adak anane
# 4 = adak adak
# 5 = adak adak anane
# 6 = adak adak adak
# 7 = adak adak adak anane
# 8 = adak adak adak adak
# Take a given number and return the Arara's equivalent. 

def count_arara(n):
    res = []
    if n % 2 == 0:
        for i in range(n // 2):
            res.append('adak')
    else:
        for i in range((n - 1) // 2):
            res.append('adak')
        res.append('anane')
    return " ".join(res)


# TASK - Find Screen Size

# Given an integer width and a string ratio written as WIDTH:HEIGHT, output the screen dimensions as a string 
# written as WIDTHxHEIGHT.
# Note: The calculated height should be represented as an integer. If the height is fractional, truncate it.

def find_screen_height(width, ratio):
    return f"{width}x{int(width / (int(ratio.split(':')[0]) / int(ratio.split(':')[1])))}"


# TASK - All Inclusive?

# Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):
# a boolean true if all rotations of strng are included in arr (C returns 1)
# false otherwise (C returns 0)

def contain_all_rots(strng, arr):
    res = []
    if strng.isdigit():
        return True
    else:
        for i in arr:
            if sorted(strng) == sorted(i):
                res.append(1)
        return res.count(1) == len(strng)


# TASK - My Languages

# You are given a dictionary/hash/object containing some languages and your 
# test results in the given languages. Return the list of languages where your 
# test score is at least 60, in descending order of the results.
# Note: the scores will always be unique (so no duplicate values).

def my_languages(results):
    res = []
    sorted_values = sorted(results.values(), reverse=True)
    sorted_dict = {}
    for v in sorted_values:
        for k in results.keys():
            if results[k] == v:
                sorted_dict[k] = results[k]
    return [i for i in sorted_dict if sorted_dict[i] >= 60]       


# TASK - Nth Smallest Element (Array Series #4) 

# Given an array/list [] of integers , Find the Nth smallest element in this array 
# of integers

def nth_smallest(arr, pos):
    for i in range(pos - 1):
        arr.remove(min(arr))
    return min(arr)


# TASK - Numbers in strings

# In this Kata, you will be given a string that has lowercase letters and numbers. 
# Your task is to compare the number groupings and return the largest number. Numbers 
# will not have leading zeros. 

def solve_23(s):
    res = []
    str_num = ""
    for i in s:
        if i.isdigit():
            str_num += i
        else:
            str_num = ""
        res.append(str_num)
    final_res = []
    for i in res:
        if i.isdigit():
            final_res.append(int(i))
    return max(final_res)


# TASK - Naughty or Nice?

# Santa needs you to write two functions. Both of the functions accept a sequence of 
# objects. The first one returns a sequence containing only the names of the nice people, 
# and the other returns a sequence containing only the names of the naughty people. Return an 
# empty sequence [] if the result from either of the functions contains no names.

def get_nice_names(people):
    res = []
    for i in people:
        if i['was_nice']:
            res.append(i['name'])
    return res

def get_naughty_names(people):
    res = []
    for i in people:
        if not i['was_nice']:
            res.append(i['name'])
    return res


# TASK - Credit card issuer checking

# Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.
# Complete the function get_issuer() that will use the values shown below to determine the card 
# issuer for a given card number. If the number cannot be matched then the function should return 
# the string Unknown.

def get_issuer(number):
    if len(str(number)) == 15:
        if str(number)[:2] == "34" or str(number)[:2] == "37":
            return "AMEX"
        else:
            return "Unknown"
    elif len(str(number)) == 16:
        if str(number)[:4] == "6011":
            return "Discover"
        elif int(str(number)[:2]) in range(51, 56):
            return "Mastercard"
        elif str(number)[0] == "4":
            return "VISA"
        else:
            return "Unknown"
    elif len(str(number)) == 13:
        if str(number)[0] == "4":
            return "VISA"
        else:
            return "Unknown"
    else:
        return "Unknown"


# TASK - How many arguments\

# Create a function args_count, that returns the count of passed arguments

def args_count(*args, **kwargs):
    count = 0
    for i in args:
        count += 1
    for i in kwargs:
        count += 1
    return count


# TASK - Count all the sheep on farm in the heights of New Zealand

# Every Friday and Saturday night, farmer counts amount of sheep returned 
# back to his farm (sheep returned on Friday stay and don't leave for a weekend).
# Sheep return in groups each of the days -> you will be given two arrays with 
# these numbers (one for Friday and one for Saturday night). Entries are always 
# positive ints, higher than zero.
# Farmer knows the total amount of sheep, this is a third parameter. You need 
# to return the amount of sheep lost (not returned to the farm) after final sheep 
# counting on Saturday.
# Example 1: Input: {1, 2}, {3, 4}, 15 --> Output: 5
# Example 2: Input: {3, 1, 2}, {4, 5}, 21 --> Output: 6

def lost_sheep(friday,saturday,total):
    counter = 0
    for i in friday:
        counter += i
    for i in saturday:
        counter += i
    return total - counter


# TASK - List to Array

# Linked lists are data structures composed of nested or chained objects, each 
# containing a single value and a reference to the next object. 

class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def list_to_array(node):
        arr = []
        curr = node
        while (curr != None):
            arr.append(curr.value)
            curr = curr.next
        return arr


# TASK - Remove duplicate words

# Your task is to remove all duplicate words from a string, leaving only 
# single (first) words entries.

def remove_duplicate_words(s):
    d = {}
    for i in s.split():
        d[i] = s.split().count(i)
    return " ".join(d.keys())


# TASK - Partial Word Searching

# Write a method that will search an array of strings for all strings 
# that contain another string, ignoring capitalization. Then return an 
# array of the found strings. 

def word_search(query, seq):
    res = []
    for i in seq:
        if query.lower() in i.lower():
            res.append(i)
    if len(res) == 0:
        return ["None"]
    else:
        return res


# TASK - NATO Phonetic Alphabet

# In this kata, we're going to create the function nato that takes a 
# word and returns a string that spells the word using the NATO phonetic alphabet.
# There should be a space between each word in the returned string, and the first 
# letter of each word should be capitalized.
# For those of you that don't want your fingers to bleed, this kata already 
# has a dictionary typed out for you.
  
def nato(word):
    letters =  {
    "A": "Alpha",  "B": "Bravo",   "C": "Charlie",
    "D": "Delta",  "E": "Echo",    "F": "Foxtrot",
    "G": "Golf",   "H": "Hotel",   "I": "India",
    "J": "Juliett","K": "Kilo",    "L": "Lima",
    "M": "Mike",   "N": "November","O": "Oscar",
    "P": "Papa",   "Q": "Quebec",  "R": "Romeo",
    "S": "Sierra", "T": "Tango",   "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
    }
    nato_word = []
    for letter in word:
        nato_word.append(letters[letter.upper()])
    return " ".join(nato_word)


# TASK - Find sum of top-left to bottom-right diagonals

# Given a square matrix (i.e. an array of subarrays), find the sum of 
# values from the first value of the first array, the second value of 
# the second array, the third value of the third array, and so on...

def diagonal_sum(array):
    c = 0
    res = 0
    for i in array:
        res += i[c]
        c += 1
    return res


# TASK - Simple Fun #37: House Numbers Sum

# For the given sequence of houses determine the sum that the boy 
# will get. It is guaranteed that there will always be at least 
# one 0 house on the path.

def house_numbers_sum(inp):
    return sum(inp[:inp.index(0)])


# TASK - Responsible Drinking

# Your fellow coders have bought you several drinks tonight in 
# the form of a string. Return a string suggesting how many 
# glasses of water you should drink to not be hungover.

def hydrate(drink_string): 
    res = 0
    for i in drink_string.split():
        if i.isdigit():
            res += int(i)
    g = ""
    if res == 1:
        g = "glass"
    else:
        g = "glasses"
    return f"{res} {g} of water"


# TASK - Return a sorted list of objects

# You'll be passed an array of objects (list) - you must sort them in descending 
# order based on the value of the specified property (sortBy). 

def sort_list(sort_by, lst):
    r = []
    res = []
    for d in lst:
        r.append(d[sort_by])
    for i in sorted(set(r), reverse=True):
        for d in lst:
            if i == d[sort_by]:
                res.append(d)
    return res


# TASK - Good vs Evil

# Middle Earth is about to go to war. The forces of good will have many battles with the 
# forces of evil. Different races will certainly be involved. Each race has a certain 
# worth when battling against others. On the side of good we have the following races, 
# with their associated worth:
    # Hobbits: 1
    # Men: 2
    # Elves: 3
    # Dwarves: 3
    # Eagles: 4
    # Wizards: 10
# On the side of evil we have:
    # Orcs: 1
    # Men: 2
    # Wargs: 2
    # Goblins: 2
    # Uruk Hai: 3
    # Trolls: 5
    # Wizards: 10
# Although weather, location, supplies and valor play a part in any battle, if you add 
# up the worth of the side of good and compare it with the worth of the side of evil, the 
# side with the larger worth will tend to win.

def goodVsEvil(good, evil):
    good_res = 0
    evil_res = 0
    
    good_d = {
        "Hobbits": 1,
        "Men": 2,
        "Elves": 3,
        "Dwarves": 3,
        "Eagles": 4,
        "Wizards": 10
    }

    good_l = ["Hobbits",
            "Men",
            "Elves",
            "Dwarves",
            "Eagles",
            "Wizards"]

    evil_d = { 
        "Orcs": 1,
        "Men": 2,
        "Wargs": 2,
        "Goblins": 2,
        "Uruk Hai": 3,
        "Trolls": 5,
        "Wizards": 10
    }

    evil_l = [
        "Orcs",
        "Men",
        "Wargs",
        "Goblins",
        "Uruk Hai",
        "Trolls",
        "Wizards"
    ]

    for i in range(len(good.split())):
        if good.split()[i] == "0":
            good_res += 0
        else:
            good_res += (good_d[good_l[i]] * int(good.split()[i]))

    for i in range(len(evil.split())):    
        if evil.split()[i] == "0":
            evil_res += 0
        else:
            evil_res += (evil_d[evil_l[i]] * int(evil.split()[i]))

    if good_res > evil_res:
        return "Battle Result: Good triumphs over Evil"
    elif good_res < evil_res:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

    
# TASK - Special Number (Special Numbers Series #5)

# A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5
# Given a number determine if it special number or not . 

def special_number(number):
    str_num = [i for i in str(number)]
    res = []
    for i in str_num:
        if int(i) in range(0, 6):
            res.append(True)
        else:
            res.append(False)
    if False in res:
        return "NOT!!"
    else:
        return "Special!!"


# TASK - Jumping Number (Special Numbers Series #4)

# Jumping number is the number that All adjacent digits in it differ by 1.
# Given a number, Find if it is Jumping or not.

def jumping_number(number):
    if len(str(number)) == 1:
        return "Jumping!!"
    else:
        res = []
        c = 1
        num_to_check = int(str(number)[0])
        for i in range(len(str(number)) - 1):
            if num_to_check - int(str(number)[c]) == 1:
                res.append(True)
            elif int(str(number)[c]) - num_to_check == 1:
                res.append(True)
            else:
                res.append(False)
            num_to_check = int(str(number)[c])
            c += 1
        if False in res:
            return"Not!!"
        else:
            return "Jumping!!"


# TASK - Unique string characters

# In this Kata, you will be given two strings a and b and your task will 
# be to return the characters that are not common in the two strings.
# Notice also that you return the characters from the first string concatenated with 
# those from the second string.

def solve(a,b):
    res = ""
    for i in a:
        if not i in b:
            res += i
    for i in b:
        if not i in a:
            res += i
    return res
    

# TASK - Tidy Number (Special Numbers Series #9)

# A Tidy number is a number whose digits are in non-decreasing order.
# Given a number, Find if it is Tidy or not . 

def tidyNumber(n):
    res = []
    c = 1
    numb = int(str(n)[0])
    for i in range(len(str(n)) - 1):
        if int(str(n)[c]) >= numb:
            res.append(True)
        else:
            res.append(False)
        numb = int(str(n)[c])
        c += 1
    if False in res:
        return False
    else:
        return True


# TASK - Building blocks

# Write a class Block that creates a block (Duh..)
#Requirements
# The constructor should take an array as an argument, this will contain 3 integers 
# of the form [width, length, height] from which the Block should be created.

class Block:
    def __init__(self, arr):
        self.arr = arr

    def get_width(self):
        return self.arr[0]
    
    def get_length(self):
        return self.arr[1]
    
    def get_height(self):
        return self.arr[2]
    
    def get_surface_area(self):
        return 2 * self.get_width() * self.get_length() + 2 * self.get_length() * self.get_height() + 2 * self.get_height() * self.get_width()
    
    def get_volume(self):
        return self.get_width() * self.get_height() * self.get_length()


# TASK - Two fighters, one winner.

# Create a function that returns the name of the winner in a fight between two fighters.
# Each fighter takes turns attacking the other and whoever kills the other first is 
# victorious. Death is defined as having health <= 0.# 
# Each fighter will be a Fighter object/instance. See the Fighter class below in 
# your chosen language.
# Both health and damagePerAttack (damage_per_attack for python) will be integers 
# larger than 0. You can mutate the Fighter objects.

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

def declare_winner(fighter1, fighter2, first_attacker):
    dam = 0
    while fighter1.health >= 0 and fighter2.health >= 0:
        if first_attacker == fighter1.name:
            dam = fighter2.health - fighter1.damage_per_attack
            fighter2.health = dam
            first_attacker = fighter2.name
        else:
            dam = fighter1.health - fighter2.damage_per_attack
            fighter1.health = dam
            first_attacker = fighter1.name
    
    if fighter1.health <= 0:
        return fighter2.name
    else:
        return fighter1.name


# TASK - Classy Classes

# Your task is to complete this Class, the Person class has been created. You must fill 
# in the Constructor method to accept a name as string and an age as number, complete 
# the get Info property and getInfo method/Info getter which should return johns age is 34

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"


# TASK - Bumps in the Road

# Your car is old, it breaks easily. The shock absorbers are gone and you think it can 
# handle about 15 more bumps before it dies totally.
# Unfortunately for you, your drive is very bumpy! Given a string showing either flat road 
# ("_") or bumps ("n"), work out if you make it home safely. 15 bumps or under, return 
# "Woohoo!", over 15 bumps return "Car Dead".

def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"


# TASK - Switcheroo

# Given a string made up of letters a, b, and/or c, switch the position of letters a and b 
# (change a to b and vice versa). Leave any incidence of c untouched.

def switcheroo(s):
    res_list = []
    for i in s:
        if i == "a":
            res_list.append("b")
        elif i == "b":
            res_list.append("a")
        else:
            res_list.append(i)
    return "".join(res_list)


# TASK - Simple remove duplicates

# In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

def solve(arr): 
    reverse_arr = arr[::-1]
    d = {}
    for i in reverse_arr:
        d[i] = reverse_arr.count(i)
    return [i for i in d.keys()][::-1]


# TASK - Alternate case

# Write function alternateCase which switch every letter in string from upper to lower and from lower 
# to upper. E.g: Hello World -> hELLO wORLD

def alternate_case(s):
    res = ""
    for i in s:
        if i.islower():
            res += i.upper()
        else:
            res += i.lower()
    return res
    

# TASK - Return substring instance count

# Complete the solution so that it returns the number of times the search_text is found within the full_text. 

def solution(full_text, search_text):
    return full_text.count(search_text)


# TASK - Cat and Mouse - Easy Version

# You will be given a string (x) featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'.
# You need to find out if the cat can catch the mouse from it's current position. The cat can jump over 
# three characters. So:
# C.....m returns 'Escaped!' <-- more than three characters between
# C...m returns 'Caught!' <-- as there are three characters between the two, the cat can jump.

def cat_mouse(x):
    return "Escaped!" if x.count(".") > 3 else "Caught!"


# TASK - Coding Meetup #2 - Higher-Order Functions Series - Greet developers

# You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.
# Your task is to return an array where each object will have a new property 'greeting' with the following string value:
# Hi < firstName here >, what do you like the most about < language here >?

def greet_developers(lst): 
    res = []
    for d in lst:
        res_d = {}
        for k, v in d.items():
            res_d[k] = v
        res_d["greeting"] = f"Hi {d['firstName']}, what do you like the most about {d['language']}?"
        res.append(res_d)
    return res


# TASK - Sum of all arguments

# Write a function that finds the sum of all its arguments.

def sum_args(*args):
    res = 0
    for i in args:
        res += i
    return res


# TASK - Compare Strings by Sum of Chars

# Compare two strings by comparing the sum of their values (ASCII character code).
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as 
# it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.

def compare(s1,s2):
    if s1 == "" or s2 == "":
        return True
    else:
        s1_sum = 0
        s2_sum = 0
        for i in s1:
            if ord(i.upper()) in range(65, 90):
                s1_sum += ord(i.upper())
        for i in s2:
            if ord(i.upper()) in range(65, 90):
                s2_sum += ord(i.upper())
        return s1_sum == s2_sum


# TASK - Interview Question (easy)

# You receive the name of a city as a string, and you need to return a string that shows 
# how many times each letter shows up in the string by using asterisks (*).

def get_strings(city):
    d = {}
    res = []
    for l in city.lower():
        if not l == " ":
            d[l] = "*" * city.lower().count(l)
    for elem in d:
        s = ""
        s += elem
        s += ":"
        s += d[elem]
        res.append(s)
    return ",".join(res)


# TASK - Candy problem

# Your job is to find out how much candy each child has, and give them each additional candy 
# until they too have as much as the child(ren) with the most candy. You also want to keep 
# a total of how much candy you've handed out because reasons."

def candies(s):
    if len(s) > 1:
        res = 0
        for i in s:
            res += (max(s) - i)
        return res
    else:
        return -1


# TASK - Arithmetic List!

# In this kata, you will write an arithmetic list which is basically a list that contains 
# consecutive terms in the sequence.
# You will be given three parameters :
# first the first term in the sequence
# c the constant that you are going to ADD ( since it is an arithmetic sequence...)
# l the number of terms that should be returned
# In this kata, you will write an arithmetic list which is basically a list that contains 
# consecutive terms in the sequence.
# You will be given three parameters :
# first the first term in the sequence
# c the constant that you are going to ADD ( since it is an arithmetic sequence...)
# l the number of terms that should be returned

def seqlist(first,c,l):
    res = []
    for i in range(l):
        res.append(first)
        first += c
    return res


# TASK - Convert an array of strings to array of numbers

# Create the function that takes as a parameter a sequence of numbers represented 
# as strings and outputs a sequence of numbers.

def to_float_array(arr): 
    res = []
    for i in arr:
        if "." in i:
            res.append(float(i))
        else:
            res.append(int(i))
    return res


# TASK - Formatting decimal places #1

# Each floating-point number should be formatted that only the first two decimal places 
# are returned. You don't need to check whether the input is a valid number because only
# valid numbers are used in the tests. 

def two_decimal_places(number):
    return float(str(number)[:str(number).index(".")] + "." + str(number)[str(number).index(".") + 1 : str(number).index(".") + 3])


# TASK - Numbers to Letters

# Given an array of numbers (in string format), you must return a string. The numbers correspond 
# to the letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for '!', 
# '?' and ' ' that are represented by '27', '28' and '29' respectively.

def switcher(arr):
    d = {"27": "!", "28": "?", "29": " ", }
    for i in range(97, 123):
        d[str(123 - i)] = chr(i)
    res = ""
    for i in arr:
        res += d[i]
    return res


# TASK - Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?

# You will be given an array of objects (associative arrays in PHP) representing data about developers who 
# have signed up to attend the next coding meetup that you are organising.

def is_ruby_coming(lst): 
    res = 0
    for d in lst:
        if d["language"] == "Ruby":
            res += 1
    if res >= 1:
        return True
    else:
        return False


# TASK - Maximum Gap (Array Series #4)

# Given an array/list [] of integers , Find The maximum difference between the successive elements 
# in its sorted form. 

def max_gap(numbers):
    sorted_list = sorted(numbers)
    res = []
    c = 0
    for i in range(len(sorted_list) - 1):
        res.append(sorted_list[c + 1] - sorted_list[c])
        c += 1
    return max(res)


# TASK - Basic Math (Add or Subtract)

# In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

def calculate(s):
    res = []
    for i in s:
        if i.isdigit():
            res.append(i)
        else:
            if i == "p":
                res.append("+")
            elif i == "m":
                res.append("-")
    return str(eval("".join(res)))


# TASK - Sum of Intervals

# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the 
# sum of all the interval lengths. Overlapping intervals should only be counted once. 

def sum_of_intervals(intervals):
    res = []
    for i in intervals:
        for e in range(min(i), max(i)):
            res.append(e)
    sorted_l = sorted(set(res))
    return len(sorted_l)


# TASK - Series of integers from m to n

# Write a function that accepts two arguments and generates a sequence containing the integers from 
# the first argument to the second inclusive. 

def generate_integers(m, n): 
    return [i for i in range(m, n + 1)]


# TASK - Case swapping

# Given a string, swap the case for each of the letters.

def swap(string_):
    res = ""
    for i in string_:
        if i.islower():
            res += i.upper()
        else:
            res += i.lower()
    return res


# TASK - Populate hash with array keys and default value

# Complete the function so that it takes an array of keys and a default 
# value and returns a hash (Ruby) / dictionary (Python) with all keys set to the default value. 

def populate_dict(keys, default):
    d = {}
    for i in keys:
        d[i] = default
    return d


# TASK - Converting integer to currency format

# Write a function that takes an integer in input and outputs a string with currency format.
# Integer in currency format is expressed by a string of number where every three characters 
# are separated by comma. 

def to_currency(price):
    reversed_price = str(price)[::-1]
    l = []
    c = 0    
    for i in range(1, len(reversed_price) + 1):
        if i % 3 == 0:
            l.append(reversed_price[c])
            l.append(",")

        else:
            l.append(reversed_price[c])
        c += 1
    return "".join(l[::-1])[1:] if len(reversed_price) % 3 == 0 else "".join(l[::-1])


# TASK - ATM

# There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
# You are given money in nominal value of n with 1<=n<=1500.
# Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

def solve(n):
    c = 0
    while n > 0:
        c += 1
        res = n
        if res >= 500:
            n = res - 500
        elif res >= 200:
            n = res - 200
        elif res >= 100:
            n = res - 100
        elif res >= 50:
            n = res - 50    
        elif res >= 20:
            n = res - 20
        elif res >= 10:
            n = res - 10
        elif res < 10:
            n = -1
    if n == 0:
        return c
    else:
        return -1


# TASK - Split In Parts

# The aim of this kata is to split a given string into different strings of equal size (note size of 
# strings is passed to the method)

def split_in_parts(s, part_length): 
    print(len(s))
    res = ""
    c = 0
    for i in range(1, len(s) + 1):
        if i % part_length == 0:
            res += s[c]
            res += " "
        else:
            res += s[c]
        c += 1
    return res[:-1] if len(s) % part_length == 0 else res


# TASK - Retrieve array value by index with default

# Complete the solution. It should try to retrieve the value of the array at the index provided. 
# If the index is out of the array's max bounds then it should return the default value instead. 

def solution(items, index, default_value):
    try:
        if items[index]:
            return items[index]
    except:
        return default_value


# TASK - Simple Fun #2: Circle of Numbers

# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that 
# the distance between any two neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).

def circle_of_numbers(n, fst):
    res = fst + n // 2
    if res > n:
        return (fst + n // 2) - n
    elif res == n:
        return 0
    else:
        return res


# TASK - Help Bob count letters and digits.

# He needs you to create a method that can determine how many letters and digits are in a given string.

def count_letters_and_digits(s):
    return sum([1 for i in s if i.isalnum()])


# TASK - All Star Code Challenge #22

# Create a function that takes an integer argument of seconds and converts the value into a string 
# describing how many hours and minutes comprise that many seconds.

def to_time(seconds):
    hours = seconds // 3600
    minutes = 0
    if hours == 0:
        minutes = seconds // 60
    else:
        minutes = (seconds - (hours * 3600)) // 60
    return f"{hours} hour(s) and {minutes} minute(s)"


# TASK - Simple string characters

# In this Kata, you will be given a string and your task will be to return a list of ints detailing 
# the count of uppercase letters, lowercase, numbers and special characters, as follows.

def solve(s):
    uppercase = 0
    lowercase = 0
    numbers = 0
    specials = 0
    for i in s:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        elif i.isdigit():
            numbers += 1
        else:
            specials += 1
    return [uppercase, lowercase, numbers, specials]


# TASK - Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer

# You will be given an array of objects (associative arrays in PHP) representing data about
# developers who have signed up to attend the next coding meetup that you are organising. 
# The list is ordered according to who signed up first.
# Your task is to return one of the following strings
# < firstName here >, < country here > of the first Python developer who has signed up; or
# There will be no Python developers if no Python developer has signed up.

def get_first_python(users):
    for i in users:
        if i["language"] == "Python":
            return f"{i['first_name']}, {i['country']}"
    return "There will be no Python developers"


# TASK - Find min and max

# Implement a function that returns the minimal and the maximal value of a list (in this order).

def get_min_max(seq): 
    return min(seq), max(seq)


# TASK - Find all occurrences of an element in an array

# Given an array (a list in Python) of integers and an integer n, find all occurrences of n 
# in the given array and return another array containing all the index positions of n in the given array.
# If n is not in the given array, return an empty array [].
#Assume that n and all values in the given array will always be integers.

def find_all(array, n):
    res = []
    for i in range(len(array)):
        if array[i] == n:
            res.append(i)
    return res


# TASK - Array Leaders (Array Series #3)

# An element is leader if it is greater than The Sum all the elements to its right side.

def array_leaders(numbers):
    res = []
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i + 1:]):
            res.append(numbers[i])
    return res


# TASK - makeBackronym

# Complete the function to create backronyms. Transform the given string (without spaces) to a backronym, 
# using the preloaded dictionary and return a string of words, separated with a single space (but no trailing spaces).

def make_backronym(acronym):
    res = []
    for i in acronym:
        res.append(dictionary[i.upper()])
    return " ".join(res)


# TASK - Extra Perfect Numbers (Special Numbers Series #7)

# Given a positive integer N , Return the extra perfect numbers in range from 1 to N .

def extra_perfect(n):
    return [i for i in range(1, n + 1) if i % 2 != 0]


# TASK - Valid Spacing

# Your task is to write a function called valid_spacing() or validSpacing() which 
# checks if a string has valid spacing. The function should return either True or False. 

def valid_spacing(s):
    count = 0
    for i in s:
        if i == " ":
            count += 1
    return count == len(s.split()) - 1


# TASK - Digital cypher

# Digital Cypher assigns to each letter of the alphabet unique number. Instead of letters 
# in encrypted word we write the corresponding number. Then we add to each obtained digit 
# consecutive digits from the key.

def encode(message, key):
    res = []
    multiply = len(message) // len(str(key)) + 1
    l = [int(i) for i in str(key)] * multiply
    c = 0
    for i in message:
        res.append((ord(i) - 96) +  l[c])
        c += 1
    return res


# TASK - String to integer conversion

# It should make the conversion if the given string only contains a single integer 
# value (and possibly spaces - including tabs, line feeds... - at both ends)
# For all other strings (including the ones representing float values), it should return NaN

def my_parse_int(string):
    try:
        return int(string)
    except:
        return "NaN"


# TASK - Sorting Dictionaries

# Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 
# 2 items).
# The list must be sorted by the value and be sorted largest to smallest.

def sort_dict(d):
    res = []
    dic = {}
    for i in d:
        dic[d[i]] = i
    sorted_d = sorted(dic, reverse=True)
    for i in sorted_d:
        res.append((dic[i], i))
    return res


# TASK - Spacify

# Modify the spacify function so that it returns the given string with spaces inserted between each character. 

def spacify(string):
    res = ""
    for i in string:
        res += i
        res += " "
    return res[:-1]


# TASK - Product of Array Items

# Calculate the product of all elements in an array.
# If the array is empty or None, return None.

def product(numbers):
    if numbers:
        res = 1
        for i in numbers:
            res *= i
        return res
    else:
        return None


# TASK - Spoonerize Me

# Your task is to create a function that takes a string of two words, separated by a space: 
# words and returns a spoonerism of those words in a string, as in the above example.

def spoonerize(words):
    return words.split()[1][0] + words.split()[0][1:] + " " + words.split()[0][0] + words.split()[1][1:]


# TASK - Remove All The Marked Elements of a List

# Define a method/function that removes from a given array of integers all the values contained 
# in a second array.

class List:
    def remove_(self, integer_list, values_list):
        res = []
        for i in integer_list:
            if not i in values_list:
                res.append(i)
        return res


# TASK - Difference Of Squares

# Find the difference between the sum of the squares of the first n natural numbers 
# (1 <= n <= 100) and the square of their sum.

def difference_of_squares(n):
    num = 0
    num_sq = 0
    for i in range(1, n + 1):
        num += i
        num_sq += i ** 2
    return (num ** 2) - num_sq


# TASK - Inspiring Strings

# When given a string of space separated words, return the word with the longest length. 
# If there are multiple words with the longest length, return the last instance of the 
# word with the longest length.

def longest_word(string_of_words):
    l = [len(i) for i in string_of_words.split()]
    res = []
    for i in string_of_words.split():
        if len(i) == max(l):
            res.append(i)
    if len(res) == 1:
        return res[0]
    else:
        return res[-1]


# TASK - Summy

# Write a function that takes a string which has integers inside it separated 
# by spaces, and your task is to convert each integer in the string into an integer 
# and return their sum.

def summy(string_of_ints):
    sum_of_ints = sum([int(i) for i in string_of_ints.split()])
    return sum_of_ints


# TASK - The Office I - Outed

# Given an object (meet) containing team member names as keys, and their happiness rating 
# out of 10 as the value, you need to assess the overall happiness rating of the group. 
# If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.

def outed(meet, boss):
    res = 0
    for i in meet:
        if i == boss:
            res += meet[i] * 2
        else:
            res += meet[i]
    if res / len(meet) <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'


# TASK - Does my number look big in this?

# A Narcissistic Number is a positive number which is the sum of its 
# own digits, each raised to the power of the number of digits in a 
# given base. In this Kata, we will restrict ourselves to decimal (base 10).

def narcissistic( value ):
    return sum([int(i) ** len(str(value)) for i in str(value)]) == value


# TASK - Find the unique number

# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    return list(set(arr))[[arr.count(list(set(arr))[0]), arr.count(list(set(arr))[1])].index(1)]


# TASK - Break camelCase

# Complete the solution so that the function will break up camel casing, using a space 
# between words.

def solution(s):
    res = ""
    for i in s[::-1]:
        if i.isupper():
            res += i 
            res += " "
        else:
            res += i
    return res[::-1]


# TASK - Give me a Diamond

# You need to return a string that looks like a diamond shape when printed on the screen, 
# using asterisk (*) characters. Trailing spaces should be removed, and every line must 
# be terminated with a newline character (\n).

def diamond(n):
    res_l = []
    if n % 2 == 0 or n <= 0:
        return None
    else:
        for i in range(1, n + 1):
            res = ""
            if i % 2 != 0:
                res += (" " * ((n - i) // 2))
                res += "*" * i
                res += "\n"
            res_l.append(res)
        return "".join(res_l) + "".join(res_l[:-1][::-1])


# TASK - Return a string's even characters.

# Write a function that returns a sequence (index begins with 1) of all the even characters 
# from a string. If the string is smaller than two characters or longer than 100 characters, 
# the function should return "invalid string".

def even_chars(st): 
    res = []
    if len(st) in range(2, 101):
        for i in range(1, len(st) + 1):
            if i % 2 == 0:
                res.append(st[i - 1])
        return res
    else:
        return "invalid string"


# TASK - Reverse the bits in an integer

# Write a function that reverses the bits in an integer.
# For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011
# which is 267

def reverse_bits(n):
    return int(bin(n)[2:][::-1], base=2)


# TASK - Odd-Even String Sort

# Given a string S. You have to return another string such that even-indexed and odd-indexed 
# characters of S are grouped and groups are space-separated (see sample below)

def sort_my_string(S):
    c = 0
    odd = ""
    even = ""
    for i in S:
        if c % 2 == 0:
            even += i
            c += 1
        else:
            odd += i
            c += 1
    return even + " " + odd


# TASK - Evens and Odds

# his kata is about converting numbers to their binary or hexadecimal representation:
# If a number is even, convert it to binary.
# If a number is odd, convert it to hex.

def evens_and_odds(n):
    return bin(n)[2:] if n % 2 == 0 else hex(n)[2:]


# TASK - What's my golf score?

# Complete the function which accepts two strings and calculates the golf score of a game. 
# Both strings will be of length 18, and each character in the string will be a number between 
# 1 and 9 inclusive. 

def golf_score_calculator(par_string, score_string):
    res = 0
    for i in range(len(par_string)):
        res += (int(score_string[i]) - int(par_string[i]))
    return res


# TASK - Unlimited Sum

# Write a function sum that accepts an unlimited number of integer arguments, and adds all of 
# them together.
# The function should reject any arguments that are not integers, and sum the remaining integers.

def sum(*args):
    res = 0
    for i in args:
        if type(i) == int:
            res += i
    return res


# TASK - Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?

# Your task is to return either:
# true if all developers in the list code in the same language; or
# false otherwise.

def is_same_language(lst): 
    count = 0
    lang = lst[0]['language']
    for d in lst:
        if d['language'] == lang:
            count += 1
    if len(lst) == count:
        return True
    else:
        return False


# TASK - Sum of integers in string

# Your task in this kata is to implement a function that calculates the sum of the integers 
# inside a string. For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy 
# dog", the sum of the integers is 3635.

def sum_of_integers_in_string(s):
    res = []
    r = ""
    for i in range(len(s)):
        if s[i].isdigit():
            r += s[i]
        else:
            res.append(r)
            r = ""
    res.append(r)
    res_l = [int(i) for i in res if i.isdigit()]
    r = 0
    for i in res_l:
        r += i 
    return r


# TASK - The Office IV - Find a Meeting Room

# In this kata, you will be given an array. Each value represents a meeting room. Your 
# job? Find the first empty one and return its index (N.B. There may be more than one empty 
# room in some test cases). 

def meeting(rooms):
    try:
        return min([rooms.index(i) for i in rooms if i == "O"])
    except:
        return "None available!"


# TASK - Who is the killer?

# Given a dictionary with all the names of the suspects and everyone that they have seen on that day

def killer(suspect_info, dead):
    res = []
    for suspect in suspect_info:
        count = 0
        for people in dead:
            if people in suspect_info[suspect]:
                count += 1
        res.append(count)
    keys = list(suspect_info.keys())
    return keys[res.index(len(dead))]


# TASK - String matchup

# Given two arrays of strings, return the number of times each string of the second array appears in the 
# first array.

def solve(a,b):
    res = []
    for i in b:
        res.append(a.count(i))
    return res


# TASK - Holiday III - Fire on the boat

# You will be provided a string that lists many boat related items. If any of these items are "Fire" you must spring into 
# action. Change any instance of "Fire" into "~~". Then return the string.

def fire_fight(s):
    res = []
    for i in s.split():
        if i == "Fire":
            res.append("~~")
        else:
            res.append(i)
    return " ".join(res)


# TASK - Narcissistic Numbers 

# A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original 
# number. If this seems confusing, refer to the example below.
# Ex: 153, where n = 3 (number of digits in 153)
# 13 + 53 + 33 = 153

def is_narcissistic(i):
    return sum([int(e) ** len(str(i)) for e in str(i)]) == i


# TASK - Life Path Number

# A person's Life Path Number is calculated by adding each individual number in that person's date of birth, until it is 
# reduced to a single digit number.

def life_path_number(birthdate):
    year = birthdate.split("-")[0]
    month = birthdate.split("-")[1]
    date = birthdate.split("-")[2]
    while len(year) != 1:
        temp = sum([int(i) for i in year])
        year = str(temp)
    while len(month) != 1:
        temp = sum([int(i) for i in month])
        month = str(temp)
    while len(date) != 1:
        temp = sum([int(i) for i in date])
        date = str(temp)
    result = int(year) + int(month) + int(date)
    while len(str(result)) != 1:
        temp = sum([int(i) for i in str(result)])
        result = str(temp)
    return int(result)


# TASK - SevenAte9

# Write a function that removes every lone 9 that is inbetween 7s.

def seven_ate9(str_):
    for i in range(len(str_) // 3):
        temp = str_.replace("797", "77")
        str_ = temp
    return str_


# TASK - Valid Phone Number

# Write a function that accepts a string, and returns true if it is in the form 
# of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

def validPhoneNumber(phoneNumber):
    if not phoneNumber[0] == "(":
        return False
    if not phoneNumber[4] == ")":
        return False
    if not phoneNumber[5] == " ":
        return False
    if not phoneNumber[9] == "-":
        return False
    return True


# TASK - Make the Deadfish swim

# Write a simple parser that will parse and run Deadfish.
# Deadfish has 4 commands, each 1 character long:
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

def parse(data):
    res = []
    data_res = 0
    for i in data:
        if i == "i":
            data_res += 1
        elif i == "d":
            data_res -= 1
        elif i == "s":
            data_res **= 2
        elif i == "o":
            res.append(data_res)
    return res


# TASK - Sums of Parts

# The function parts_sums (or its variants in other languages) 
# will take as parameter a list ls and return a list of the sums of its parts as defined above.

def parts_sums(ls):
    if ls == []:
        return [0]
    else:
        c = 0
        calc = sum(ls)
        res = [calc]
        for i in range(len(ls) - 1):
            temp = calc - ls[c] 
            res.append(temp)
            calc = temp
            c += 1
        res.append(0)
        return res


# TASK - Matrix Addition

# Write a function that accepts two square matrices (N x N two dimensional arrays), and return the sum 
# of the two. Both matrices being passed into the function will be of size N x N (square), containing only integers.

def matrix_addition(a, b):
    res = []
    for l in range(len(a)):
        res_l = []
        for i in range(len(a[0])):
            res_l.append(a[l][i] + b[l][i])
        res.append(res_l)
    return res


# TASK - Playing with passphrases

# Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they 
# can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:
#choose a text in capital letters including or not digits and non alphabetic characters,
# shift each letter by a given number but the transformed letter must be a letter (circular shift),
# replace each digit by its complement to 9,
# keep such as non alphabetic and non digit characters,
# downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# reverse the whole result

def play_pass(s, n):
    res = ""
    c = 0
    for i in s:
        if i.isalpha():
            let = ""
            if (ord(i.lower()) + n) in range(97, 123):
                let = chr(ord(i) + n)
            else:
                let = chr(ord(i) + n - 122 + 96)
            if c % 2 == 0:
                res += let.upper()
            else:
                res += let.lower()
            
        elif i.isdigit():
            res += str(9 - int(i))
        else:
            res += i
        c += 1
    return res[::-1]


# TASK - The Vowel Code

# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according 
# to the following pattern:
# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5

# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern 
# shown above.

def encode(st):
    res = ""
    vowels = "aeiou"
    for i in st:
        if i in vowels:
            if i.islower():
                res += str(vowels.index(i) + 1)
        else:
            res += i
    return res

def decode(st):
    res = ""
    vowels = "aeiou"
    for i in st:
        if i.isdigit():
            res += vowels[int(i) - 1]
        else:
            res += i
    return res


# TASK - Consonant value

# Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. 
# Consonants are any letters of the alphabet except "aeiou".
# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

def solve(s):
    res_l = []
    res = 0
    vowels = "aeiou"
    for i in s:
        if not i in vowels:
            res += (ord(i) - 96)
        else:
            res = 0
        res_l.append(res)
    return max(res_l)


# TASK - Word a10n (abbreviation)

# The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and 
# trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.
# Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an 
# abbreviation, following these rules:
# A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") 
# will split up a series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. 
# "elephant ride" => "e6t r2e").

def abbreviate(s):
    l = []
    word = ""
    res = ""
    for i in s:
        if i.isalpha():
            word += i
        else:
            l.append(word)
            l.append(i)
            word = ""
    l.append(word)
    for e in l:
        if len(e) >= 4:
            res += e[0] + str(len(e) - 2) + e[-1]
        else:
            res += e
    return res


# TASK - Data Reverse

# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed
# The total number of bits will always be a multiple of 8.

def data_reverse(data):
    res = []
    c = 0
    for i in range (len(data) // 8):
        for e in data[c : c + 8][::-1]:
            res.append(e)
        c += 8
    return res[::-1]


# TASK - Meeting

# Could you make a program that
# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between 
# parentheses separated by a comma.

def meeting(s):
    l = []
    l_res = []
    res = ""
    for i in s.split(";"):
        l.append(i)
    print(l)
    for e in l:
        l_res.append(f'{e.split(":")[1].upper()} {e.split(":")[0].upper()}')
    for t in sorted(l_res):
        res += (f'({t.split()[0]}, {t.split()[1]})')
    return res


# TASK - Multiplication table

# Your task, is to create NxN multiplication table, of size provided in parameter.

def multiplication_table(size):
    c = 1
    res = []
    for i in range(size):
        l = []
        for e in range(1, size + 1):
            l.append(c * e)
        c += 1
        res.append(l)
    return res


# TASK - Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.

def encrypt_this(text):
    res = []
    for i in text.split():
        if len(i) == 1:
            res.append(str(ord(i)))
        elif len(i) == 2:
            res.append(str(ord(i[0])) + i[1:])
        elif len(i) == 3:
            res.append(str(ord(i[0])) + i[-1] + i[1])
        else:
            res.append(str(ord(i[0])) + i[-1] + i[2:-1] + i[1])
    return " ".join(res)


# TASK - Largest pair sum in array

# Given a sequence of numbers, find the largest pair sum in the sequence.

def largest_pair_sum(numbers): 
    res = 0
    for i in range(2):
        res += max(numbers)
        numbers.remove(max(numbers))
    return res


# TASK - Average Scores

# Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number. You are 
# not allowed to use any loops (including for, for/in, while, and do/while loops).

def average(array):
    return round(sum(array) / len(array))


# TASK - Evens times last

# Given a sequence of integers, return the sum of all the integers that have an even index, multiplied by the integer at the last index. 

def even_last(numbers): 
    res = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            res += numbers[i] * numbers[-1]
    return res


# TASK - Letterbox Paint-Squad

# Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.

def paint_letterboxes(start, finish):
    l = []
    for number in range(start, finish + 1):
        for i in str(number):
            l.append(int(i))
    c = 0
    result_l = []
    while c != 10:
        result_l.append(l.count(c))
        c += 1
    return result_l


# TASK - 16+18=214

# In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)

def add(num1, num2):
    first_num = [int(i) for i in str(num1)][::-1]
    second_num = [int(i) for i in str(num2)][::-1]
    m = 0
    if len(str(num1)) > len(str(num2)):
        m = len(str(num2))
    else:
        m = len(str(num1))
    c = 0
    res_l = []
    for i in range(m):
        res_l.append(str(first_num[c] + second_num[c]))
        c += 1
    more_nums = ""
    if len(str(num1)) > len(str(num2)):
        more_nums = str(num1)[:len(str(num1)) - len(str(num2))]
    elif len(str(num1)) < len(str(num2)):
        more_nums = str(num2)[:len(str(num2)) - len(str(num1))]
    return int(more_nums + "".join(res_l[::-1]))


# TASK - Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages

# You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next 
# coding meetup that you are organising.
# Your task is to return an object (associative array in PHP) which includes the count of each coding language represented at the meetup.

def count_languages(lst): 
    l = []
    for d in lst:
        l.append(d['language'])
    res_d = {}
    for i in l:
        res_d[i] = l.count(i)
    return res_d


# TASK - Debug Sum of Digits of a Number

# Debug   function getSumOfDigits that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.

def get_sum_of_digits(num):
    return sum([int(i) for i in str(num)])


# TASK - Minimum Steps (Array Series #6)

# Given an array of N integers, you have to find how many times you have to add up the smallest numbers in the array until their 
# Sum becomes greater or equal to K.

def minimum_steps(numbers, value):
    result = 0
    m = min(numbers)
    numbers.remove(min(numbers))
    c = 0
    while m < value:
        m += min(numbers)
        numbers.remove(min(numbers))
        result += 1
    return result


# TASK - Drone Fly-By

# You will be given two strings: lamps and drone. lamps represents a row of lamps, currently off, each represented by x. When these lamps are 
# on, they should be represented by o.
# The drone string represents the position of the drone T (any better suggestion for character??) and its flight path up until this point =. 
# The drone always flies left to right, and always begins at the start of the row of lamps. Anywhere the drone has flown, including its 
# current position, will result in the lamp at that position switching on.

def fly_by(lamps, drone):
    print(lamps, drone)
    on = len(drone) * "o"
    if len(lamps) > len(drone):
        return on + (len(lamps) - len(drone)) * "x"
    else:
        return len(lamps) * "o"


# TASK - Band name generator

# My friend wants a new band name for her band. She like bands that use the formula: "The" + a noun with the first letter capitalized.
# However, when a noun STARTS and ENDS with the same letter, she likes to repeat the noun twice and connect them together with the first 
# and last letter, combined into one word (WITHOUT "The" in front)

def band_name_generator(name):
    return f"The {name.capitalize()}" if name[0] != name[-1] else name.capitalize() + name[1:]


# TASK - Numbers with this digit inside

# You have to search all numbers from inclusive 1 to inclusive a given number x, that have the given digit d in it.
# The value of d will always be 0 - 9.
# The value of x will always be greater than 0.
# You have to return as an array
# the count of these numbers,
# their sum
# and their product.

def numbers_with_digit_inside(x, d):
    l = []
    for i in range(1, x + 1):
        if str(d) in str(i):
            l.append(i)
    lis = []
    p = 1
    for i in l:
        p *= i
        lis.append(p)
    if len(lis) == 0:
        product = 0
    else:
        product = max(lis)
    return [len(l), sum(l), product]


# TASK - Scaling Squared Strings

# You are given a string of n lines, each substring being n characters long. 
# A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').\
# A v-vertical scaling of a string consists of replicating v times each part of the squared string.
# Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

def scale(strng, k, v):
    if strng == "":
        return ""
    else:
        result = []
        for i in strng.split("\n"):
            word = ""
            for e in i:
                word += e * k
            for i in range(v):
                result.append(word)
        return "\n".join(result)


# TASK - Broken sequence

# You receive some random elements as a space-delimited string. Check if the elements are part of an ascending sequence of integers starting with 1, with an increment of 1 (e.g. 1, 2, 3, 4).
#Return:
# 0 if the elements can form such a sequence, and no number is missing ("not broken", e.g. "1 2 4 3")
# 1 if there are any non-numeric elements in the input ("invalid", e.g. "1 2 a")
# n if the elements are part of such a sequence, but some numbers are missing, and n is the lowest of them ("broken", e.g. "1 2 4" or "1 5")

def find_missing_number(sequence):
    if sequence == "":
        return 0
    else:
        count = 1
        l = []
        for i in sequence.split(" "):
            try:
                l.append(int(i))
            except:
                return 1
        compare = [i for i in range(1, max(l) + 1)]
        res = []
        for i in compare:
            if not i in l:
                res.append(i)
        if len(res) == 0:
            return 0
        else:
            return min(res)


# TASK - Help the Fruit Guy

# Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace all the rotten 
# pieces of fruit with fresh ones. For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. 
# Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings where all the 
# rotten fruits are replaced by good ones. 

def remove_rotten(bag_of_fruits):
    if bag_of_fruits:
        l = []
        for i in bag_of_fruits:
            for e in i.split("rotten"):
                l.append(e.lower())
        res = []
        for i in l:
            if len(i) > 0:
                res.append(i)
        return res
    else:
        return []


# TASK - Thinkful - List Drills: Longest word

# Complete the function that takes one argument, a list of words, and returns the length of the longest word in the list.

def longest(words):
    return max([len(i) for i in words])


# TASK - Selective fear of numbers

# I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated: The number I'm afraid of depends on which day of 
# the week it is... This is a concrete description of my mental illness:
# Monday --> 12
# Tuesday --> numbers greater than 95
# Wednesday --> 34
# Thursday --> 0
# Friday --> numbers divisible by 2
# Saturday --> 56
# Sunday --> 666 or -666
# Write a function which takes a string (day of the week) and an integer (number to be tested) so it tells the doctor if I'm afraid or 
# not. (return a boolean)

def am_I_afraid(day,num):
    if day == "Monday" and num == 12:
        return True
    elif day == "Tuesday" and num > 95:
        return True
    elif day == "Wednesday" and num == 34:
        return True
    elif day == "Thursday" and num == 0:
        return True
    elif day == "Friday" and num % 2 == 0:
        return True
    elif day == "Saturday" and num == 56:
        return True
    elif day == "Sunday" and abs(num) == 666:
        return True
    else:
        return False


# TASK - Product Array (Array Series #5)

# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the 
# elements of Arr[] except Arr[i]. 

def product_array(numbers):
    count = 0
    result = []
    for i in range(len(numbers)):
        res = 1
        for e in range(len(numbers)):
            if e != count:
                res *= numbers[e]
        count += 1
        result.append(res)
    return result


# TASK - Enumerable Magic #5- True for Just One?

# Create a function called one that accepts two params:
# a sequence
# a function
# and returns true only if the function in the params returns true for exactly one (1) item in the sequence. 

def one(sq, fun): 
    res = 0
    for i in sq:
        if fun(i):
            res += 1
    if res == 1:
        return True
    else:
        return False


# TASK - Exclamation marks series #13: Count the number of exclamation marks and question marks, return the product

# Count the number of exclamation marks and question marks, return the product.

def product(s):
    return s.count("!") * s.count("?")


# TASK - Help Suzuki rake his garden!

# The monastery has a magnificent Zen garden made of white gravel and rocks and it is raked diligently 
# everyday by the monks. Suzuki having a keen eye is always on the lookout for anything creeping into 
# the garden that must be removed during the daily raking such as insects or moss.
# You will be given a string representing the garden.
# Rake out any items that are not a rock or gravel and replace them with gravel.

def rake_garden(garden):
    res = []
    for i in garden.split():
        if i == "gravel" or i == "rock":
            res.append(i)
        else:
            res.append("gravel")
    return " ".join(res)


# TASK - Double Sort

# Your job is to return a single array that has first the numbers sorted in ascending order, followed by 
# the strings sorted in alphabetic order. The values must maintain their original type.

def db_sort(arr): 
    numbers = [i for i in arr if type(i) == int]
    strings = [i for i in arr if type(i) == str]
    return sorted(numbers) + sorted(strings)


# TASK - Correct the time-string

# You have to create a method, that corrects a given time string.
# There was a problem in addition, so many of the time strings are broken.
# Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.

def time_correct(t):
    if t == "":
        return ""
    elif t == None:
        return None
    elif not t.count(":") == 2:
        return None
    else:
        for i in t.split(":"):
            if not i.isdigit() or not len(i) == 2:
                return None
        all_seconds = (int(t.split(":")[0]) * 3600) + (int(t.split(":")[1]) * 60) + (int(t.split(":")[2]))
        hours = all_seconds // 3600
        check_hours = 0
        if hours > 24:
            check_hours = round((hours / 24 - hours // 24) * 24)
        else:
            check_hours = hours
        minutes = int((all_seconds / 3600 - hours) * 60)
        seconds = all_seconds - hours * 3600 - minutes * 60 
        f_hours = ""
        f_minutes = ""
        f_seconds = ""
        if check_hours == 24:
            f_hours = "00"
        elif check_hours < 10:
            f_hours = "0" + str(check_hours)
        else:
            f_hours = str(check_hours)
        if minutes < 10:
            f_minutes = "0" + str(minutes)
        else:
            f_minutes = str(minutes)
        if seconds < 10:
            f_seconds = "0" + str(seconds)
        else:
            f_seconds = str(seconds)
        return f_hours + ":" + f_minutes + ":" + f_seconds


# TASK - Hungarian Vowel Harmony (easy)

# Your goal is to create a function dative() (Dative() in C#) which returns the valid form of a valid Hungarian word w in dative 
# case i. e. append the correct suffix nek or nak to the word w based on vowel harmony rules.

def dative(word):
    front_vowel = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    back_vowel = ["a", "á", "o", "ó", "u", "ú"]
    res_front = 0
    res_back = 0
    for i in word:
        if i in front_vowel:
            res_front += 1
        elif i in back_vowel:
            res_back += 1
    if res_front > res_back:
        return word + "nek"
    else:
        return word + "nak"


# TASK - Find all pairs

# You are given array of integers, your task will be to count all pairs in that array and return their count.

def duplicates(arr):
    res_d = {}
    res = 0
    for i in arr:
        res_d[i] = arr.count(i)
    for e in res_d:
        res += res_d[e] // 2
    return res


# TASK - Consecutive letters

# In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs 
# only once. 

def solve(st):
    alphabet = [chr(i) for i in range(97, 123)]
    indx = alphabet.index(sorted(st)[0])
    print(indx)
    print(sorted(st))
    res = []
    for i in sorted(st):
        if i == alphabet[indx]:
            res.append(1)
            indx += 1
        else:
            res.append(0)
            indx += 1
    print(res)
    if 0 in res:
        return False
    else:
        return True


# TASK - Max-min arrays

# In this Kata, you will be given an array of unique elements, and your task is to rearrange the values so that the first 
# max value is followed by the first minimum, followed by second max value then second min value, etc. 

def solve(arr):
    count = 1
    res = []
    for i in range(len(arr)):
        if count % 2 == 0:
            res.append(min(arr))
            arr.remove(min(arr))
            count += 1
        else:
            res.append(max(arr))
            arr.remove(max(arr))
            count += 1
    return res


# TASK - Do you speak retsec?

# You're given a single word. Your task is to swap the halves. If the word has an uneven length, leave the character in the middle at 
# that position and swap the chunks around it.

def reverse_by_center(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2:] + s[:len(s) // 2]
    else:
        return s[len(s) // 2 + 1: ] + s[len(s) // 2] + s[:len(s) // 2]


# TASK - Return String of First Characters

# In this exercise, a string is passed to a method and a new string has to be returned with the first character of each word in the string.

def make_string(s):
    res = ""
    for i in s.split():
        res += i[0]
    return res


# TASK - Move 10

# Move every letter in the provided string forward 10 letters through the alphabet.
# If it goes past 'z', start again at 'a'.
# Input will be a string with length > 0.

def move_ten(st):
    res = ""
    for i in st:
        if ord(i) + 10 in range(97, 123):
            res += chr(ord(i) + 10)
        else:
            res += chr((ord(i) + 10 - 123) + 97)
    return res


# TASK - Simple Fun #3: Late Ride

# One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the 
# length of your ride, in minutes. Off you go to explore the neighborhood.
# When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! 
# Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n 
# minutes have passed since 00:00.
# Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

def late_ride(n):
    h = 0
    m = 0
    if n % 60  == 0:
        h += (n // 60)
    else:
        h += (n // 60)
        m += (n - ((n // 60) * 60))
    res = str(h) + str(m)
    return sum([int(i) for i in res])


# TASK - Digits explosion

# Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value. 

def explode(s):
    res = ""
    for i in s:
        res += i * int(i)
    return res


# TASK - This is odd

# Create a function that checks if a number is odd.
# Expect negative and decimal numbers too. Remember... all negative numbers can also be either odd or even.
# Decimal numbers always return false 

def is_odd(n):
    if type(n) == float:
        if int(n) == 0:
            return False
        elif abs(n) % int(n) != 0:
            return False
        else:
            return abs(n) % 2 != 0
    else:
        return abs(n) % 2 != 0


# TASK - Complete The Pattern #6 - Odd Ladder

# You have to write a function pattern which creates the following pattern (see examples) up to the desired number of rows.
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
# If any even number is passed as argument then the pattern should last upto the largest odd number which is smaller than the passed even number.

def pattern(n):
    if n <= 0:
        return ""
    else:
        res = []
        final = 0
        if n % 2 == 0:
            final = n - 1
        else:
            final = n
        for i in range(1, final + 1):
            if i % 2 != 0:
                res.append(str(i) * i)
    return "\n".join(res)


# TASK - Running out of space

# Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the 
# space decreasing. For example, running this function on the array ['i', 'have','no','space'] would produce 
# ['i','ihave','ihaveno','ihavenospace'].

def spacey(array):
    res = []
    count = 1
    for i in range(len(array)):
        res.append("".join(array[:count]))
        count += 1
    return res


# TASK - Scrabble Score

# Write a program that, given a word, computes the scrabble score for that word.

def scrabble_score(st): 
    res = 0
    d = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP":  3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10
    }
    for i in st.upper():
        for e in d:
            if i in e:
                res += d[e]
    return res


# TASK - Find all non-consecutive numbers

# Your task is to find all the elements of an array that are non consecutive.
# A number is non consecutive if it is not exactly one larger than the previous element in the array. The first element gets a pass and 
# is never considered non consecutive.

def all_non_consecutive(arr):
    res = []
    count = min(arr)
    for i in arr:
        d = {}
        if i != count:
            d["i"] = arr.index(i)
            d["n"] = i
            count = i
            res.append(d)
        count += 1
    return res


# TASK - Sort arrays - 1

# Just a simple sorting usage. Create a function that returns the elements of the input-array / list sorted in lexicographical order.

def sortme(names):
    return sorted(names)


# TASK - Gauß needs help! (Sums of a lot of numbers).

# Due to another of his misbehaved, the primary school's teacher of the young Gauß, Herr J.G. Büttner, to keep the bored and 
# unruly young schoolboy Karl Friedrich Gauss busy for a good long time, while he teaching arithmetic to his mates, assigned him 
# the problem of adding up all the whole numbers from 1 through a given number n.
#Your task is to help the young Carl Friedrich to solve this problem as quickly as you can; so, he can astonish his teacher and 
# rescue his recreation interval.

def f(n):
    try:
        if n:
            if n >= 0:
                res = 0
                for i in range(1, n+1):
                    res += i
                return res
            else:
                return None
    except:
        return None


# TASK - Factorial Factory

# In mathematics, the factorial of integer 'n' is written as 'n!'. It is equal to the product of n and every integer preceding it. For 
# example: 5! = 1 x 2 x 3 x 4 x 5 = 120
# Your mission is simple: write a function that takes an integer 'n' and returns 'n!'.
# You are guaranteed an integer argument. For any values outside the positive range, return null, nil or None .

def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        res = 1
        for i in range(1, n+1):
            res *= i
        return res
    else:
        return None


# TASK - Complete The Pattern #4

# You have to write a function pattern which creates the following pattern upto n number of rows. If the Argument is 0 or a 
# Negative Integer then it should return "" i.e. empty string.

def pattern(n):
    res = []
    count = 1
    for i in range(n):
        temp = "".join([str(i) for i in range(count, n+1)])
        res.append(temp)
        count += 1
    return "\n".join(res)


# TASK - Computer problem series #1: Fill the Hard Disk Drive

# Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive. The files must be saved 
# in the order they appear in the queue. 

def save(sizes, hd): 
    res = 0
    count = 0
    count_res = 0
    step = 0
    if sum(sizes) <= hd:
        return len(sizes)
    else:
        while res <= hd:
            res += sizes[step]
            step += 1
            count_res = count
            count += 1
        return count_res


# TASK - Arithmetic progression

# In your class, you have started lessons about arithmetic progression. Since you are also a programmer, you have decided to write a 
# function that will return the first n elements of the sequence with the given common difference d and first element a. Note that the 
# difference may be zero!

def arithmetic_sequence_elements(a, r, n):
    count = 0
    res = []
    temp = a
    while count != n:
        res.append(str(temp) + ",")
        temp += r
        count += 1
    return " ".join(res)[:-1]


# TASK - The Office II - Boredom Score

# You will be provided with an object(staff) containing the staff names as keys, and the department they work in as values.
# Each department has a different boredom assessment score.
# Depending on the cumulative score of the team, return the appropriate sentiment

def boredom(staff):
    d = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25
    }
    res = 0
    for i in staff:
        res += d[staff[i]]
    if res <= 80:
        return "kill me now"
    elif res in range(81, 100):
        return "i can handle this"
    else:
        return "party time!!"


# TASK - Simple string reversal II

# In this Kata, you will be given a string and two indexes (a and b). Your task is to reverse the portion of that string between those two 
# indices inclusive. 

def solve(st,a,b):
    res_before = ""
    res_middle = ""
    res_after = ""
    for i in range(len(st)):
        if i < a:
            res_before += st[i]
        elif i > b:
            res_after += st[i]
        else:
            res_middle += st[i]
    return res_before + res_middle[::-1] + res_after


# CODEWARS TEST EXERCISES

# TASK - Rearrange Number to Get its Maximum

# Create a function that takes one positive three digit integer and rearranges 
# its digits to get the maximum possible number. Assume that the argument 
# is an integer. Return null (nil for Ruby, nothing for Julia) if the argument is not valid.

def max_redigit(num):
	if len(str(num)) == 3:
		if num < 0:
			return None
		else:
			return int("".join(sorted(str(num), reverse=True)))
	else:
		return None


# TASK - V A P O R C O D E

# Write a function that converts any sentence into a V A P O R W A V E 
# sentence. a V A P O R W A V E sentence converts all the letters into 
# uppercase, and adds 2 spaces between each letter (or special character)
# to create this V A P O R W A V E effect.

def vaporcode(s):
	res = []
	for i in s:
		if i != " ":
			res.append(i.upper())
	return "  ".join(res)


# TASK - Even or Odd - Which is Greater?

# Given a string of digits confirm whether the sum of all the individual
# even digits are greater than the sum of all the indiviudal odd digits. 
# Always a string of numbers will be given.

def even_or_odd(s):
	even = 0
	odd = 0
	for i in s:
		if int(i) % 2 == 0:
			even += int(i)
		else:
			odd += int(i)
	if even > odd:
		return "Even is greater than Odd"
	elif odd > even:
		return "Odd is greater than Even"
	else:
		return "Even and Odd are the same"


# TASK - Check for prime numbers

# In this kata you will create a function to check a non-negative input 
# to see if it is a prime number.
# The function will take in a number and will return True if it is a 
# prime number and False if it is not.
# A prime number is a natural number greater than 1 that has no positive
# divisors other than 1 and itself.

def is_prime(n):
	flag = False
	if n > 1:
		for i in range(2, int(n / 2) + 1):
			if (n % i) == 0:
				flag = True
				break
	else:
		flag = True
	if flag:
		return False
	else:
		return True


# TASK - Is n divisible by (...)?

# Create a function isDivisible(n,...) that checks if the first 
# argument n is divisible by all other arguments (return true if no 
# other arguments)

def is_divisible(*kwargs):
	res = []
	flag = False
	for i in kwargs[1:]:
		if not kwargs[0] % i == 0:
			flag = True
			break
	if flag:
		return False
	else:
		return True


# TASK - Gradually Adding Parameters

# This kata is all about adding numbers.
# You will create a function named add. This function will return the 
# sum of all the arguments. Sounds easy, doesn't it??
# Well here's the twist. The inputs will gradually increase with their 
# index as parameter to the function.

def add(*args):
	res = 0
	for i in range(len(args)):
		res += args[i] * (i + 1)
	return res


# TASK - Plus - minus - plus - plus - ... - Count

# Count how often sign changes in array.

def catch_sign_change(lst):
	if len(lst) == 0:
		return 0
	else:
		res = 0
		var = "neg"
		if lst[0] >= 0:
			var = "pos"
		for i in lst[1:]:
			t = "neg"
			if i >= 0:
				t = "pos"
			if t != var:
				res += 1
			var = t
		return res


# TASK - Replace every nth

# Write a method, that replaces every nth char oldValue with char newValue.

def replace_nth(text, n, old, new):
	if n <= 0:
		return text
	else:
		res = ""
		count = 0
		for letter in text:
			if letter == old:
				count += 1
				if count % n == 0:
					res += new
				else:
					res += letter
			else:
				res += letter
		return res


# TASK - Homogenous arrays

# Given a two-dimensional array, return a new array which carries 
# over only those arrays from the original, which were not empty and 
# whose items are all of the same type (i.e. homogenous). For simplicity, 
# the arrays inside the array will only contain characters and integers.

def filter_homogenous(arrays):
	l = []
	res = []
	for arr in arrays:
		if len(arr) > 0:
			if len(arr) == 1:
				res.append(arr)
			else:
				temp_res = 1
				temp = type(arr[0])
				for i in arr[1:]:
					if type(i) == temp:
						temp_res += 1
				if temp_res == len(arr):
					res.append(arr)
	return res


# TASK - The Office III - Broken Photocopier

# The bloody photocopier is broken... Just as you were sneaking around 
# the office to print off your favourite binary code!
# Instead of copying the original, it reverses it: '1' becomes '0' and 
# vice versa.
# Given a string of binary, return the version the photocopier gives you
# as a string.

def broken(inp):
	res = ""
	for i in inp:
		if i == "0":
			res += "1"
		else:
			res += "0"
	return res


# TASK - Check three and two

# Given an array with exactly 5 strings "a", "b" or "c" (chars in 
# Java, characters in Fortran), check if the array contains three and 
# two of the same values.

def check_three_and_two(array):
	res_d = {}
	for i in array:
		res_d[i] = array.count(i)
	if len(res_d) == 2:
		l = []
		for i in res_d:
			l.append(res_d[i])
		if 3 in l and 2 in l:
			return True
		else:
			return False
	else:
		return False


# TASK - L2: Triple X

# Given a string, return true if the first instance of "x" in the 
# string is immediately followed by the string "xx". 

def triple_x(s):
	if s == "":
		return False
	else:
		if not "x" in s:
			return False
		else:
			indx = s.index("x")
			if s[indx:indx+3] == "xxx":
				return True
			else:
				return False


# TASK - Thinkful - List and Loop Drills: Inverse Slicer

# write a function inverse_slice() that takes three arguments: a list 
# items, an integer a and an integer b. The function should return a 
# new list with the slice specified by items[a:b]

def inverse_slice(items, a, b):
	res = []
	for i in range(len(items)):
		if not i in range(a, b):
			res.append(items[i])
	return res


# TASK - Filter unused digits

# Given a list of integers, return the digits that are not present in any of them.

def unused_digits(*args):
	res = []
	l = []
	for i in args:
		for e in str(i):
			l.append(int(e))
	compare_var = [i for i in range(0, 10)]
	for i in compare_var:
		if not i in l:
			res.append(i)
	res_str = ""
	for i in sorted(res):
		res_str += str(i)
	return res_str


# TASK - Count the Characters
 
# The goal of this kata is to write a function that takes two inputs: a
# string and a character. The function will count the number of times 
# that character appears in the string. The count is case insensitive.

def count_char(str, char):
	return str.lower().count(char.lower())


# TASK - Hit Count

# As a step towards achieving this; you have decided to create a 
# function that will produce a multi-dimensional array out of the hit 
# count value. Each inner dimension of the array represents an individual
# digit in the hit count, and will include all numbers that come before 
# it, going back to 0.

def counter_effect(hit_count):
	res = []
	for i in hit_count:
		l = []
		for e in range(0, int(i) + 1):
			l.append(e)
		res.append(l)
	return res


# TASK - Odder Than the Rest

# Create a method that takes an array/list as an input, and outputs the 
# index at which the sole odd number is located.

def odd_one(arr):
	res = -1
	for i in arr:
		if i % 2 != 0:
			res = arr.index(i)
			break
	return res


# TASK - Elevator Distances

# Given an array representing a series of floors you must reach by 
# elevator, return an integer representing the total distance travelled 
# for visiting each floor in the array in order. 

def elevator_distance(array):
	count = 0
	res = 0
	for i in range(len(array) - 1):
		res += (max(array[count : count + 2]) - min(array[count : count + 2]))
		count += 1
	return res


# TASK - Borrower Speak

# The borrowers are tiny tiny fictional people. As tiny tiny people they
# have to be sure they aren't spotted, or more importantly, stepped on.
# As a result, the borrowers talk very very quietly. They find that 
# capitals and punctuation of any sort lead them to raise their voices 
# and put them in danger. 

def borrow(s):
	res = ""
	for i in s:
		if ord(i.lower()) in range(97, 123):
			res += i.lower()
	return res


# TASK - Email Address Obfuscator

# write a function that takes an email address string and returns the 
# obfuscated version as a string that replaces the characters @ and . 
# with [at] and [dot], respectively.

def obfuscate(email):
	res = email.replace("@", " [at] ")
	res2 = res.replace(".", " [dot] ")
	return res2


# TASK - Consecutive items

# ou are given a list of unique integers arr, and two integers a and b. 
# Your task is to find out whether or not a and b appear consecutively 
# in arr, and return a boolean value (True if a and b are consecutive, 
# False otherwise). 

def consecutive(arr, a, b):
	if arr.index(a) + 1 == arr.index(b) or arr.index(b) + 1 == arr.index(a):
		return True
	else:
		return False


# TASK - Sum - Square Even, Root Odd

# Complete the function that takes a list of numbers (nums), as the only
# argument to the function. Take each number in the list and square it 
# if it is even, or square root the number if it is odd. Take this new 
# list and return the sum of it, rounded to two decimal places.

import math
def sum_square_even_root_odd(nums):
	res = []
	for i in nums:
		if i % 2 == 0:
			res.append(i ** 2)
		else:
			res.append(math.sqrt(i))
	return round(sum(res), 2)


# TASK - Hells Kitchen

# Obviously the words should be Caps, Every word should end with '!!!!', 
# Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.

def gordon(a):
	res = []
	vowels = "eiou"
	for i in a.split():
		strng = ""
		for e in i:
			if e in vowels:
				strng += "*"
			elif e.lower() == "a":
				strng += "@"
			else:
				strng += e.upper()
		res.append(strng + "!!!!")
	return " ".join(res)


# TASK - Coding Meetup #11 - Higher-Order Functions Series - Find the average age

# You will be given a sequence of objects representing data about 
# developers who have signed up to attend the next coding meetup that 
# you are organising.

def get_average(lst): 
	res = 0
	for i in lst:
		res += i["age"]
	return round(res / len(lst))


# TASK - Calculate mean and concatenate string

# Return an array of length 2 with a[0] representing the mean of the 
# ten integers as a floating point number. There will always be 10 
# integers and 10 characters. Create a single string with the characters
# and return it as a[1] while maintaining the original order.

def mean(lst):
	char = ""
	count = 0
	nums = 0
	for i in lst:
		if i.isalpha():
			char += i
		else:
			nums += int(i)		
	return [round(nums / 10, 1), char]


# TASK - Pandemia

# You would be given a map of the world in a type of string:
# string s = "01000000X000X011X0X"
# '0' : uninfected
# '1' : infected
# 'X' : ocean
# Your task is to find the percentage of human population that got 
# infected in the end.

def infected(s):
	if not "1" in s:
		return 0
	else:
		res = []
		for i in s.split("X"):
			if "1" in i:
				res.append("1" * len(i))
			elif i == "":
				res.append("X")
			else:
				res.append(i)
		return 100 * "X".join(res).count("1") / (len(s) - s.count("X"))


# TASK - Who's Online?

# Given an input of an array of objects containing usernames, status 
# and time since last activity (in mins), create a function to work out 
# who is online, offline and away.

def who_is_online(friends):
	online = []
	offline = []
	away = []
	for i in friends:
		if i["status"] == "online":
			if i["last_activity"] <= 10:
				online.append(i["username"])
			else:
				away.append(i["username"])
		else:
			offline.append(i["username"])
	res = {}
	if len(online) > 0:
		res["online"] = online
	if len(offline) > 0:
		res["offline"] = offline
	if len(away) > 0:
		res["away"] = away
	return res
	

# TASK - Initialize my name

# Some people just have a first name; some people have first and last 
# names and some people have first, middle and last names.
# You task is to initialize the middle names (if there is any).

def initialize_names(name):
	if len(name.split()) <= 2:
		return name
	elif len(name) > 2:
		res = []
		for i in name.split()[1:-1]:
			res.append(i[0]  + ".")
		return name.split()[0] + " " + " ".join(res) + " " + name.split()[-1]


# TASK - Delete occurrences of an element if it occurs more than n times

# Given a list lst and a number N, create a new list that contains each 
# number of lst at most N times without reordering. For example if 
# N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
# drop the next [1,2] since this would lead to 1 and 2 being in the 
# result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

def delete_nth(order,max_e):
	d = {}
	for i in order:
		d[i] = 0
	res = []
	for e in order:
		d[e] += 1
		if d[e] <= max_e:
			res.append(e)
	return res


# TASK - Backspaces in string

# Assume "#" is like a backspace in string. This means that string 
# "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols.

def clean_string(s):
	rev_string = s[::-1] # 'c##d#cba'
	count = s.count("#")
	res = ""
	c = 0
	for i in rev_string:
		if i == "#":
			c += 1
		else:
			if c == 0:
				res += i
			else:
				c -= 1
	return res[::-1] 


# TASK - Highest Rank Number in an Array

# Complete the method which returns the number which is most frequent 
# in the given input array. If there is a tie for most frequent number, 
# return the largest number among them.

def highest_rank(arr):
	d = {}
	for i in arr:
		d[i] = arr.count(i)
	res_v = []
	for i in d.values():
		res_v.append(i)
	res_k = []
	for i in d.keys():
		res_k.append(i)
	if res_v.count(max(res_v)) > 1:
		res_final = []
		count = 0
		maxim = max(res_v)
		for i in res_v:
			if i == maxim:
				res_final.append(count)
			count += 1
		res_f = []
		for i in range(len(res_final)):
			res_f.append(res_k[res_final[i]])
		return max(res_f)
	else:
		return res_k[res_v.index(max(res_v))]


# TASK - Dictionary from two lists

# There are two lists, possibly of different lengths. The first one 
# consists of keys, the second one consists of values. Write a function 
# createDict(keys, values) that returns a dictionary created from keys 
# and values. If there are not enough values, the rest of keys should 
# have a None (JS null)value. If there not enough keys, just ignore the 
# rest of values.

def createDict(keys, values):
	res_d = {}
	for i in range(len(keys)):
		if i in range(len(values)):
			res_d[keys[i]] = values[i]
		else:
			res_d[keys[i]] = None
	return res_d


# TASK - Return the closest number multiple of 10

# Given a number return the closest number to it that is divisible by 10.

def closest_multiple_10(i):
	if (int(i) - (int(i) // 10) * 10) <= 4:
		return (i // 10) * 10
	else:
		return (i // 10) * 10 + 10


# TASK - C.Wars

# Normally we have firstname, middle and the last name but there may be 
# more than one word in a name like a South Indian one.
# Similar to those kinda names we need to initialize the names.

def initials(name):
	rev_name = name.split()[::-1]
	final_res = [rev_name[0].title()]
	for i in rev_name[1:]:
		final_res.append(i[0].upper() + ".")
	return "".join(final_res[::-1])


# TASK - Binary Calculator

# Your task is to write the calculate function so that it will perform 
# the arithmetic and the result returned should be a string representing
# the binary result.

def calculate(n1, n2, o):
	res = 0
	if o == "add":
		res = int(n1, 2) + int(n2, 2)
	elif o == "subtract":
		res = int(n1, 2) - int(n2, 2)
	elif o == "multiply":
		res = int(n1, 2) * int(n2, 2)
	if "-" in str(res):
		return bin(res)[0] + bin(res)[3:]
	else:
		return bin(res)[2:]


# TASK - Sudoku Solution Validator

# Write a function validSolution/ValidateSolution/valid_solution() that 
# accepts a 2D array representing a Sudoku board, and returns true if 
# it is a valid solution, or false otherwise. The cells of the sudoku 
# board may also contain 0's, which will represent empty cells. Boards 
# containing one or more zeroes are considered to be invalid solutions.
# The board is always 9 cells by 9 cells, and every cell only contains 
# integers from 0 to 9.

def valid_solution(board):
	res = "123456789"
	if len(board) != 9:
		return False
	else:
		for line in board:
			if 0 in line:
				return False
				break
			else:
				# verifying rows
				if not "".join([str(i) for i in sorted(line)]) == res:
					return False
					break
		# verifying columns
		for i in range(9):
			res_l = []
			for e in range(9):
				res_l.append(board[e][i])
			if not "".join([str(i) for i in sorted(res_l)]) == res:
				return False
				break
		# verifying 3x3 grids
		col_range = 0
		for e in range(3):
			row_range = 0
			for i in range(3):				
				temp_res = []
				for row in range(row_range, row_range + 3):
					for col in range(col_range, col_range + 3):
						temp_res.append(board[row][col])
				if not "".join(str(i) for i in sorted(temp_res)) == res:
					return False
					break
				row_range += 3	
			col_range += 3
		return True


# TASK - Generate range of integers

# Implement a function named generateRange(min, max, step), which takes 
# three arguments and generates a range of integers from min to max, 
# with the step. The first integer is the minimum value, the second is 
# the maximum of the range and the third is the step. (min < max)

def generate_range(min, max, step):
	res = []
	str = min
	while str <= max:
		res.append(str)
		str += step
	return res


# TASK - Multiplication table for number

# Your goal is to return multiplication table for number that is always 
# an integer from 1 to 10.

def multi_table(number):
	res = []
	for i in range(1, 11):
		res.append("{} * {} = {}".format(i, number, i * number))
	return "\n".join(res)


# TASK - Do you speak "English"? 

# Given a string of arbitrary length with any ascii characters. Write 
# a function to determine whether the string contains the whole 
# word "English".

def sp_eng(sentence): 
	return "english" in sentence.lower()


# TASK - Pyramid Array

# Write a function that when given a number >= 0, returns an Array of 
# ascending length subarrays.

def pyramid(n):
	res = []
	for i in range(1, n + 1):
		temp = []
		for e in range(i):
			temp.append(1)
		res.append(temp)
	return res


# TASK - Grouped by commas

# Finish the solution so that it takes an input n (integer) and returns 
# a string that is the decimal representation of the number grouped by 
# commas after every 3 digits.

def group_by_commas(n):
	if n < 1000:
		return str(n)
	else:
		res = ""
		rev_n = str(n)[::-1]
		for i in range(1, len(rev_n) + 1):
			if i != 1:
				if i % 3 == 0:
					res += rev_n[i - 1]
					res += ","
				else:
					res += rev_n[i - 1]
			else:
				res += rev_n[i - 1]
		if len(rev_n) % 3 == 0:
			return res[::-1][1:]
		else:
			return res[::-1]


# TASK - Merge two sorted arrays into one

# You are given two sorted arrays that both only contain integers. 
# Your task is to find a way to merge them into a single one, sorted 
# in asc order. Complete the function mergeArrays(arr1, arr2), where 
# arr1 and arr2 are the original sorted arrays.

def merge_arrays(arr1, arr2):
	arr1.extend(arr2)
	s = set(arr1)
	return sorted(list(s))


# TASK - Compare within margin

# Create a function close_compare that accepts 3 parameters: a, b, 
# and an optional margin. The function should return whether a is lower 
# than, close to, or higher than b. 

def close_compare(a, b, margin=0):
	if margin >= abs(a - b):
		return 0
	else:
		if a < b:
			return -1
		elif a > b:
			return 1
		else:
			return 0


# TASK - Holiday VI - Shark Pontoon

# You are given 5 variables;
# sharkDistance = distance from the shark to the pontoon. The shark 
# will eat you if it reaches you before you escape to the pontoon.
# sharkSpeed = how fast it can move in metres/second.
# pontoonDistance = how far you need to swim to safety in metres.
# youSpeed = how fast you can swim in metres/second.
# dolphin = a boolean, if true, you can half the swimming speed of the 
# shark as the dolphin will attack it.
# The pontoon, you, and the shark are all aligned in one dimension.
# You need to work out if the shark will get to you before you can get 
# to the pontoon. To make it easier... as you do the mental calculations
# in the water you either freeze when you realise you are dead, or swim 
# when you realise you can make it!

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
	attack = 0
	if dolphin:
		attack = round(shark_speed / 2, 1)
	else:
		attack = shark_speed
	while pontoon_distance >= 0 and shark_distance >= 0:
		pontoon_distance -= you_speed
		shark_distance -= attack
	if shark_distance <= 0:
		return "Shark Bait!"
	else:
		return "Alive!"


# TASK - Name on billboard 

# You can print your name on a billboard ad. Find out how much it will 
# cost you. Each letter has a default price of 30 pounds, but that can be 
# different if you are given 2 parameters instead of 1.

def billboard(name, price=30):
	res = 0
	for i in range(len(name)):
		res += price
	return res


# TASK - Uncollapse Digits

# You will be given a string of English digits "stuck" together
# Your task is to split the string into separate digits

def uncollapse(digits):
	compare = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	res = []
	count = 0
	for i in range(len(digits) + 1):
		if digits[count:i] in compare:
			res.append(digits[count:i])
			count = i
	return " ".join(res)


# TASK - Price of Mangoes

# There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a 
# given quantity and price (per mango), calculate the total cost of the 
# mangoes.

def mango(quantity, price):
	return (quantity - quantity // 3) * price


# TASK - validate code with simple regex

# Basic regex tasks. Write a function that takes in a numeric code of 
# any length. The function should check if the code begins with 1, 2, 
# or 3 and return true if so. Return false otherwise. 
 
def validate_code(code):
	return str(code)[0] in ["1","2","3"]


# TASK - USD => CNY

# Create a function that converts US dollars (USD) to Chinese Yuan 
# (CNY) . The input is the amount of USD as an integer, and the output 
# should be a string that states the amount of Yuan followed by 'Chinese 
# Yuan'

def usdcny(usd):
	convert = str(round(usd * 6.75, 2))
	if len(convert.split(".")[-1]) == 2:
		return f"{convert} Chinese Yuan"
	else:
		return f"{convert}0 Chinese Yuan"


# TASK - Is there a vowel in there?

# Given an array of numbers, check if any of the numbers are the 
# character codes for lower case vowels (a, e, i, o, u).
# If they are, change the array value to a string of that vowel.
# Return the resulting array.

def is_vow(inp):
    vowels = [ord("a"),ord("e"),ord("i"),ord("o"),ord("u")]
    res = []
    for i in inp:
        if i in vowels:
            res.append(chr(i))
        else:
            res.append(i)
    return res


# TASK - Fix the Bugs (Syntax) - My First Kata

# In this Kata you should fix/create a program that returns the following 
# values:
# false/False if either a or b (or both) are not numbers
# a % b plus b % a if both arguments are numbers

def my_first_kata(a,b):
    if not type(a) == int or not type(b) == int: return False
    else:
        return a % b + b % a


# TASK - Man in the west

# You need to check if there is gold in the bucket, and if so, return 
# True/true. If not, return False/false.

def check_the_bucket(bucket):
    return "gold" in bucket


# TASK - Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins

# You will be given an array of objects representing data about 
# developers who have signed up to attend the next coding meetup that 
# you are organising. 

def find_admin(lst, lang): 
    return [i for i in lst if i['language'] == lang and i['githubAdmin'] == "yes"]


# TASK - How many are smaller than me?

# Write smaller(arr) that given an array arr, you have to return the 
# amount of numbers that are smaller than arr[i] to the right.

def smaller(arr):
    res = []
    for i in range(len(arr)):
        count = 0
        compare = arr[i]
        for e in arr[i + 1:]:
            if e < compare:
                count += 1
        res.append(count)
    return res


# TASK - How many consecutive numbers are needed?

# Create the function consecutive(arr) that takes an array of integers 
# and return the minimum number of integers needed to make the contents 
# of arr consecutive from the lowest number to the highest number.

def consecutive(arr):
    if arr == []:
        return 0
    else:
        res = 0
        for i in range(min(arr), max(arr) + 1):
            if i not in arr:
                res += 1
        return res


# TASK - SillyCASE

# Create a function that takes a string and returns that string with 
# the first half lowercased and the last half uppercased.

def sillycase(silly):
    if len(silly) % 2 == 0:
        return silly[:len(silly) // 2].lower() + silly[len(silly) // 2:].upper()
    else:
        return silly[:len(silly) // 2 + 1].lower() + silly[len(silly) // 2 + 1:].upper()


# TASK - Simple Fun #136: Missing Values

#  You are given a sequence of positive ints where every element appears
# three times, except one that appears only once (let's call it x) and 
# one that appears only twice (let's call it y).
# Your task is to find x * x * y.

def missing_values(seq): 
    x = 0
    y = 0
    for i in seq:
        if seq.count(i) == 1:
            x = i
        elif seq.count(i) == 2:
            y = i
    return x * x * y


# TASK - How many times should I go?

# Lot of museum allow you to be a member, for a certain amount 
# amount_by_year you can have unlimitted acces to the museum.
# In this kata you should complete a function in order to know after 
# how many visit it will be better to take an annual pass. The function 
# take 2 arguments annual_price and individual_price.

def how_many_times(annual_price, individual_price):
    res = 0
    count = 0
    while res < annual_price:
        res += individual_price
        count += 1
    return count


# TASK - Character Counter

# You are going to be given a word. Your job will be to make sure that 
# each character in that word has the exact same number of occurrences. 
# You will return true if it is valid, or false if it is not.

def validate_word(word):
	res = {}
	result = True
	for letter in word.lower():
		res[letter] = word.lower().count(letter)
	return len(set(res.values())) == 1


# TASK - Histogram - H1

# You will be passed the dice value frequencies, and your task is to 
# write the code to return a string representing a histogram, so that 
# when it is printed it has the same format as the example.

def histogram(results):
    res = []
    for i in range(len(results)):
        res.append(f"{i + 1}|{'#' * results[i]} {results[i]}" if results[i] != 0 else f"{i + 1}|")
    return "\n".join(res[::-1]) + "\n"


# TASK - Absent vowel

# Your job is to figure out the index of which vowel is missing from a 
# given string 

def absent_vowel(x): 
    vowels = "aeiou"
    for letter in vowels:
        if not letter in x:
            return vowels.index(letter)


# TASK - Thinkful - String Drills: Hello, World

# Complete the function body for this hello() function so that it takes 
# one argument (person, a string) and returns a string saying hello to 
# that person. 

def hello(name):
    return f"Hello, {name}"


# TASK - Nickname Generator

# Write a function, nicknameGenerator that takes a string name as an 
# argument and returns the first 3 or 4 letters as a nickname.

def nickname_generator(name):
    vowels = "aeiou"
    return (name[:4] if name[2] in vowels else name[:3]) if len(name) > 3 else "Error: Name too short"


# TASK - Find the calculation type

# You have to create a function calcType, which receives 3 arguments: 
# 2 numbers, and the result of an unknown operation performed on them 
# (also a number). 

def calc_type(a, b, res):
    if a + b == res:
        return "addition"
    elif a - b == res:
        return "subtraction"
    elif a * b  == res:
        return "multiplication"
    else:
        return "division"


# TASK - Failed Sort - Bug Fixing #4 

# Your task is to fix the sortArray function to sort all numbers in 
# ascending order 

def sort_array(value):
    return "".join(sorted([i for i in value]))


# TASK - Find the Missing Number

# You are given an unsorted array containing all the integers from 0 to 
# 100 inclusively. However, one number is missing. Write a function to 
# find and return this number. 

def missing_no(nums):   
    compare = 0
    for i in sorted(nums):
        if compare != i:
            return compare
            break
        else:
            compare += 1
    if max(nums) != 100:
	    return 100


# TASK - All Star Code Challenge #1 

# Write a function, called sumPPG, that takes two NBA player 
# objects/struct/Hash/Dict/Class and sums their PPG 

def sum_ppg(player_one, player_two):
    return player_one['ppg'] + player_two['ppg']


# TASK - Invalid Input - Error Handling #1

# Your task is to implement a function which takes a string as input 
# and return an object containing the properties vowels and consonants. 
# The vowels property must contain the total count of vowels 
# {a,e,i,o,u}, and the total count of consonants {a,..,z} - {a,e,i,o,u}.
# Handle invalid input and don't forget to return valid ones.

def get_count(*words):
	res = {"vowels":0, "consonants":0}
	if words:
		try:
			for word in words:
				if type(word) == str:
					for letter in word:
						if letter.isalpha():
							if letter.lower() in "aeiou":
								res["vowels"] += 1
							else:
								res["consonants"] += 1
				else:
					return res
			return res
		except:
			return res
	else:
		return res