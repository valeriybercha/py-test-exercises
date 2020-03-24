# HOMETASK 1 - YEAR CALCULATION
print("# HOMETASK 1 - YEAR CALCULATION")
var_age = int(input("Insert a year: "))
if var_age % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
var_cent = var_age / 100 + 1
print("The year you've typed is related to " + str(int(var_cent)) + "th century")

# HOMETASK 2 - SHAPE AREA CALCULATION
print("# HOMETASK 2 - SHAPE AREA CALCULATION")
print("You can choose between typing 'rectangle', 'triangle' or 'circle'")
shape = input("Type the shape you'd like to work with: ")
if shape == "rectangle":
    shape_length = int(input("Insert the shape length: "))
    shape_width = int(input("insert the shape width: "))
    shape_area = shape_length * shape_width
    print("Calculated rectangle area is " + str(shape_area))
elif shape == "triangle":
    shape_length = int(input("Insert the shape length: "))
    shape_height = int(input("Insert the shape height: "))
    shape_area = (shape_length * shape_height) / 2
    print("Calculated triangle area is " + str(shape_area))
elif shape == "circle":
    import math
    shape_radius = int(input("Insert the shape radius: "))
    shape_area = math.pi * (shape_radius ** 2)
    print("Calculated circle area is " + str(round(shape_area, 2)))
else:
    print("Something goes wrong. We couldn't identify the shape. Please re-enter it")

# HOMETASK 3 - INSERTED NUMBER DESCRIPTION
print("# HOMETASK 3 - INSERTED NUMBER DESCRIPTION")
var_num = int(input("Type a number: "))
if var_num < 0:
    if var_num <= -1 and var_num <= -9:
        print("You've typed an one-digit negative number")
    elif var_num >= -10 and var_num <= -99:
        print("You've typed an two-digit negative number")
elif var_num == 0:
    print("You've typed a ZERO")
elif var_num > 0:
    if var_num >= 1 and var_num <= 9:
        print("You've typed an one-digit positive number")
    elif var_num >= 10 and var_num <= 99:
        print("You've typed an two-digit positive number")
else:
    print("You've enter an invalid value")

# HOMETASK 4 - PLACING THE ROUND STAGE IN THE HALL
print("# HOMETASK 4 - PLACING THE ROUND STAGE IN THE HALL")
hall_area = int(input("Insert the hall area: "))
stage_area = int(input("Insert the round stage area: "))
pass_k = int(input("Insert the pass length variable: "))
import math
hall_length = math.sqrt(hall_area)
stage_radius = math.sqrt(stage_area / math.pi)
if pass_k <= (hall_length / 2) - stage_radius:
    print("It is POSSIBLE to place the round stage in the hall")
elif pass_k > (hall_length / 2) - stage_radius:
    print("It's NOT POSSIBLE to place the round stage in the hall")
else:
    print("Something goes wrong. We cannot calculate with introduced values. Please try again")

# HOMETASK 5 - MONEY EXCHANGE - METHOD 1
print("# HOMETASK 5 - MONEY EXCHANGE - METHOD 1")
amount_money = int(input("Insert the amount of money: "))
if amount_money % 200 == 0:
    bank_200 = amount_money / 200
    print("We can change your money by giving you " + str(int(bank_200)) + " banknotes of 200")
elif amount_money % 100 == 0:
    bank_100 = amount_money / 100
    print("We can change your money by giving you " + str(int(bank_100)) + " banknotes of 100")
elif amount_money % 10 == 0:
    bank_10 = amount_money / 10
    print("We can change your money by giving you " + str(int(bank_10)) + " banknotes of 10")
elif amount_money % 1 == 0:
    bank_1 = amount_money / 1
    print("We can change your money by giving you " + str(int(bank_1)) + " banknotes of 1")

# HOMETASK 5 - MONEY EXCHANGE - METHOD 2
print("# HOMETASK 5 - MONEY EXCHANGE - METHOD 2")
money_amount = int(input("Type the amount of money you want to change: "))
var_s = str(money_amount)

# Checking if where inserted 3 digits
if money_amount >= 100 and money_amount <= 999:
    # First digit
    first_digit = int(var_s[0])
    all_digit = int(var_s)
    if first_digit % 2 == 0:
        bank_200 = int(all_digit / 200)
        print("We can exchange by giving you " + str(int(bank_200)) + " banknotes of 200")
    else:
        bank_100 = int(all_digit / 100)
        print("We can exchange by giving you " + str(int(bank_100)) + " banknotes of 100")

    # Second digit
    second_digit = int(var_s[1])
    all_digit_minus_one = int(var_s[1:3])
    if second_digit % 1 == 0:
        bank_10 = int(all_digit_minus_one / 10)
        print("We can exchange by giving you " + str(int(bank_10)) + " banknotes of 10")
    else: second_digit == 0

    # Third digit
    third_digit = int(var_s[2])
    all_digit_minus_two = int(var_s[2:4])
    if third_digit % 1 == 0:
        bank_1 = int(all_digit_minus_two / 1)
        print("We can exchange by giving you " + str(int(bank_1)) + " banknotes of 1")
    else: third_digit == 0

# Checking if where inserted 2 digits
elif money_amount >= 10 and money_amount <= 99:
    # First digit
    first_digit = int(var_s[0])
    all_digit = int(var_s)
    if first_digit % 1 == 0:
        bank_10 = int(all_digit / 10)
        print("We can exchange by giving you " + str(int(bank_10)) + " banknotes of 10")
    else:
        first_digit == 0

    # Second digit
    second_digit = int(var_s[1])
    all_digit_minus_one = int(var_s[1:3])
    if second_digit % 1 == 0:
        bank_1 = int(all_digit_minus_one / 1)
        print("We can exchange by giving you " + str(int(bank_1)) + " banknotes of 1")
    else:
        second_digit == 0

# Checking if where inserted 1 digit
elif money_amount >= 1 and money_amount <= 9:
    # First digit
    first_digit = int(var_s[0])
    all_digit = int(var_s)
    if first_digit % 1 == 0:
        bank_1 = int(all_digit / 1)
        print("We can exchange by giving you " + str(int(bank_1)) + " banknotes of 1")
    else:
        first_digit == 0
else:
    print("Ooops... Seems that we cannot change your money")