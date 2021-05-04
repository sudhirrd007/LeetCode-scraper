# ID : 26
# Title : Remove Duplicates from Sorted Array
# Difficulty : EASY
# Acceptance_rate : 46.9%
# Runtime : 80 ms
# Memory : 14.5 MB
# Tags : Array , Two Pointers
# Language : python3
# Problem_link : https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Premium : 0
# Notes : -
###

    def removeDuplicates(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        else:
            i,j = 0,1
            while(j < len(nums)):
                if(nums[i] != nums[j]):
                    nums[i+1] = nums[j]
                    i += 1
                j += 1
            return i+1
