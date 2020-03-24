# HOMETASK 1 - SCHOOL DICTIONARY
print("# HOMETASK 1 - SCHOOL DICTIONARY")
print("You can type a classroom 'number' you want to check, 'update' to make modifications or 'stop' to quit program")
# Creating a dictionary with school classrooms
dict_school = {
    "1a": 20,
    "1b": 22,
    "1c": 19,
    "2a": 17,
    "2b": 15,
    "3a": 22,
    "4a": 19,
    "5a": 23,
    "6a": 25,
    "7a": 18,
    "7b": 12,
    "8a": 25,
    "9a": 22,
    "10a": 19
}

var_school = ""

while var_school != "stop" and var_school != "s":

    # Creating a variable 'var_school' for identifying the classroom
    var_school = input("Type a classroom you want to verify: ").lower()
    for key, value in dict_school.items():
        if var_school == key:
            print("The are", value, "pupils in the classroom", key)

    # Updating dictionary with information by typing the word 'update'
    if var_school == "update":

        # Modify, add or delete information in the 'dict_school' dictionary by typing in 'modify', 'add', 'delete' words
        ask_school = input("Type 'modify', 'add' or 'delete' to make changes to school dictionary: ")

        # Changing the number of pupils in one of the classrooms with 'modify' word or adding the new class with 'add' \
        # word
        if ask_school == "modify" or ask_school == "add":
            modify_school_key = \
                input("Type the number of the classroom you want make modifications or add the new one: ")
            modify_school_value = int(input("Type the new number of pupils in the classroom: "))
            dict_school[modify_school_key] = modify_school_value

        # Deleting one of the classrooms from dictionary with 'delete' word
        if ask_school == "delete":
            delete_school_key = input("Type the number of the classroom you want to delete: ")
            dict_school.pop(delete_school_key)
        print("- Updated dictionary with modifications made")
        print(dict_school)
print("Thank for using our program. See you later")

# HOMETASK 2 - WORD SYNONYMS AND SENTENCES
print("# HOMETASK 2 - WORD SYNONYMS AND SENTENCES")
print("You can type a word to see it's synonym, 'update' to make modifications, 'sentence' to type a sentence \
or 'stop' to quit program")

# Creating an orignal dictionary
dict_synonyms = {
    "hello": ["greeting", "hi", "howdy"],
    "pleasant": ["enjoyable", "gracious", "satisfying"],
    "good": ["great", "positive"],
    "bad": ["awful", "poor", "sad"],
    "sunrise": ["daylight", "morning"]
}

# Creating a dictionary with string values
dict_synonyms_str = {}
for key, value in dict_synonyms.items():
    for i in dict_synonyms:
        c = str(value[0])
        dict_synonyms_str[key] = c

var_inp = ""
var_add = ""

# Printing the synonyms words in a 'while' loop while the typed word is not equal to 'stop' or 's'
while var_inp != "stop":

    # Creating the reversed 'synonyms' dictionary with 'defaultdict' import in a 'while' loop
    from collections import defaultdict
    dict_synonyms_reversed = defaultdict(list)
    for key, value in dict_synonyms.items():
        for i in value:
            dict_synonyms_reversed[i].append(key)

    # Creating string values for reversed dictionary
    dict_synonyms_reversed_str = {}
    for key, value in dict_synonyms_reversed.items():
        for i in dict_synonyms_reversed:
            c = str(value[0])
            dict_synonyms_reversed_str[key] = c

    # Typing a word to print back it's synonyms
    var_inp = input("Type a word to print back it synonyms: ").lower()
    if var_inp in dict_synonyms:
        synonym_word = dict_synonyms[var_inp]
        print(", ".join(synonym_word))
    elif var_inp in dict_synonyms_reversed:
        synonym_word = dict_synonyms_reversed[var_inp]
        print(", ".join(synonym_word))

    # Updating dictionary with information by typing the word 'update'
    if var_inp == "update":
        import re
        add_word = input("Type the word you want to add: ").lower()
        list_add_word = re.sub("[^\w]", " ",  add_word).split()
        add_word_synonym = input("Type the synonyms for the word with coma: ").lower()
        list_add_word_synonym = re.sub("[^\w]", " ",  add_word_synonym).split()
        dict_synonyms[add_word] = list_add_word_synonym
        print("Thank you! You've added '", add_word, "' = '", add_word_synonym,"' to dictionary")

    # Changing the word in the sentence by it's synonym with 'sentence' or 's' words
    if var_inp == "sentence" or var_inp == "s":
        import re
        add_sentence = input("Type a sentence: "). lower()

        # Checking the matching words in input sentence with dictionaries
        for key, value in dict_synonyms_reversed_str.items():
            for i in dict_synonyms_reversed_str:
                add_sentence = add_sentence.replace(i, dict_synonyms_reversed_str[i])
        for key, value in dict_synonyms_str.items():
            for i in dict_synonyms_str:
                add_sentence = add_sentence.replace(i, dict_synonyms_str[i])
        print(add_sentence)
print("Thank's for using our synonym program. See you later alligator!")

# HOMETASK 3 - CREATING A DICTIONARY FROM A STRING SENTENCE
print("# HOMETASK 3 - CREATING A DICTIONARY FROM A STRING SENTENCE")

# The string sentence
var_sentence = "See you later alligator. See you later alligator. See you sometime".lower()

# Creating a list from sentence for key
import re
list_key = re.sub("[^\w]", " ",  var_sentence).split()
print(list_key)

# Creating a list with counters for values
list_value = []
for i in list_key:
    a = list_key.count(i)
    list_value.append(a)
print("- The 'counter' list")
print(list_value)

# Creating a dictionary from two created lists - method 1
dict_str_sentence = {}
for key in list_key:
    for value in list_value:
        dict_str_sentence[key] = value
print(dict_str_sentence)

# Creating a dictionary from two created lists - method 2
dict_str_sentence = dict(zip(list_key, list_value))
print(dict_str_sentence)