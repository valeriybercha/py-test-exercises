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
