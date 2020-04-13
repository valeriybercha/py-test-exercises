# My solutions for tasks on Python on HackerRank


###### INTRODUCTION TASKS ######


### Task - Python if else ###

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n = int(input())

if n % 2 == 0:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
elif n % 2 != 0:
    print("Weird")


### Task - Arithmetic Operators ###

# Read two integers from STDIN and print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# Variant 1
a = int(input())
b = int(input())

if a >= 1 and a<= 10 ** 10 and b >=1 and b <= 10 ** 10:
    print(a + b)
    print(a - b)
    print(a * b)


# Variant 2
def arithmetic_operations(a, b):
    if a in range(1, 10 ** 10+1) and b in range(1, 10 ** 10+1):
        summ = a + b
        diff = a - b
        mult = a * b
        return summ, diff, mult

print(arithmetic_operations(a = int(input()), b = int(input())))


### Task - Python: Division ###

# Read two integers and print two lines. The first line should contain integer division,  a//b . The second
# line should contain float division,  a/b .
# You don't need to perform any rounding or formatting operations.

# Variant 1
a = int(input())
b = int(input())

print(a//b)
print(a/b)

# Variant 2
def python_division(a, b):
    print(a//b)
    print(a/b)

python_division(a = int(input()), b = int(input()))


### Task - Loops ###

# Read an integer N. For all non-negative integers i < N, print i ** 2.

n = int(input())

if 1 <= n <= 20:
    for i in range(n):
        print(i ** 2)


### Task - Write a function ###

# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.

def is_leap(year):
    leap = False

    # Write your logic here
    if 1900 <= year <= 10 ** 5:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

    return leap

year = int(input())


### Task - Print Function ###

# Read an integer N.
# Without using any string methods, try to print the following 123...N:
# Note that "..." represents the values in between.

n = int(input())
for i in range(1, n+1):
    print(i, end="")



###### BASIC DATA DRIVEN ######


### Task - Find the Runner-Up Score ###

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input())
arr = list(map(int, input().split()))

a = set(arr[:n])
a_list = list(a)

max_elem = max(a_list)

for elem in a_list:
    if elem == max_elem:
        a_list.remove(elem)

print(max(a_list))


### Task - Nested Lists ###

# Given the names and grades for each student in a Physics class of n students, store them in a nested list and print
# the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on
# a new line.

from operator import itemgetter

n = int(input())

# Creating the list of students
students_list = []
for student in range(n):
    student_profile = []
    students_name = input()
    student_profile.append(students_name)
    students_grade = float(input())
    student_profile.append(students_grade)
    students_list.append(student_profile)


# Min of all elements
min_students_list = min(students_list, key=itemgetter(1))[1]

# Remove elements equal to min
filtered_list = [x for x in students_list if x[1] != min_students_list]

# Get min of remaining
min_list_filtered = min(filtered_list, key=itemgetter(1))[1]

a = []

# Filter remaining
out = [x for x in filtered_list if x[1] == min_list_filtered]
for name in out:
    a.append(name[0])
a.sort()
for name in a:
    print(name)


### Task - Finding the percentage ###

# You have a record of N students. Each record contains the student's name, and their percent marks in Maths,
# Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names
# and marks for N students. You are required to save the record in a dictionary data type. The user then enters
# a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

n = int(input())

student_marks = {}

for stud_num in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

for key, value in student_marks.items():
    if key == query_name:
        sum_score = sum(value)
        score_percent = sum_score / 3
        print("%.2f" % score_percent)


### Task - Tuples ###

# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute
# and print the result of hash(t).

import hashlib

n = int(input())

l = list(map(int, input().strip().split()))[:n]

t = tuple(l)
print(hash(t))



###### STRINGS ######


### Task - sWAP cASE ###

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
# letters and vice versa.

s = input()
final = ""

for i in range(len(s)):
    if s[i].islower():
        final += s[i].upper()
    else:
        final += s[i].lower()

print(final)


### Task - String Split and Join ###

# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Variant 1
a = input()
b = a.split(" ")

c = "-".join(b)
print(c)

# Variant 2
def split_and_join(line):

    # write your code here
    b = line.split(" ")
    c = "-".join(b)
    return c

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


### Task - What's Your Name? ###

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print
# the following:
# Hello firstname lastname! You just delved into python.

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


### Task - Mutations ###

# Read a given string, change the character at a given index and then print the modified string.
# Input Format
# The first line contains a string, S.
# The next line contains an integer i, denoting the index location and a character c separated by a space.

# Variant 1
s = input()

i, c = input().split()

l = list(s)
print(l)

l[int(i)] = c
print(l)

s_new = "".join(l)
print(s_new)

# Variant 2
def mutate_string(string, position, character):
    l = list(s)
    l[int(i)] = c
    s_new1 = "".join(l)
    return s_new1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


### Task - String Validators ###

# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits,
# lowercase and uppercase characters.
# Input Format
# A single line containing a string S.

# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.


s = input()
result = int()
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []

# check for alphanumeric characters
for aplpha in s:
    if aplpha.isalnum():
        result = 1
    else:
        result = 0
    list_1.append(result)
c_1 = sum(list_1)

if c_1 >= 1:
    print(True)
else:
    print(False)

# check for alphabet characters
for alphabet in s:
    if alphabet.isalpha():
        result = 1
    else:
        result = 0
    list_2.append(result)
c_2 = sum(list_2)

if c_2 >= 1:
    print(True)
else:
    print(False)

# check for digits numbers
for digit in s:
    if digit.isdigit():
        result = 1
    else:
        result = 0
    list_3.append(result)
c_3 = sum(list_3)

if c_3 >= 1:
    print(True)
else:
    print(False)

# check for lowercase characters
for lowercase in s:
    if lowercase.islower():
        result = 1
    else:
        result = 0
    list_4.append(result)
c_4 = sum(list_4)

if c_4 >= 1:
    print(True)
else:
    print(False)

# check for uppercase characters
for uppercase in s:
    if uppercase.isupper():
        result = 1
    else:
        result = 0
    list_5.append(result)
c_5 = sum(list_5)

if c_5 >= 1:
    print(True)
else:
    print(False)


### Task - Text Alignment ###

# Replace all ______ with rjust, ljust or center.

thickness = int(input()) # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


### TASK - Text Wrap ###

# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

import textwrap

# Variant 1
def wrap(string, max_width):
    return textwrap.wrap(string, max_width)

string = input()
max_width = int(input())

for elem in wrap(string, max_width):
    print(elem)

# Variant 2
def wrap(string, max_width):
    l = list()
    for i in range(0, len(string), max_width): l.append(string[i:i + max_width])
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


### Task - String Formatting ###

# Given an integer, n, print the following values for each integer i from 1 to n:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each i from 1 to n. Each
# value should be space-padded to match the width of the binary value of n.

n = 2

def print_formatted(number):
    n_bin = bin(number)
    n_bin_len = int(len(n_bin[2:]))
    for elem in range(1, number + 1):
        var_decimal = str(elem)
        var_octal = str(oct(elem))
        var_hexadecimal = str(hex(elem))
        var_binary = str(bin(elem))

        print("{:>{n_bin_len}} {:>{n_bin_len}} {:>{n_bin_len}} {:>{n_bin_len}}".format(var_decimal, var_octal[2:], var_hexadecimal[2:].upper(), var_binary[2:], n_bin_len=n_bin_len))

print_formatted(n)


### TASK - Capitalize! ###

# You are asked to ensure that the first and last names of people begin with a capital letter in their
# passports. For example, alison heck should be capitalised correctly as Alison Heck.

s = input()

l = s.split()

# Variant 1
l_fin = []

for split in l:
    word = ""
    for elem in range(len(split)):
        f_word = split[0].upper()
        r_word = split[1:]
        word = f_word + r_word
    l_fin.append(word)

final_word = " ".join(l_fin)
print(final_word)

# Variant 2
l_fin_one = []

for split_one in l:
    word_one = split_one.capitalize()
    l_fin_one.append(word_one)

final_word_one = " ".join(l_fin_one)
print(final_word_one)

# Variant 3
import string
print(string.capwords(s, ' '))



###### SETS ######


### Task - Introduction to Sets ###

# The first line contains the integer, n, the total number of plants.
# The second line contains the n space separated heights of the plants.

n = 5
arr = list(map(int, input().split()))
final_s = set()

count = 0
while count != n:
    for elem in arr:
        final_s.add(elem)
        count += 1

average = sum(final_s) / len(final_s)
print(average)


### Task - Symmetric Difference ###

# Given 2 sets of integers, m and n, print their symmetric difference in ascending order. The term symmetric difference
# indicates those values that exist in either m or n but do not exist in both.

m = int(input())
m_int = input() # 2 4 5 9
m_int_list = m_int.split()
m_int_list_int = list(map(int, m_int_list))
m_int_set = set(m_int_list_int)

n = int(input())
n_int = input() # 2 4 11 12
n_int_list = n_int.split()
n_int_list_int = list(map(int, n_int_list))
n_int_set = set(n_int_list_int)

final_list = []

for elem in m_int_set.difference(n_int_set):
    final_list.append(elem)

for e in n_int_set.difference(m_int_set):
    final_list.append(e)

final_list.sort()

for item in final_list:
    print(item)

### Task - Set .add() ###

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps
# in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.
# Find the total number of distinct country stamps.

n = int(input())
country_set = set()
for cntry in range(7):
    country_name = input()
    country_set.add(country_name)

final_n = 0
for c in range(len(country_set)):
    final_n += 1
print(final_n)



### Task - Set .discard(), .remove() & .pop() ###

# You have a non-empty set s, and you have to execute n commands given in n lines.
# The commands will be pop, remove and discard.
# The first line contains integer n, the number of elements in the set a.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less
# than or equal to 9.
# The third line contains integer n, the number of commands.
# The next n lines contains either pop, remove and/or discard commands followed by their associated value.

n = int(input())
s = set(map(int, input().split()))

c = int(input())

for command in range(c):
    c_input = input()
    if c_input == "pop":
        s.pop()
    else:
        c_list = c_input.split()
        c_int = int(c_list[1])
        if c_list[0] == "remove":
            s.remove(c_int)
        elif c_list[0] == "discard":
            s.discard(c_int)

final_s = sum(s)
print(final_s)


### Task - Set .union() Operation ###

# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.
# Output the total number of students who have at least one subscription.

n_1 = int(input())
s_1 = set(map(int, input().split()))

n_2 = int(input())
s_2 = set(map(int, input().split()))

final_s = s_1.union(s_2)

count = 0
for elem in final_s:
    count += 1

print(count)


### Task - Set .intersection() Operation ###


# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.
# Output the total number of students who have subscriptions to both English and French newspapers.

n_1 = int(input())
s_1 = set(map(int, input().split()))

n_2 = int(input())
s_2 = set(map(int, input().split()))

final_s = s_1.intersection(s_2)

count = 0
for elem in final_s:
    count += 1

print(count)


### Task - Set .difference() Operation ###

# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.
# Output the total number of students who are subscribed to the English newspaper only.

n_1 = int(input())
s_1 = set(map(int, input().split()))

n_2 = int(input())
s_2 = set(map(int, input().split()))

final_s = s_1.difference(s_2)

count = 0
for elem in final_s:
    count += 1

print(count)


### Task - Set .symmetric_difference() Operation ###

# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.
# Output total number of students who have subscriptions to the English or the French newspaper but not both.

n_1 = int(input())
s_1 = set(map(int, input().split()))

n_2 = int(input())
s_2 = set(map(int, input().split()))

final_s = s_1.symmetric_difference(s_2)

count = 0
for elem in final_s:
    count += 1

print(count)


### Task - Set Mutations ###

# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation
# operations on set A.
# Your task is to execute those operations and print the sum of elements from set A.
# Input Format
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the
# other set.
# The second line of each part contains space separated list of elements in the other set.
# Output the sum of elements in set A.

n_set_elems = int(input())
set_a = set(map(int, input().split()[:n_set_elems]))

n = int(input())

for elems in range(n):
    n_new_set_inp = input()
    n_new_set_list = n_new_set_inp.split()

    if n_new_set_list[0] == "intersection_update":
        n_new_set_elems = int(n_new_set_list[1])
        n_new_set = set(map(int, input().split()[:n_new_set_elems]))
        set_a.intersection_update(n_new_set)
        #print(set_a)

    elif n_new_set_list[0] == "update":
        n_new_set_elems = int(n_new_set_list[1])
        n_new_set = set(map(int, input().split()[:n_new_set_elems]))
        set_a.update(n_new_set)
        #print(set_a)

    elif n_new_set_list[0] == "difference_update":
        n_new_set_elems = int(n_new_set_list[1])
        n_new_set = set(map(int, input().split()[:n_new_set_elems]))
        set_a.difference_update(n_new_set)
        #print(set_a)

    elif n_new_set_list[0] == "symmetric_difference_update":
        n_new_set_elems = int(n_new_set_list[1])
        n_new_set = set(map(int, input().split()[:n_new_set_elems]))
        set_a.symmetric_difference_update(n_new_set)
        #print(set_a)

sum_set_a = sum(set_a)
print(sum_set_a)



###### MATH ######


### Task - Mod Divmod ###

# Read in two integers, a and b, and print three lines.
# The first line is the integer division a // b (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: a % b.
# The third line prints the divmod of a and b.

a = int(input())
b = int(input())

int_division = a // b
print(int_division)

int_modulo = a % b
print(int_modulo)

int_divmod = divmod(a, b)
print(int_divmod)


### Task - Power - Mod Power ###

# You are given three integers: a, b, and m, respectively. Print two lines.
# The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

a = int(input())
b = int(input())
m = int(input())

int_pow = a ** b
print(int_pow)

int_pow_mod = pow(a, b, m)
print(int_pow_mod)


### Task - Integers Come In All Sizes ###

# Read four numbers, a, b, c, and d, and print the result of a ** b + c ** d.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = a ** b + c ** d
print(result)


### Task - Polar Coordinates ###

# You are given a complex z. Your task is to convert it to polar coordinates.
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input
# as a complex number.
# Output two lines:
# The first line should contain the value of 'r'.
# The second line should contain the value of 'phi'.

import cmath

z = complex(input())

res_phi = abs(z)
print(res_phi)
res_r = cmath.phase(z)
print(res_r)



###### ITERTOOLS ######


### Task - itertools.product() ###

# You are given a two lists a and b. Your task is to compute their cartesian product a*b.

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))



