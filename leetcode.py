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