# ID : 1
# Title : Two Sum
# Difficulty : EASY
# Acceptance_rate : 46.8%
# Runtime : 6948 ms
# Memory : 12.8 MB
# Tags : Array , Hash Table
# Language : python
# Problem_link : https://leetcode.com/problems/two-sum
# Premium : 0
# Notes : -
###

    def twoSum(self, nums, target):
        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if(i<j):
                    if((nums[i] +nums[j]) == target ):
                        return [i,j]

