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

print(numIdenticalPairs([1,1,1,1]))