# TASK - CREATING UKR-ENG-UKR DICTIONARY
print("# TASK - CREATING UKR-ENG-UKR DICTIONARY")
print("Welcome to our Ukrainian-English-Ukrainian dictionary")
print("You can type a word in 'Ukrainian' or 'English' language. Thew program will translate it for you.")
print("To quit stop the program - just type the word 'stop' or 'стоп' and the program will stop translating")
var_inp = ""

# Creating a 'ukr-eng' dictionary
eng_ukr = {
    "hello": "привіт",
    "summer": "літо",
    "winter": "зима",
    "spring": "весна",
    "autumn": "осінь",
    "stop": "стоп",
    "sun": "сонце"
}

# Creating 'eng-ukr' dictionary by swapping the key and values in the 'python dictionary'
ukr_eng = {}
for key, value in eng_ukr.items():
    if value in ukr_eng:
        ukr_eng[value].append(key)
    else:
        ukr_eng[value] = key

# Translating the words in a 'while' loop while the inserted word is not equal to 'stop'
while var_inp != "stop" and var_inp != "стоп":
    var_inp = input("Type a word in English or Ukrainian: ").lower()
    if var_inp in eng_ukr:
        translated_word = eng_ukr[var_inp]
        print(translated_word)
    elif var_inp in ukr_eng:
        translated_word = ukr_eng[var_inp]
        print(translated_word)
    else:
        # If there is a mistake or there is no word in the dictionary we can actually add this word to dictionary
        print("Sorry, but we couldn't translate the word you'we typed in")
        var_add = input("Do you want to add this word to dictionary? Type 'Y/N': ").lower()
        if var_add == "y":
            eng_word = input("Type the adding word in English: ").lower()
            ukr_word = input("Type the adding translation in Ukrainian: ").lower()
            eng_ukr[eng_word] = ukr_word
            ukr_eng[ukr_word] = eng_word
            print("Thank you! You've added '", eng_word, "' = '", ukr_word,"' to dictionary")
print("Thank you for using our dictionary. Have a nice day")
