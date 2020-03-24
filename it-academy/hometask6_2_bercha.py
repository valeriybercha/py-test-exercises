# HOMETASK 1 - SUM OF ROWS AND COLS IN A 2D LIST
print("# HOMETASK 1 - SUM OF ROWS AND COLS IN A 2D LIST")
list_1 = [
    [1, 2, 3],
    [4, 4, 5],
    [6, 7, 8],
    [9, 10, 11],
    [12, 13, 14],
    [15, 16, 17]
]
# The original list
print("- The original list")
for i in range(6):
    for j in range(3):
        print("%8d" % list_1[i][j], end="")
    print()

row_1 = sum(list_1[0])
row_2 = sum(list_1[1])
row_3 = sum(list_1[2])
row_4 = sum(list_1[3])
row_5 = sum(list_1[4])
row_6 = sum(list_1[5])

row_list = [row_1, row_2, row_3, row_4, row_5, row_6]

col_1 = sum([_[0] for _ in list_1])
col_2 = sum([_[1] for _ in list_1])
col_3 = sum([_[2] for _ in list_1])

col_list = [col_1, col_2, col_3]

# List with COLS values
print("- List with COLS values")
list_1.append(col_list)
for i in range(7):
    for j in range(3):
        print("%8d" % list_1[i][j], end="")
    print()

# List with ROWS values
print("- List with ROWS values")
list_1 = [x + row_list for x in list_1]
for i in range(7):
    for j in range(4):
        print("%8d" % list_1[i][j], end="")
    print()

# TASK 2 - THE SUM OF TWO-DIGIT NUMBERS IN A MATRIX
print("# TASK 2 - THE SUM OF TWO-DIGIT NUMBERS IN A MATRIX")
import random
my_list_2 = []
for i in range(0, 15):
    x = random.randint(0, 999)
    my_list_2.append(x)
print("- The original random list")
print(my_list_2)

z = 0
result_list = []
for y in my_list_2:
    if y >= 10 and y <= 99:
        b = my_list_2[z]
        result_list.append(b)
    z += 1
print("- Results list of TWO-DIGIT ELEMENTS elements")
a = 1
sum_list = []
for x in result_list:
    sum_list.append(a)
print("There are", sum(sum_list), "TWO-DIGIT elements in a list")

# HOMETASK 3 - SUM OF INPUT ELEMENTS IN A MATRIX
print("# HOMETASK 3 - SUM OF INPUT ELEMENTS IN A MATRIX")
var_0_0 = int(input("Input the 1 number: "))
var_0_1 = int(input("Input the 2 number: "))
var_0_2 = int(input("Input the 3 number: "))
var_0_3 = int(input("Input the 4 number: "))
var_1_0 = int(input("Input the 5 number: "))
var_1_1 = int(input("Input the 6 number: "))
var_1_2 = int(input("Input the 7 number: "))
var_1_3 = int(input("Input the 8 number: "))
var_2_0 = int(input("Input the 9 number: "))
var_2_1 = int(input("Input the 10 number: "))
var_2_2 = int(input("Input the 11 number: "))
var_2_3 = int(input("Input the 12 number: "))
var_3_0 = int(input("Input the 13 number: "))
var_3_1 = int(input("Input the 14 number: "))
var_3_2 = int(input("Input the 15 number: "))
var_3_3 = int(input("Input the 16 number: "))

list_3 = [
    [var_0_0, var_0_1, var_0_2, var_0_3],
    [var_1_0, var_1_1, var_1_2, var_1_3],
    [var_2_0, var_2_1, var_2_2, var_2_3],
    [var_3_0, var_3_1, var_3_2, var_3_3]

]

row_1 = sum(list_3[0])
row_2 = sum(list_3[1])
row_3 = sum(list_3[2])
row_4 = sum(list_3[3])

row_list = [row_1, row_2, row_3, row_4]

# List with ROWS values
print("- List with ROWS values")
list_3.append(row_list)
for i in range(5):
    for j in range(4):
        print("%8d" % list_3[i][j], end="")
    print()

# HOMETASK 4 - MIN AND MAX ELEMENTS IN A MATRIX
print("# HOMETASK 4 - MIN AND MAX ELEMENTS IN A MATRIX")
# Creating a list
list_4 = [
    [1, 2, 3],
    [4, 4, 5],
    [6, 1, 8],
    [9, 10, 11],
    [12, 13, 14],
    [15, 16, 17]
]

# Printing the original list
print("- The original list")
for i in range(6):
    for j in range(3):
        print("%8d" % list_4[i][j], end="")
    print()

# Finding the minimal values in the list columns
min_col_1 = min([_[0] for _ in list_4])
min_col_2 = min([_[1] for _ in list_4])
min_col_3 = min([_[2] for _ in list_4])

# Creating a list with minimal column values and finding the maximal value between them
res_list = [min_col_1, min_col_2, min_col_3]
print("Minimum coloms values are",res_list)
print("Maximum number is equal to",max(res_list))

# HOMETASK 5 - THIRD LIST WITH ELEMENTS FROM FIRST TWO LISTS
print("# HOMETASK 5 - THIRD LIST WITH ELEMENTS FROM FIRST TWO LISTS")
x_5 = ""
y_5 = ""
list_5_1 = []
list_5_2 = []
list_count = 0

# Building the 1st list
for list_count in range(10):
        list_count += 1
        print("You insert the", list_count, "value")
        x_5 = int(input("Insert a value in the 1st list: "))
        list_5_1.append(x_5)
print("The 1st list is", list_5_1)

# Building the 2nd list
for list_count in range(10):
        list_count += 1
        print("You insert the", list_count, "value")
        y_5 = int(input("Insert a value in the 2nd list: "))
        list_5_2.append(y_5)
print("The 2nd list is", list_5_2)

# Building the 3rd list
list_5_3 = []
for z in list_5_1:
    if z in list_5_2:
        list_5_3.append(z)
print("The resulted 3rd list", list_5_3)



# HOMETASK 6 - SWAP DIAGONAL AND COUNTER-DIAGONAL VALUES IN A MATRIX
print("# HOMETASK 6 - SWAP DIAGONAL AND COUNTER-DIAGONAL VALUES IN A MATRIX")
import random

# Creating an original, random matrix with numbers from 1 to 10 and in range 10
print("- The original matrix")
list_6 = [[random.randint(1, 10) for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        print("%8d" % list_6[i][j], end="")
    print()

# Printing the diagonals values
list_diag = [r[i] for i, r in enumerate(list_6)]
list_diag_inv = [r[-i-1] for i, r in enumerate(list_6)]
print("Diagonal values are", list_diag)
print("Inversed diagonal values are", list_diag_inv)

# Swapping the values of two diagonals with 'temp' variable
for i in range(10):
    for j in range(10):
        if i == j:
            temp_var = list_6[i][j]
            list_6[i][j] = list_6[i][10 - j - 1]
            list_6[i][10 - j - 1] = temp_var

# Printing the resulted matrix
print("- The resulted matrix")
for i in range(10):
    for j in range(10):
        print("%8d" % list_6[i][j], end="")
    print()

