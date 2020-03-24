# Hometask 1 - min-max values
print("# Hometask 1 - min-max values")
mm_a = int(input("Enter your first value: "))
mm_b = int(input("Enter your second value: "))
mm_c = int(input("Enter your third value: "))

mm_x = max(mm_a, mm_b, mm_c)
print("The max value you've entered is " + str(mm_x))
mm_x = min(mm_a, mm_b, mm_c)
print("The min value you've entered is " + str(mm_x))

# Hometask 2 - weight in kg and t
print("# Hometask 2 - weight in kg and t")
p_grams = int(input("Enter the weight in grams: "))
p_kilograms = p_grams / 1000
p_tons = p_kilograms / 1000
print("The weight you've entered in grams is " + str(p_grams) + " g")
print("The weight in kilograms will be " + str(round(p_kilograms, 4)) + " kg")
print("The weight in tons will be " + str(round(p_tons, 5)) + " t")

# Hometask 3 - convertion to kbytes and mbytes
print("# Hometask 3 - convertion to kbytes and mbytes")
bytes = int(input("Enter the number of bytes: "))
kbytes = bytes / 1024
mbytes = kbytes / 1024
print("The number of bytes you've entered is " + str(bytes))
print("Convertion to kbytes: " + str(round(kbytes, 5)) + " kB")
print("Convertion to mbytes: " + str(round(mbytes, 5)) + " MB")

# Hometask 4 - swapping the values method 1
print("# Hometask 4 - swapping the values method 1")
swap_a = input("Type the first variable A: ")
swap_b = input("Type the second variable B: ")
tmp = swap_a
swap_a = swap_b
swap_b = tmp

print("Result for swapped variable A is " + swap_a)
print("Result for swapped variable B is " + swap_b)

# Hometask 4 - swapping the values method 2
print("# Hometask 4 - swapping the values method 2")
swap_d = input("Type the first variable D: ")
swap_e = input("Type the second variable E: ")
swap_d, swap_e = swap_e, swap_d

print("Result for swapped variable D is " + swap_d)
print("Result for swapped variable E is " + swap_e)

# Hometask 5 - rectangle area calculation
print("# Hometask 5 - rectangle area calculation")
r_length = int(input("Insert the value for the length: "))
r_width = int(input("Insert the value for the width: "))
r_area = r_length * r_width
print("Calculated rectangle area is " + str(r_area))
r_perimeter = 2 * (r_length + r_width)
print("Calculated rectangle perimeter is " + str(r_perimeter))

# Hometask 6 - circle area and calculation
print("# Hometask 6 - circle area and calculation")
import math
c_radius = int(input("Insert circle radius: "))
c_area = math.pi * (c_radius ** 2)
print("Calculated circle area is " + str(round(c_area, 2)))
c_perimeter = 2 * math.pi * c_radius
print("Calculated circle perimeter is " + str(round(c_perimeter, 2)))

# Hometask 7 - the Pythagorean theorem
print("# Hometask 7 - the Pythagorean theorem")
import math
pyt_a = int(input("Insert variable for side A: "))
pyt_b = int(input("Insert variable for side B: "))
pyt_c = math.sqrt(pyt_a ** 2 + pyt_b **2)
print("Variable for side C will be equal to: " + str(round(pyt_c, 2)))

# Hometask 8 - painting the tank
print("# Hometask 8 - painting the tank")
import math
tank_h = int(input("Enter the height of the tank: "))
tank_d = int(input("Enter the diameter of the tank: "))
tank_r = tank_d / 2
tank_area = 2 * math.pi * tank_r * (tank_h + tank_r)
print("The outside surface of the tank is " + str(round(tank_area, 2)))
tank_full_area = tank_area * 2
print("The full (outside and inside) surface of the tank is " + str(round(tank_full_area, 2)))
print("The average consumption of paint per 1m2 for applying coating on tank \
surface is 130 grams per square meter.")

paint_grams = tank_full_area * 130
paint_litres = paint_grams / 1000
print("The amount of paint needed for painting the tank is " + str(round(paint_grams, 2)) + " grams or " \
      + str(round(paint_litres, 2))+ " litres" )
paint_075 = paint_litres / 0.75
paint_25 = paint_litres / 2.5
paint_5 = paint_litres / 5
print("For this you'll need " + str(round(paint_075)) + " pcs of paints of 0,75l; or " + str(round(paint_25)) + \
      " pcs of paints of 2,5l; or " + str(round(paint_5)) + " pcs of paints of 5l.")