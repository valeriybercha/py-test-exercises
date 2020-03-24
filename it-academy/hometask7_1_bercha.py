# HOMETASK 1 - CREATINNG A LIST
print("# HOMETASK 1 - CREATINNG A LIST")
# Creating a list with numbers, symbols and letters using ASCII code
print("- Creating a list with symbols, letters and numbers")
list_1 = []
for i in range(33, 123):
    list_1.append(chr(i))
print(list_1)

# HOMETASK 2 - DIVIDING LISTS
print("# HOMETASK 2 - DIVIDING LISTS")
list_1_letters = []
list_1_numbers = []
list_1_symbols = []

# Creating a list with symbols only
print("- The list with symbols only")
for i in range(33, 48):
    list_1_symbols.append(chr(i))
for i in range(58, 65):
    list_1_symbols.append(chr(i))
for i in range(91, 97):
    list_1_symbols.append(chr(i))
print(list_1_symbols)

# Creating a list with numbers only
print("- The list with numbers only")
for i in range(48, 58):
    list_1_numbers.append(chr(i))
print(list_1_numbers)

# Creating a list with letters only
print("- The list with letters only")
for i in range(65, 91):
    list_1_letters.append(chr(i))
print(list_1_letters)
for i in range(97, 123):
    list_1_letters.append(chr(i))
print(list_1_letters)

# HOMETASK 3 - CONVERTING LISTS IN TUPLES
print("# HOMETASK 3 - CONVERTING LISTS IN TUPLES")
print("- Converting lists in tuples")
tuple_1_symbols = tuple(list_1_symbols)
print(tuple_1_symbols)
tuple_1_numbers = tuple(list_1_numbers)
print(tuple_1_numbers)
tuple_1_letters = tuple(list_1_letters)
print(tuple_1_letters)

# HOMETASK 4 - INDEXING AN ELEMENT
print("# HOMETASK 4 - INDEXING AN ELEMENT")
var_a = input("Type a symbol, number or letter: ")
for i in tuple_1_letters:
    if var_a == i:
        var_a = tuple_1_letters.index(i)
for i in tuple_1_numbers:
    if var_a == i:
        var_a = tuple_1_numbers.index(i)
for i in tuple_1_symbols:
    if var_a == i:
        var_a = tuple_1_symbols.index(i)
print("The index of element you'we typed is", var_a)

# HOMETASK 5 - REVERSISNG TUPLES
print("# HOMETASK 5 - REVERSISNG TUPLES")
reversed_tuples_numbers = tuple_1_numbers[::-1]
print(reversed_tuples_numbers)