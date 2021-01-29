# LEARNING PATH - Learn Python basics with Wonder Woman


# CHALLENGE - Decode a full word with a Caesar cipher

def lassoLetter(letter, shiftAmount):
    x = ord(letter.lower()) + shiftAmount
    return chr(x) if x in range(96, 122) else (chr((x - 122) + 96) if shiftAmount > 0 else chr(122 - (96 - x)))  

def lassoWord(word, shiftAmount):
    decodedLetter = ""
    for letter in word:
        decodedLetter += lassoLetter(letter, shiftAmount)
    return decodedLetter

print("Shifting terra by 13 gives: \n" + lassoWord( "terra", 13 ))


# CHALLENGE - Use the Lasso decoder to reveal the secret message

# Secret message: WHY(13) 4th, 1984 oskza(-18) + ohupo(-1) ED(25)

scrt_msg = ["WHY", "4th,", "1984", "oskza", "ohupo", "ED"]

print(f"{lassoWord(scrt_msg[0], 13)} {scrt_msg[1]} {scrt_msg[2]} {lassoWord(scrt_msg[3], -18)}{lassoWord(scrt_msg[4], -1)} {lassoWord(scrt_msg[5], 25)}")


# CHALLENGE - Completing the WONDER WOMAN 1984 personality quiz

# ask the first question
def wonder_woman_quiz_activity(qstn):
    return "Nice choice" if qstn.lower() == "a" else ("Sounds fun" if qstn.lower() == "b" else "You must type A or B, let's just say you like to read.")

# ask the second question
def wonder_woman_quiz_job(qstn):
    return "Curator, Nice choice!" if qstn.lower() == "a" else ("Running a business? Sounds fun!" if qstn.lower() == "b" else "You must type A or B, let's just say you want to be a curator at the Smithsonian")

# ask the third question
def wonder_woman_quiz_value(qstn):
    return "Money, Nice choice!" if qstn.lower() == "a" else ("Love? Sounds fun!" if qstn.lower() == "b" else "You must type A or B, let's just say money is more important to you.")

# ask the fourth question
def wonder_woman_quiz_decade(qstn):
    return "1910s, Nice choice!" if qstn.lower() == "a" else ("1980s? Sounds fun!" if qstn.lower() == "b" else "You must type A or B, let's just say the 1910s is your favorite decade.")

# ask the fifth question
def wonder_woman_quiz_travel(qstn):
    return "Driving, Nice choice!" if qstn.lower() == "a" else ("Flying? Sound fun!" if qstn.lower() == "b" else "You must type A or B, let's just say your favorite way to travel is by driving")

# wonder woman personality quiz
def wonder_woman_quiz_personality(arr):
    diana_like = 0
    steve_like = 0
    max_like = 0
    barbara_like = 0

    # update scoring variables based on activity choise
    if arr[0].lower() == "a":
        diana_like += 1
        barbara_like += 1
    else:
        max_like += 1
        steve_like += 1
    
    # update scoring variables based on job choise
    if arr[1].lower() == "a":
        diana_like += 2
        barbara_like += 2
        steve_like -= 1
    else:
        max_like += 2

    # update scoring variables based on the value choice
    if arr[2].lower() == "a":
        diana_like = diana_like - 1
        max_like = max_like + 2
    else:
        diana_like = diana_like + 1
        steve_like = steve_like + 2
        barbara_like = barbara_like + 1

    # update scoring variables based on the decade choice
    if arr[3].lower() == "a":
        steve_like = steve_like + 2
        diana_like = diana_like + 1
    else:
        max_like = max_like + 1
        barbara_like = barbara_like + 2

    # update scoring variables based on the travel choice
    if arr[4].lower() == "a":
        max_like = max_like + 2
        barbara_like = barbara_like - 1
    else:
        diana_like = diana_like + 1
        steve_like = steve_like + 1

    # print the results depending on the score
    if diana_like >= 6:
        print( "You're most like Wonder Woman!" )
    elif steve_like >= 6:
        print( "You're most like Steve Trevor!" )
    elif barbara_like >= 6:
        print( "You're most like Barbara Minerva!")
    else:
        print( "You're most like Max Lord!")

# ask the candidate a question
activity = input("How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n")
print(wonder_woman_quiz_activity(activity))

job = input("What's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n")
print(wonder_woman_quiz_job(job))

value = input("What's more important?\n(A) Money\n(B) Love\n")
print(wonder_woman_quiz_value(value))

decade = input("What's your favorite decade?\n(A) 1910s\n(B) 1980s\n")
print(wonder_woman_quiz_decade(decade))

travel = input( "What's your favorite way to travel?\n(A) Driving\n(B) Flying\n" )
print(wonder_woman_quiz_travel(travel))

quiz_answers = [activity, job, value, decade, travel]
wonder_woman_quiz_personality(quiz_answers)