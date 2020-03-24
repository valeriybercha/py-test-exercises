# https://pythonworld.ru/osnovy/tasks.html

import math
import string

# ЗАДАЧА 1 - Простейшие арифметические операции. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть;
# * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
operator = input("Enter the operator: ")

def arithmetic(num1, num2, operator):

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Division to zero is not possible")
        else:
            return num1 / num2
    else:
        print("Operation unknown")

print("RESULT =", arithmetic(num1, num2, operator))


# ЗАДАЧА 2 - Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный,
# и False иначе.

year = int(input("Enter the year: "))

def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

print(is_year_leap(year))

if is_year_leap(year) == True:
    print("The year you've entered IS leap")
else:
    print("The year you've entered is NOT leap")

# ЗАДАЧА 3 - Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

side = int(input("Enter the square side dimension: "))

def square(side):

    # Variant 1
    # p = 4 * side
    # s = side ** 2
    # d = side * math.sqrt(2)
    # result = (p, s, d)
    # return result

    # Variant 2
    return 4 * side, side ** 2, side * round(math.sqrt(2), 2)

print("The Perimeter, Area and Digonal of the square are", square(side))


# ЗАДАЧА 4 - Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).

month_num = int(input("Enter a month number from 1 to 12: "))

def season(month_num):
    if month_num in range(1, 13):
        if month_num in range(3, 6):
            print("Spring")
        elif month_num in range(6, 9):
            print("Summer")
        elif month_num in range(9, 12):
            print("Autumn")
        else:
            print("Winter")
    else:
        print("You must enter the number in range 1 to 12")

season(month_num)

# ЗАДАЧА 5 - Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его
# вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

a = int(input("Enter the sum you want to deposit: "))
years = int(input("Enter the number of years of deposit: "))

def bank(a, years):
    sum = []
    for year in range(years):
        value = a * 1.1
        sum.append(value)
        a = value
    return round(sum[-1], 2)

print("You'll have -", bank(a, years), "on your deposit account")

# ЗАДАЧА 6 - Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно
# простое, и False - иначе.

num = int(input("Enter a number from 0 to 1000: "))

def is_prime(num):
    if num in range(0, 1001):
        if num == 2 or num == 3:
            return True
        elif num == 1 or num == 0:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
    else:
        print("You have to enter a number from 0 to 1000")

print(is_prime(num))

# ЗАДАЧА 7 - Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть
# в нашем календаре, и False иначе.

day = int(input("Enter a day of the month: "))
month = int(input("Enter the month number: "))
year = int(input("Enter a year: "))

def date(day, month, year):

    if month in range(1, 13) and day in range(1, 32) and year > 1:

        # Check the 2nd month - February which has only 28-29 days

        if month == 2 and day in range(1, 29):
            return True
        elif month == 2 and year % 4 == 0 and day in range(1, 30):
            return True

        # Check the first 7 months

        elif month in range(3, 8) or month == 1:
            if month % 2 != 0:
                if day in range(1, 32):
                    return True
                else:
                    return False
            elif month % 2 == 0:
                if day in range(1, 31):
                    return True
                else:
                    return False

        # Check the other months

        elif month in range(8, 13) or month == 1:
            if month % 2 == 0:
                if day in range(1, 32):
                    return True
                else:
                    return False
            elif month % 2 != 0:
                if day in range(1, 31):
                    return True
                else:
                    return False

        else:
            return False

    else:
        return False

print(date(day, month, year))


# ЗАДАЧА 8 - Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ
# шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с
# ключом. Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную
# строку.

message = (input("Enter the message you want to encrypt: "))
token = ("")

def XOR_cipher(message):
    # Creating symbols list
    token_list = []
    alphabet = list(string.ascii_letters)
    digits = list(string.digits)
    space = [" "]
    alpha_digits = alphabet + digits + space
    numbers = list()
    for i in range(len(alpha_digits)):
        numbers.append(i)

    numbers_str = [str(item) for item in numbers] # ''.join(str(e) for e in numbers)

    complex_numbers_str = ["aFg" + i for i in numbers_str]

    # Creating the dictionary based on previous created symbols list
    xor = dict(zip(alpha_digits, complex_numbers_str))
    #print(xor)

    message_list = list(message)

    for list_item in message_list:
        for dict_key in xor:
            if list_item == dict_key:
                dict_value = xor[dict_key]
                token_list.append(dict_value)
                token_list.append("z0i")

    token = ''.join(str(e) for e in token_list)
    print("Your token is -", token)

XOR_cipher(message)


token_to_decrypt = input("Enter the secret token: ")
decrypted_message = ("")

def XOR_uncipher(decrypted_message):

    for item in token_to_decrypt:
        token_to_decrypt_list = list(token_to_decrypt.split("z0i"))
    #print(token_to_decrypt_list)

    # Creating symbols list
    token_list = []
    alphabet = list(string.ascii_letters)
    digits = list(string.digits)
    space = [" "]
    alpha_digits = alphabet + digits + space
    numbers = list()
    for i in range(len(alpha_digits)):
        numbers.append(i)

    numbers_str = [str(item) for item in numbers] # ''.join(str(e) for e in numbers)

    complex_numbers_str = ["aFg" + i for i in numbers_str]

    # Creating the dictionary based on previous created symbols list
    xor = dict(zip(complex_numbers_str, alpha_digits))
    #print(xor)

    decrypted_message_list = []

    for list_item in token_to_decrypt_list:
        for dict_key in xor:
            if list_item == dict_key:
                dict_value = xor[dict_key]
                decrypted_message_list.append(dict_value)

    decrypted_message = ''.join(str(e) for e in decrypted_message_list)
    print(decrypted_message)

XOR_uncipher(decrypted_message)