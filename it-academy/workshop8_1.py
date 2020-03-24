# TASK 1
salaries = { "John": 15000, "Ann": 30000, "Mike": 12000, "Mary": 15000}
print(salaries["John"])
print(salaries["Ann"])

# TASK 2
if "Ann" in salaries:
    print("Ann’s salary is", salaries["Ann"])
else:
    print("Ann’s salary is not in my list.")


#
dict = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}
new_dict = {}
for k, v in dict.items():
    if v in new_dict:
        new_dict[v].append(k)
    else:
        new_dict[v] = [k]
print(new_dict)

var_a = "Ukraine"
d_countries = {"Ukraine": "Lviv", "Spain": "Madrid", "Italy": "Rome", "Great Britain": "London"}
new_dict_countries = {}
for k, v in d_countries.items():
    if v in new_dict_countries:
        new_dict_countries[v].append(k)
    else:
        new_dict_countries[v] = [k]
print(new_dict_countries)

if var_a in new_dict_countries:
    print(new_dict_countries[var_a])