###### OTHER TASKS ######


### Task - Sorting String ###

# Your task is to sort the string "S" in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.


s = input()

s_lower = ""
s_upper = ""
s_int = ""

s_lower_list = []
s_upper_list = []
s_int_list = []
s_odd_list = []
s_even_list = []

if 0 <= len(s) <= 1000:
    for i in s:
        if i.islower():
            s_lower_list.append(i)
            s_lower_list.sort()
        elif i.isupper():
            s_upper_list.append(i)
            s_upper_list.sort()
        else:
           if int(i) % 2 == 0:
               s_even_list.append(i)
               s_even_list.sort()
           else:
               s_odd_list.append(i)
               s_odd_list.sort()
           s_int_list = s_odd_list + s_even_list

s_final = s_lower_list + s_upper_list + s_int_list
s_final_string = "".join(s_final)
print(s_final_string)


### Triangle Task ###

# ABC is a traingle, 90 at B. Point M is the midpoint of hypotenuse AC. You are given the lengths AB and BC.
# Your task is to find MBC (angle , as shown in the figure) in degrees.

import math

# Triangle sides
ab = int(input())
bc = int(input())

# Right triangle at b
abc = 90

if 0 <= ab <= 100 and 0 <= bc <= 100:
    tang_deg = ab / bc
    arctang_deg = math.atan(tang_deg)
    degrees = (arctang_deg * 180) / math.pi
    degrees_int = int(round(degrees))
    mbc = str(degrees_int) + u"\N{DEGREE SIGN}"
    print(mbc)

