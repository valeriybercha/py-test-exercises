# TASK 1
r = (1, 2, 3)
a = list(r)
print(a)

a = tuple(r)
print(a)

print(r[1])

b = 1, 2, 3
print(b[0])

c = 1231231, 2342342, 234234
u = c, 23423, 234234, 4, 4
print(u)

# TASK 2
print(len(u))
print(len(b))
print(max(b))

# TASK 3
a = "1", "2", "3", 4, 5
print(tuple(a))

a = (5, 7, 9, 4)
print(sorted(a))

# TASK 4
b = "test",
print(b)

cheesePie = ["Creamy garlic", "Parmesan sauce", "Cheese", "Cheese", "Toasted Parmesan"]
cheesePizza = set(cheesePie)
print(cheesePizza)
n_of_ing = len(cheesePizza)
print(n_of_ing)
if "Creamy garlic" in cheesePizza:
    print("A cheeze pizza contains")
else:
    print("Cheeze pizza does not contain")

print("The ingredients in a cheese pizza are:")
for ingredient in cheesePizza :
    print(ingredient)

print("The ingredients in a cheese pizza are:")
for ingredient in sorted(cheesePizza):
    print(ingredient)

cheesePizza.add("Mushrooms")
print(cheesePizza)

cheesePizza.remove("Mushrooms")
print(cheesePizza)

cheesePizza.clear()
print(cheesePizza)

cheesePizza.issubset(pepperoniPizza)