# HOMETASK 1 - GUESS THE NUMBER
print("# HOMETASK 1 - GUESS THE NUMBER")
import random
var_r = random.randint(1, 101)
print(var_r)
var_a = ""
guess_count = 0
guess_limit = 10
out_of_guesses = False
while var_a != var_r and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_count += 1
        print("That is your " + str(guess_count) + " attempt")
        var_a = int(input("Type a number from 1 to 100: "))
        if var_a > var_r:
            print("The value you've introduce is BIGGER than the guessing value")
        elif var_a < var_r:
            print("The value you've introduce is SMALLER than the guessing value")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You are out of guesses! YOU LOSE! The guess number is " + str(var_r))
else:
    print("YOU WIN! You guessed the number!")

# HOMETASK 2 - QUANTITY OF NUMBERS DIVIDED TO 5
print("# HOMETASK 2 - QUANTITY OF NUMBERS DIVIDED TO 5")
print("The typed number should be bigger than 2")
var_1 = int(input("Type the 1 number: "))
var_2 = int(input("Type the 2 number: "))
var_3 = int(input("Type the 3 number: "))
var_4 = int(input("Type the 4 number: "))
var_5 = int(input("Type the 5 number: "))
var_6 = int(input("Type the 6 number: "))
var_7 = int(input("Type the 7 number: "))
var_8 = int(input("Type the 8 number: "))
var_9 = int(input("Type the 9 number: "))
var_10 = int(input("Type the 10 number: "))
calc_num = 0
var_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
for var_s in var_list:
    if var_s > 2 and var_s % 5 == 0:
        var_s = 1
        calc_num = calc_num + var_s
    var_s += 1
print("The quantity of numbers divided by 5 is equal to " + str(calc_num))

# HOMETASK 3 - MULTIPLICATION TABLE
print("# HOMETASK 3 - MULTIPLICATION TABLE")
var_num = int(input("Insert a number to multiply: "))
for mult_num in range(1, 11):
   print(str(var_num) + "x" + str(mult_num) + "=" + str(var_num*mult_num))

# HOMETASK 4 - DRAW A RECTANGLE
print("# HOMETASK 4 - DRAW A RECTANGLE")
symbol_1 = input("Type a symbol: ")
symbol_2 = input("Type another symbol: ")

print(symbol_1 * 17)
print(symbol_1, symbol_2 * 13, symbol_1)
print(symbol_1, symbol_2 * 13, symbol_1)
print(symbol_1, symbol_2 * 13, symbol_1)
print(symbol_1 * 17)

# HOMETASK 5 - variables p and h
print("# HOMETASK 5 - variables p and h")
var_a = ""
var_p = 15
var_h = 25
sum_var_p = 0
sum_var_i = 0
mult_var_k = 1
print("Variable 'p' = " + str(var_p))
print("Variable 'h' = " + str(var_h))
while var_a != var_p and var_a != var_h:
    var_a = int(input("Type a number: "))
    if var_a < var_p:
        sum_var_p = sum_var_p + var_a
    if var_a > var_h:
        mult_var_k = mult_var_k * var_a
    if var_p < var_h:
        var_i = 1
        sum_var_i = var_h - var_p
print("The sum of numbers < variable 'p' is eqaul to " +str(sum_var_p))
print("The multiplication of numbers > variable 'k' is eqaul to " +str(mult_var_k))
print("The amount of numbers in range 'p' and 'k' is eqaul to " +str(sum_var_i))

# HOMETASK 6 - percentage calculation
print("# HOMETASK 6 - percentage calculation")
per_a = ""
sum_pos = 0
sum_neg = 0
per_count = 0
while per_a != 0:
    per_count += 1
    per_a = int(input("Type a number - 'positive' or 'negative': "))
    if per_a > 0:
        per_a = 1
        sum_pos = sum_pos + per_a
    elif per_a < 0:
        per_a = 1
        sum_neg = sum_neg + per_a
per_count = per_count - 1
pos_x = (sum_pos / per_count) * 100
neg_x = (sum_neg  / per_count) * 100
print("Percentage of POSITIVE numbers is " + str(round(pos_x)) + "% and NEGATIVE - " + str(round(neg_x)) + "%")