if 0 <= ab <= 100 and 0 <= bc <= 100:
    cos_deg = bc / math.sqrt(ab ** 2 + bc ** 2)
    arccos_deg = math.acos(cos_deg)
    degrees = (arccos_deg * 180) / math.pi
    degrees_int = int(round(degrees))
    acb = str(degrees_int) + u"\N{DEGREE SIGN}"
    print(acb)


### Task - Lists ###

# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the
# 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.


# NOT WORKING!!! TO BE CHECKED!
n = 3
input_list = []
list = []
for i in range(n):
   inp = input().split()
   input_list.append(inp)

print(input_list)


for i in input_list:
    for j in i:
        c = len(j)
        print(c)


l = len(input_list)
for i in range(1, 2):
    for j in range(l-i-1):
        print(j)
        if input_list[j][1] > input_list[j + 1][1]:
            print(j)
            temp = input_list[j]
            input_list[j] = input_list[j+1]
            input_list[j + 1] = temp
print(input_list)

for item in input_list:
    if item[0] == "insert":
        number = item[2]
        list.append(number)

    elif item[0] == "remove":
        list.remove(item[1])

    elif item[0] == "append":
        list.append(item[1])

    elif item[0] == "pop":
        list.pop(item[-1])

    elif item[0] == "sort":
        print(sorted(list))

    elif item[0] == "reverse":
        print(list.sort(reverse=True))

    elif item[0] == "print":
        print(list)


### Task - Find a string ###

# In this challenge, the user enters a string and a substring. You have to print the number of times that the
# substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.


#### NOT WORKING! TO BE CHECKED!
first_str = "abcdcdc"
second_str = "cdc"

result = 0
step = 0
second_str_len = 0
for i in second_str:
    second_str_len +=1

for i in range(0, len(first_str)):
    print(first_str[i])

for item in first_str:

    first_str_len = first_str.find(second_str, step, second_str_len)
    print(first_str_len)
    if first_str_len == second_str:
        result += 1
    step +=1
print(result)








