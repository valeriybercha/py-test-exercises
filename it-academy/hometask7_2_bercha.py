# HOMETASK 1 - VOWELS AND CONSONANTS IN 'N' LISTS
print("# HOMETASK 1 - VOWELS AND CONSONANTS IN 'N' LISTS")
# Creating a list with numbers, symbols and letters using ASCII code
print("- Creating a list with symbols, letters and numbers")

# Creating random 'n' lists
n = 1
import random
import string
for a in range(n):
    random_list = [''.join([random.choice(string.ascii_letters + string.digits + string.punctuation )]) for i in range(33)]
    set_random_list = (set(random_list))
    print(set_random_list)

# Creating a vowels list
vowels_vars = ['a', 'e', 'i', 'o', 'u', 'y']
set_vowels = set(vowels_vars)
vowels = list(set_random_list.intersection(set_vowels))
print("VOWELS in the list are: ", vowels)

# Creating consonants list
consonants = []
for i in range(97, 123):
    consonants.append(chr(i))
consonants_vars = set(consonants)

set_letters = (set_random_list.intersection(consonants_vars))
set_consonants = set_letters - set_vowels
print("CONSONANTS in the list are: ", set_consonants)


# HOMETASK 2 - REMOVE DUPLICATE SYMBOLS FROM A LIST
print("# HOMETASK 2 - REMOVE DUPLICATE SYMBOLS FROM A LIST")
import random
import string
random_list = [''.join([random.choice(string.ascii_letters + string.punctuation )]) for i in range(30)]
print(random_list)
b = set()
unique = []
for x in random_list:
    if x not in b:
        unique.append(x)
        b.add(x)
print(unique)

# HOMETASK 3 - ALPHABETICAL ORDER OF ELEMENTS IN A LIST
print("# HOMETASK 3 - ALPHABETICAL ORDER OF ELEMENTS IN A LIST")
print("- The original list")
# Creating original list and set
list_3 = ['f', 'A', 'b', 'j', 'h', 'I', 'G', 'd', 'E', 'C', '2', '9']
set_list_3 = set(list_3)
print(list_3)

# Create a list and set with numbers
list_numbers = []
for i in range(48, 58):
    list_numbers.append(chr(i))
set_numbers = set(list_numbers)
numbers_1 = list(set_list_3.intersection(set_numbers))
numbers = list(set_numbers - set_list_3)

# Removing the numbers from the list
list_3.remove('2')
list_3.remove('9')

# Sorting the final list
final_list_3 = list_3 + numbers
f_2 = set(final_list_3)
print("- The list with missing numbers")
print(sorted(f_2, reverse=True))

# HOMETASK 4 - REMOVING ZERO FROM LIST ELEMENTS
print("# HOMETASK 4 - REMOVING ZERO FROM LIST ELEMENTS")
list_4 = ["000045", "00654", "000.768"]
list_without_zero = [i.strip('0') for i in list_4]
print(list_without_zero)

# HOMETASK 5 - SET OF VALUES FROM TWO LISTS
print("# HOMETASK 5 - SET OF VALUES FROM TWO LISTS")
# Creating the two original lists
print("- The original two lists")
list_5_1 = ['f', 'A', 'b', 'j', 'h', 'I', 'G', 'd', 'E', 'C', '2', '9']
print(list_5_1)
set_list_5_1 = set(list_5_1)
list_5_2 = ['k', 'L', 'm', 'N', 'o', 'P', '1', '3', '4', '5', '6', '7']
print(list_5_2)
set_list_5_2 = set(list_5_2)

# Create a list and set with letters
lett_5_1 = []
for i in range(65, 123):
    lett_5_1.append(chr(i))
set_lett_5_1 = set(lett_5_1)
list_lett_5_1 = list(set_list_5_1.intersection(set_lett_5_1))
set_letters_5_1 = set(list_lett_5_1)
print("- The set with letters from first list")
print(sorted(set_letters_5_1))

lett_5_2 = []
for i in range(65, 123):
    lett_5_2.append(chr(i))
set_lett_5_2 = set(lett_5_2)
list_lett_5_2 = list(set_list_5_2.intersection(set_lett_5_2))
set_letters_5_2 = set(list_lett_5_2)
print("- The set with letters from second list")
print(sorted(set_letters_5_2))

# Combining results together
list_letters = list_lett_5_1 + list_lett_5_2
set_list_letters = set(list_letters)
print("- The list with letters from two lists")
print(sorted(set_list_letters))

# Create a list and set with numbers
num_5_1 = []
for i in range(48, 58):
    num_5_1.append(chr(i))
set_num_5_1 = set(num_5_1)
list_num_5_1 = list(set_list_5_1.intersection(set_num_5_1))

num_5_2 = []
for i in range(48, 58):
    num_5_2.append(chr(i))
set_num_5_2 = set(num_5_2)
list_num_5_2 = list(set_list_5_2.intersection(set_num_5_2))

# Combining results together
list_numbers = list_num_5_1 + list_num_5_2
set_list_numbers = set(list_numbers)
print("- The list with numbers from two lists")
print(sorted(set_list_numbers))