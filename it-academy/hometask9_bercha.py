# TASK 1 - ARITHMETIC FUNCTION
print("# TASK 1 - ARITHMETIC FUNCTION")

def arithmetic(var_1_a, var_1_b, var_1_op):
    if var_1_op == "+":
        var_1_result = var_1_a + var_1_b
        return var_1_result
    elif var_1_op == "-":
        var_1_result = var_1_a - var_1_b
        return var_1_result
    elif var_1_op == "*":
        var_1_result = var_1_a * var_1_b
        return var_1_result
    elif var_1_op == "/":
        var_1_result = var_1_a / var_1_b
        return var_1_result
    else:
        var_1_result = -1
        return var_1_result


var_1_a = int(input("Type the 1st number : "))
var_1_b = int(input("Type the 2nd number : "))
var_1_op = input("Type the operator : ")
var_1_result = int()

if var_1_result == "-1":
    print("You've made an mistake")
else:
    print("The result is : ", arithmetic(var_1_a, var_1_b, var_1_op))

# TASK 2 - IS YEAR LEAP FUNCTION
print("# TASK 2 - IS YEAR LEAP FUNCTION")
def is_year_leap(year):
    if year % 4 == 0:
        result = True
        return result
    else:
        result = False
        return result

year = int(input("Type a year : "))
print(is_year_leap(year))

# TASK 3 - SQUARE CALCULATIONS FUNCTION
print("# TASK 3 - SQUARE CALCULATIONS FUNCTION")

import math

def square(side):
    perimeter = 4 * side
    surface = side ** 2
    diagonal = side * math.sqrt(2)
    results = (perimeter, surface, diagonal)
    return results

side = int(input("Type a square side : "))
print(square(side))

# TASK 4 - SEASONS CHECK FUNCTION
print("# TASK 4 - SEASONS CHECK FUNCTION")

def season(month):
    if month in range(3, 6):
        print("It's SPRING")
    elif month in range(6, 9):
        print("It's SUMMER")
    elif month in range(9, 12):
        print("It's AUTUMN")
    elif month == 12 or month in range(1, 3):
        print("It's WINTER")

month = int()
while month != 13:
    month = int(input("Type a month : "))
    print(season(month))
print("END of program")

# TASK 5 - BANK DEPOSIT
print("# TASK 5 - BANK DEPOSIT")
def bank(n, years):
    percents_per_year = 1.1
    add_n = n * 1.1

    result = add_n * percents_per_year ** years
    return result

n = int(input("Insert the amount to be deposited : "))
years = int(input("Type the number of years : "))
print("The amount of money in the account would be", round(bank(n, years), 2))

# TASK 6 - NUMBER IS PRIME OR COMPOSITE
print("# TASK 6 - NUMBER IS PRIME OR COMPOSITE")
def is_prime(num):

    if num > 1:
        for item in range(2, 1001):
            if num % item == 0:
                result = False
                return result
            else:
                result = True
                return result
    else:
        return print("Not prime neither composite")

num = int(input("Type a number from 0 to 1000 : "))
print(is_prime(num))

# TASK 7 - CALENDAR FUNCTION CHECK
print("# TASK 7 - CALENDAR FUNCTION CHECK")
def date(day, month, year):

    if day in range(1, 32):
        day = True
    else:
        day = False

    if month in range(1, 13):
        month = True
    else:
        month = False

    if len(year) == 4:
        year = True
    else:
        year = False

    date_list = [day, month, year]
    result = len(set(date_list)) == 1
    return result

day = int(input("Type a day 'from 1 to 31' : "))
month = int(input("Type a month 'from 1 to 12' : "))
year = input("Type a year : ")
print(date(day, month, year))
