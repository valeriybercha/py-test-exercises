# TASK 1
t = (8, 7, 6, 5, 4, 3, 2, 1)
l = list(sorted(t))
print(l)

# TASK 2
grades = [("Ann", 4), ("Bob", 2), ("Elizabeth", 3), ("Dan", 5)]
for x in grades:
    print("Hello,", x[0], "! Your grade is", x[1])

# TASK 3
names = ("Ann", "Bob", "Elizabeth", "Mr. McMullen", "Mrs. Smith")
for x in names:
    if x[:2] == "Mr":
        print("Good morning, ", x)
    else:
        print("Hello, ", x)

# TASK 4
a = ['boat', 'bus', 'plane', 'train']
b = set(a)
print(b)

# TASK 5
a = ('cyclist', 'driver', 'pedestrian')
b = set(a)
print(b)

# TASK 6
letters = set()
for i in range(65, 91):
    letters.add(chr(i))
for i in range(97,123):
    letters.add(chr(i))
print(sorted(letters))
for i in sorted(letters):
    print(i)

# TASK 7
a = {"a", "e", "i", "o", "u", "y"}
