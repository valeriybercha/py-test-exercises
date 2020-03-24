# HOMETASK 1 - THREE LISTS
print("# HOMETASK 1 - THREE LISTS")
import random
my_list_1 = []
for i in range(0, 10):
    x = random.randint(1, 10)
    my_list_1.append(x)
print("- The original random list")
print(my_list_1)

my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("- The second list")
print(my_list_2)

i = 0
my_list_3 = []
for x in my_list_2:
    a = my_list_1[i] + my_list_2[i]
    my_list_3.append(a)
    i += 1
print("- The resulted list with sums from 1 and 2")
print(my_list_3)

# HOMETASK 2 - SUM AND MULTIPLICATION OF LIST ITEMS
print("# HOMETASK 2 - SUM AND MULTIPLICATION OF LIST ITEMS")
my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
print("- The original list")
print(my_list_2)
print("The sum of the list is equal to", sum(my_list_2))
i = 1
for x in my_list_2:
    i = i * x
print("Multiplication of all elements in a list is equal to", i)

# HOMETASK 3 - POSITIVE, NEGATIVE AND ZERO ELEMENTS IN A LIST
print("# HOMETASK 3 - POSITIVE, NEGATIVE AND ZERO ELEMENTS IN A LIST")
import random
my_list_3 = []
for i in range(0, 10):
    x = random.randint(-5, 4)
    my_list_3.append(x)
print("- The original random list")
print(my_list_3)

z = 0
result_list = []
for y in my_list_3:
    if y > 0:
        b = my_list_3[z]
        result_list.append(b)
    z += 1
print("- Results list of POSITIVE elements")
print(result_list)

z = 0
result_list = []
for y in my_list_3:
    if y == 0:
        b = my_list_3[z]
        result_list.append(b)
    z += 1
print("- Results list of ZERO elements")
print(result_list)

z = 0
result_list = []
for y in my_list_3:
    if y < 0:
        b = my_list_3[z]
        result_list.append(b)
    z += 1
print("- Results list of NEGATIVE elements")
print(result_list)

# HOMETASK 4 - POSITIVE AND NEGATIVE ELEMENTS IN TWO LISTS
print("# HOMETASK 4 - POSITIVE AND NEGATIVE ELEMENTS IN TWO LIST")
import random
my_list_4 = []
for i in range(0, 10):
    x = random.randint(-5, 5)
    my_list_4.append(x)
print("- The original random list")
print(my_list_4)

z = 0
my_list_4_pos = []
for y in my_list_4:
    if y > 0:
        b = my_list_4[z]
        my_list_4_pos.append(b)
    z += 1
print("- Results list with POSITIVE numbers")
print(my_list_4_pos)

z = 0
my_list_4_neg = []
for y in my_list_4:
    if y < 0:
        b = my_list_4[z]
        my_list_4_neg.append(b)
    z += 1
print("- Results list with NEGATIVE numbers")
print(my_list_4_neg)

# HOMETASK 5 - DELETING NEGATIVE NUMBERS FROM A LIST
print("# HOMETASK 5 - DELETING NEGATIVE NUMBERS FROM A LIST")
import random
my_list_5 = []
for i in range(0, 10):
    x = random.randint(-5, 5)
    my_list_5.append(x)
print("- The original random list")
print(my_list_5)

# VARIANT 1 - with counter elements
list_count = []
for x in my_list_5:
    a = my_list_5.count(x)
    list_count.append(a)
print("- The 'counter' list")
print(list_count)

z = 0
result_list = []
for y in list_count:
    if y == 1:
        b = my_list_5[z]
        result_list.append(b)
    z += 1
print("- Results list")
print(result_list)

for x in result_list:
    if x < 0:
        result_list.remove(x)
    x += 1
print("- The list with removed negative values  - VARIANT 1")
print(result_list)

# VARIANT 2
for x in my_list_5:
    if x < 0:
        my_list_5.remove(x)
    x += 1
print("- The list with removed negative values - VARIANT 2")
print(my_list_5)

# HOMETASK 6 - INDEXING EVEN NUMBERS IN A LIST
print("# HOMETASK 6 - INDEXING EVEN NUMBERS IN A LIST")
my_list_6 = [1, 2, 7, 6, 10, 9, 14]
print("- The original list")
print(my_list_6)
x = 1
my_list_6_index = []
while x % 2 == 0:
    a = my_list_6_index.index(x)
    my_list_6_index.append(a)
    x += 1
print("The indexed list with even numbers")
print(my_list_6_index)

# HOMETASK 7 - UNIQUE ELEMENTS IN THE LIST
print("# HOMETASK 7 - UNIQUE ELEMENTS IN THE LIST")
print("- The original list")
my_list_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 10]
print(my_list_7)

list_count = []
for x in my_list_7:
    a = my_list_7.count(x)
    list_count.append(a)
print("- The 'counter' list")
print(list_count)

z = 0
result_list = []
for y in list_count:
    if y == 1:
        b = my_list_7[z]
        result_list.append(b)
    z += 1
print("- Results list")
print(result_list)

# HOMETASK 8 - SWAP MIN AND MAX VALUES IN A LIST
print("# HOMETASK 8 - SWAP MIN AND MAX VALUES IN A LIST")
import random
my_list_8 = []
for i in range(0, 10):
    x = random.randint(1, 10)
    my_list_8.append(x)
print("- The original random list")
print(my_list_8)
var_max = my_list_8.index(max(my_list_8))
var_min = my_list_8.index(min(my_list_8))
my_list_8[var_max], my_list_8[var_min] = my_list_8[var_min], my_list_8[var_max]
print("- Result list")
print(my_list_8)