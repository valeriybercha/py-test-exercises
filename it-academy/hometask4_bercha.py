# HOMETASK 1 - UPPER AND LOWER CASES
print("# HOMETASK 1 - UPPER AND LOWER CASES")
p_phylosophy = "Beautiful is better than ugly \
Explicit is better than implicit \
Simple is better than complex \
Complex is better than complicated \
Readability counts"

# Printing in upper cases
print (p_phylosophy.upper())
p_phylosophy_upper = (p_phylosophy.upper())
print(p_phylosophy_upper.isupper())

# Printing in lower cases
print (p_phylosophy.lower())
p_phylosophy_lower = (p_phylosophy.lower())
print(p_phylosophy_lower.islower())

# HOMETASK 2 - PLAYING WITH NUMBERS
print("# HOMETASK 2 - PLAYING WITH NUMBERS")

# Task A - Multiplication
four_digit_number = int(input("Insert the 4-digit number: "))
var_n = str(four_digit_number)
digit_1 = int(var_n[0])
digit_2 = int(var_n[1])
digit_3 = int(var_n[2])
digit_4 = int(var_n[3])
var_calc = digit_1 * digit_2 * digit_3 * digit_4
print("The multiplication of numbers you've entered is " +str(var_calc))

# Task B - Reversing
rev_string = var_n[::-1]
print("The reversed number you've typed is " + str(rev_string))