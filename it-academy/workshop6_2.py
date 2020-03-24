# TASK 2 - 1
print("# TASK 2 - 1")
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
counts = [
    [var_0_0, var_0_1, var_0_2, var_0_3],
    [var_1_0, var_1_1, var_1_2, var_1_3],
    [var_2_0, var_2_1, var_2_2, var_2_3],
    [var_3_0, var_3_1, var_3_2, var_3_3]
]

for i in range(4):
    for j in range(4):
        print("%8d" % counts[i][j], end="")
    print()

# TASK 2 - 2
print("# TASK 2 - 2")
print("Minimal value of 3rd row is", min(counts[2]))
print("Maximum value of 2nd column is", max([_[1] for _ in counts]))

# TASK 2 - 3
print("TASK 2 - 3")
temp_3 = counts[0][1]
counts[0][1] = counts[0][3]
counts[0][3] = temp_3
temp_3 = counts[1][1]
counts[1][1] = counts[1][3]
counts[1][3] = temp_3
temp_3 = counts[2][1]
counts[2][1] = counts[2][3]
counts[2][3] = temp_3
temp_3 = counts[3][1]
counts[3][1] = counts[3][3]
counts[3][3] = temp_3
for i in range(4):
    for j in range(4):
        print("%8d" % counts[i][j], end="")
    print()

# TASK 2 - 4
print("# TASK 2 - 4")
print("Diagonal values of the list are", [r[i] for i, r in enumerate(counts)])
sum_diagonal = ([r[i] for i, r in enumerate(counts)])
print("The sum of diagonal values is equal to", sum(sum_diagonal))