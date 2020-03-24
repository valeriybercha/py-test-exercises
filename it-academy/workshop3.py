# Task 1
fuelAmount = float(input("Insert fuel amount: "))
fuelCapacity = int(input("Insert fuel capacity: "))
if fuelAmount >= 0 and fuelAmount <= fuelCapacity / 10:
    print("RED color. Fuel level is low. Please refuel.")
elif fuelAmount > fuelCapacity / 10 and fuelAmount <= fuelCapacity:
    print("GREEN color. Fuel level is ok.")
else:
    print("Oops. Something goes wrong. We cannot calculate the amount of fuel")

# Task 2-1
var_a = int(input("Insert a value: "))

if var_a % 4 == 0:
    print("PAIR number and IS multiple of 4")
elif var_a % 2 == 0:
    print("PAIR number but NOT multiple of 4")
else:
    print("ODD number")

# Task 2-2
var_b = int(input("Insert a value: "))

if var_b % 5 == 0 and var_b % 2 != 0:
    print("ODD number and IS multiple of 5")
elif var_b % 5 == 0 and var_b % 2 == 0:
    print("IS multiple of 5 but PAIR number")
elif var_b % 2 != 0:
    print("ODD number, but NOT multiple of 5")
else:
    print("PAIR number")

# Task 2-3
var_c = int(input("Insert a value: "))
if var_c <0:
    print("The number is negative")
elif var_c == 0:
    print("The number is equal to ZERO")
else:
    print("The number is positive")

# Task 2-4 Model 1
var_d = int(input("Insert a value: "))
if var_d >= 1 and var_d <= 36 and var_d % 2 == 0:
    print("You have the UPPER place which is situated in COUPE carriage")
elif var_d >= 1 and var_d <= 36 and var_d % 2 != 0:
    print("You have the BOTTOM place which is situated in COUPE carriage")
elif var_d > 36 and var_d <= 54 and var_d % 2 == 0:
    print("You have the UPPER place which is situated in SIDE carriage")
elif var_d > 36 and var_d <= 54 and var_d % 2 != 0:
    print("You have the BOTTOM place which is situated in SIDE carriage")
else:
    print("Sorry but we cannot find your place. Try again")