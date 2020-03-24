# Task
goodFood = []
goodFood.append("burgers")
print(goodFood)

# Task
prerequisites = ["COP 2271c", "Introduction to Computation and Programming", 3, "Dr. Anderson" , 2015]
prerequisites.pop(4)
print(prerequisites)

# Task
prerequisites.remove("Dr. Anderson")
print(prerequisites)
prerequisites.remove(3)
print(prerequisites)

# Task
prerequisites.insert(1, "Test message")
print(prerequisites)

# Task
temp_s = ["test 1", "test 2", "test 3", "test 4"]
prerequisites.extend(temp_s)
print(prerequisites)

# Task
friends = ["Harry", "Cindy", "Emily", "Bob", "Cari", "Emily"]
if "Cindy" in friends:
    print("She's a friend")

n = friends.index("Emily")
print(n)

n2 = friends.index("Emily", n + 1)
print(n2)

# Task
for fruit in ["apple", "banana", "mango"]:
    print("I like", fruit)

# Task
fruit = ["apple", "banana", "mango"]
for i in range(len(fruit)):
    print("I like", fruit[i])

# Task
list_a = [x * 2 for x in range(1, 11)]
print(list_a)

# Task
counts = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

for i in range(7):
    for j in range(3):
        print("%8d" % counts [i][j], end="")
    print()