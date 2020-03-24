# Task 1
num_a = int(input("Insert the first number: "))
num_b = int(input("Insert the second number: "))
calc_num = 0
while num_a <= num_b:
    if num_a % 2 == 0:
        calc_num = calc_num + num_a
    num_a += 1
print("The sum is equal to " +str(calc_num))

# Task 2
num_c = ""
stop_op = "0"
num_d = ""
calc_op = ""

while calc_op != stop_op:
    num_c = int(input("Insert the first number: "))
    calc_op = input("Insert the operator: ")
    num_d = int(input("Insert the second number: "))
    if calc_op == "+":
        calc_num = num_c + num_d
        print("The output is " + str(int(calc_num)))
    elif calc_op == "-":
        calc_num = num_c - num_d
        print("The output is " + str(int(calc_num)))
    elif calc_op == "/":
        calc_num = num_c / num_d
        print("The output is " + str(int(calc_num)))
    elif calc_op == "*":
        calc_num = num_c * num_d
        print("The output is " + str(int(calc_num)))
    elif num_d == 0:
        print("It is impossible to divide by 0")
    else:
        print("Seems that an error appeared! Try again")

print("Calculation has stop")

# Task 3
user_name = input("Enter your name: ")
i = 0
while i < len(user_name):
    letter = user_name[i]
    print(letter)
    i += 1

# Task 4
num_a = int(input("Insert the first number: "))
num_b = int(input("Insert the second number: "))
calc_num = 0
calc_step = 1
num_b += calc_step
for var_c in range (num_a, num_b):
    if num_a % 2 != 0:
        calc_num = calc_num + num_a
    num_a += 1
print("The sum is equal to " +str(calc_num))