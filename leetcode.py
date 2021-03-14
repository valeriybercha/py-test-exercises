# Leetcode coding solutions


# TASK 1 - Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for e in range(len(nums)):
            if i != e:
                if nums[i] + nums[e] == target:
                    return [i, e]


# TASK 2 - Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    c = 1
    for i in range(len(nums)):
        s = 0
        for e in nums[:c]:
            s += e
        res.append(s)
        c += 1
    return res


# TASK 3 - Defanging an IP Address

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]". 

def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    return "[.]".join(address.split("."))


# TASK 4 - Richest Customer Wealth

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of 
# money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest 
# customer has.

def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    res = []
    for i in accounts:
        res.append(sum(i))
    return max(res)


# TASK 5 - ids With the Greatest Number of Candies

# Given the array candies and the integer extraCandies, where candies[i] represents the number 
# of candies that the ith kid has.

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    kid_with_greatest_number = []
    for candie in candies:
        if candie + extraCandies >= max(candies):
            kid_with_greatest_number.append(True)
        else:
            kid_with_greatest_number.append(False)
    return kid_with_greatest_number
    

# TASK 6 - Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    res = []
    c = 0
    for i in range(n):
        res.append(nums[c])
        res.append(nums[c + n])
        c += 1
    return res


# TASK 7 - Number of Good Pairs

# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    c = 1
    for i in nums:
        count += nums[c:].count(i)
        c += 1
    return count


# TASK 8 - Jewels and Stones

# You're given strings jewels representing the types of stones that are jewels, and stones 
# representing the stones you have. Each character in stones is a type of stone you have. 
# You want to know how many of the stones you have are also jewels.

def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    count = 0
    for j in jewels:
        count += stones.count(j)
    return count


# TASK 9 - How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller 
# than it. That is, for each nums[i] you have to count the number of valid j's such 
# that j != i and nums[j] < nums[i].
# Return the answer in an array.

def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    c = 0
    for i in range(len(nums)):
        count = 0
        for e in nums:
            if e < nums[c]:
                count += 1
        res.append(count)
        c += 1
    return res


# TASK 10 - Number of Steps to Reduce a Number to Zero

# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    res = num
    count = 0
    while num != 0:
        if num % 2 == 0:
            res = num / 2
            count += 1
            num = res
        else:
            res = num - 1
            count += 1
            num = res
    return count


# TASK 11 - Decode XORed Array

# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] 
# XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array. You are also given an integer first, that is the first element 
# of arr, i.e. arr[0].
#Return the original array arr. It can be proved that the answer exists and is unique.

def decode(encoded, first):
    """
    :type encoded: List[int]
    :type first: int
    :rtype: List[int]
    """
    res = [first]
    for i in range(len(encoded)):
        res.append(res[i] ^ encoded[i])
    return res


# TASK 12 - Shuffle String

# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to 
# indices[i] in the shuffled string.
# Return the shuffled string.

def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    shuffle_str = ""
    for i in range(len(indices)):
        shuffle_str += s[indices.index(i)]
    return shuffle_str


# TASK 13 - Goal Parser Interpretation

# You own a Goal Parser that can interpret a string command. The command consists of an 
# alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" 
# as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted 
# strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

def interpret(command):
    """
    :type command: str
    :rtype: str
    """
    res_1 = command.replace("()", "o")
    res_2 = res_1.replace("(al)", "al")
    return res_2


# TASK 14 - Subtract the Product and Sum of Digits of an Integer

# Given an integer number n, return the difference between the product of its digits and the sum of its digits. 

def subtractProductAndSum(n):
    """
    :type n: int
    :rtype: int
    """
    str_n = [int(i) for i in str(n)]
    mult = 1 
    for i in str_n:
        mult *= i
    return mult - sum(str_n)


# TASK 15 - Check If Two String Arrays are Equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same 
# string, and false otherwise.

def arrayStringsAreEqual(word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w_1 = ""
        w_2 = ""
        for i in word1:
            w_1 += i
        for i in word2:
            w_2 += i
        return w_1 == w_2


# TASK 16 - Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating 
# order, starting with word1. If a string is longer than the other, append the additional letters 
# onto the end of the merged string.

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    res = ""
    count = 0
    if len(word1) > len(word2):
        count += len(word1)
        for i in range(count):
            if i < len(word2):
                res += word1[i]
                res += word2[i]
            else:
                res += word1[i]
    else:
        count += len(word2)
        for i in range(count):
            if i < len(word1):
                res += word1[i]
                res += word2[i]
            else:
                res += word2[i]
    return res


# TASK 17 - Count Items Matching a Rule

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, 
# and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

def countMatches(items, ruleKey, ruleValue):
    """
    :type items: List[List[str]]
    :type ruleKey: str
    :type ruleValue: str
    :rtype: int
    """
    count = 0
    ruleDict = {
        "type": 0,
        "color": 1,
        "name": 2
    }
    for i in items:
        if i[ruleDict[ruleKey]] == ruleValue:
            count += 1
    return count


# TASK 18 - Count the Number of Consistent Strings

# You are given a string allowed consisting of distinct characters and an array of strings words. A string 
# is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

def countConsistentStrings(allowed, words):
    """
    :type allowed: str
    :type words: List[str]
    :rtype: int
    """
    count = 0
    for word in words:
        res = []
        for letter in word:
            if letter in allowed:
                res.append(True)
            else:
                res.append(False)
        if False in res:
            count += 0
        else:
            count += 1
    return count


# TASK 19 - Find the Highest Altitude

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points 
# i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

def largestAltitude(gain):
    """
    :type gain: List[int]
    :rtype: int
    """
    altitudes = [0]
    biker = 0
    for i in gain:
        alt = biker + i
        altitudes.append(alt)
        biker = alt
    return max(altitudes)


# TASK 20 -  To Lower Case

# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    return str.lower()


# TASK 21 - Find Numbers with Even Number of Digits

# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            count += 1
    return count


# TASK 22 - Flipping an Image

# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the 
# resulting image.
# To flip an image horizontally means that each row of the image is reversed.

def flipAndInvertImage(image):
    """
    :type image: List[List[int]]
    :rtype: List[List[int]]
    """
    reverse_row = []
    for elem in image:
        reverse_row.append(elem[::-1])
    invert_image = []
    for item in reverse_row:
        invert = []
        for number in item:
            if number == 1:
                invert.append(0)
            else:
                invert.append(1)
        invert_image.append(invert)
    return invert_image


# TASK 23 - Maximum 69 Number

# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 
# becomes 6).

def maximum69Number(num):
    """
    :type num: int
    :rtype: int
    """
    res = ""
    res_l = []
    str_num = str(num)
    for i in range(len(str_num)):
        if str_num[i] == "9":
            res = str_num[:i] + "6" + str_num[i + 1:]
        elif str_num[i] == "6":
            res = str_num[:i] + "9" + str_num[i + 1:]
        res_l.append(int(res))
    if num > max(res_l):
        return num
    else:
        return max(res_l)