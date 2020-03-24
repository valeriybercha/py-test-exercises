# TASK 1 - 1
print("# TASK 1 - 1")
import random
my_list = []
for i in range(0, 10):
    x = random.randint(1, 10)
    my_list.append(x)
print("- The original random list")
print(my_list)
my_list.reverse()
print("- Reversed list")
print(my_list)

# TASK 1 - 2
print("# TASK 1 - 2")
print("- The original list")
my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 10]
print(my_list_2)

list_count = []
for x in my_list_2:
    a = my_list_2.count(x)
    list_count.append(a)
print("- The 'counter' list")
print(list_count)

z = 0
result_list = []
for y in list_count:
    if y == 1:
        b = my_list_2[z]
        result_list.append(b)
    z += 1
print("- Results list")
print(result_list)

# TASK 1 - 3
print("# TASK 1 - 3")
print("- The original list")
print(my_list_2)
# Step to move elements
step = 3
# Moving element '5' by 'step' position
temp_5 = my_list_2[4]
my_list_2[4] = my_list_2[4 + step]
my_list_2[4 + step] = temp_5
my_list_2[4] = 0
# Moving element '6' by 'step' position
temp_5 = my_list_2[5]
my_list_2[5] = my_list_2[5 + step]
my_list_2[5 + step] = temp_5
my_list_2[5] = 0
print("- Result list")
print(my_list_2)

# TASK 1 - 4
print("# TASK 1 - 4")
import random
my_list_4 = []
for i in range(0, 10):
    x = random.randint(1, 10)
    my_list_4.append(x)
print("- The original random list")
print(my_list_4)
var_max = my_list_4.index(max(my_list_4))
var_min = my_list_4.index(min(my_list_4))
my_list_4[var_max], my_list_4[var_min] = my_list_4[var_min], my_list_4[var_max]
print("- Result list")
print(my_list_4)

# TASK 1 - 5
print("# TASK 1 - 5")
import random
my_list_4 = []
for i in range(0, 10):
    x = random.randint(1, 10)
    my_list_4.append(x)
print("- The original random list")
print(my_list_4)
var_max = my_list_4.index(max(my_list_4))
print("The position of value in the list is", var_max)
print("The biggest value in the list is", max(my_list_4))

# TASK 1 - 6
print("# TASK 1 - 6")
print("- Original list")
my_list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 11, 11, 11]
print(my_list_5)
list_count_5 = []
for x in my_list_5:
    a = my_list_5.count(x)
    list_count_5.append(a)
print("- The 'counter' list")
print(list_count_5)
var_max = list_count_5.index(max(list_count_5))
print("The value most presented in the list is", my_list_5[var_max])