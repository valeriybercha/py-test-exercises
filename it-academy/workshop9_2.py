# TASK 1
# var_a = ""
#while var_a != "@":

    #var_a = input("Enter a number : ")

    #list_a_str = var_a.split()

    #list_a_int = []
    #for item in list_a_str:
        #list_a_int.append(int(item))

    #list_a_sum = sum(list_a_int)
    #print(list_a_sum)

#print("That's all folks!")

# TASK 1 - 1
def sum_of_string(line):
    list_line = line.split()
    for i in range(len(list_line)):
        list_line[i] = int(list_line[i])
    return sum(list_line)

print("Enter a string of numbers or press '#'")
total = 0
while True:
    str = input()
    if "#" not in str:
        total += sum_of_string(str)
    else:
        break
print(total)

# TASK 2
def aaaa(vars):
    list_vars = vars.split()
    if len(list_vars) == 3:
         a = "Triangle"
    elif len(list_vars) == 2:
        a = "Triangle"
    elif len(list_vars) == 1:
        a = "Triangle"
    return a
print(aaaa(2, 2))
