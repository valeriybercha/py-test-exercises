# TASK - CREATING UKR-ENG-UKR DICTIONARY
print("# TASK - CREATING UKR-ENG-UKR DICTIONARY")
print("Welcome to our Ukrainian-English-Ukrainian dictionary")
print("You can type a word in 'Ukrainian' or 'English' language. The program will translate it for you.")
print("To stop the program - just type the word 'stop' or 'стоп' and the program will stop translating")
var_inp = ""
var_add = ""
# Creating a 'ukr-eng' dictionary
eng_ukr = {
    "hello": ["привіт", "вітаю", "доброго дня", "доброго вечора"],
    "summer": ["літо"],
    "winter": ["зима"],
    "spring": ["весна"],
    "autumn": ["осінь"],
    "stop": ["стоп"],
    "sun": ["сонце"]
}
# Creating 'eng-ukr' dictionary by swapping the key and values in the 'python dictionary'
from collections import defaultdict
ukr_eng = defaultdict(list)
for key, value in eng_ukr.items():
    for i in value:
        ukr_eng[i].append(key)

# Translating the words in a 'while' loop while the inserted word is not equal to 'stop'
while var_inp != "stop" and var_inp != "стоп":
    var_inp = input("Type a word in English or Ukrainian: ").lower()
    if var_inp in eng_ukr:
        translated_word = eng_ukr[var_inp]
        print(", ".join(translated_word))
    elif var_inp in ukr_eng:
        translated_word = ukr_eng[var_inp]
        print(", ".join(translated_word))
    else:
        # If there is a mistake or there is no word in the dictionary we can actually add the word
        import re
        print("Sorry, but we couldn't translate the word you'we typed in")
        var_add = input("Do you want to add this word to dictionary? Type 'Y/N': ").lower()
        if var_add == "y":
            eng_word = input("Type the adding word in English: ").lower()
            list_eng_word = re.sub("[^\w]", " ",  eng_word).split()
            ukr_word = input("Type the adding translation in Ukrainian: ").lower()
            list_ukr_word = re.sub("[^\w]", " ",  ukr_word).split()
            eng_ukr[eng_word] = list_ukr_word
            ukr_eng[ukr_word] = list_eng_word
            print("Thank you! You've added '", eng_word, "' = '", ukr_word,"' to dictionary")
print("Thank you for using our dictionary. Have a nice day")
