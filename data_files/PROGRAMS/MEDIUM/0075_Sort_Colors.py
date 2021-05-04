# ID : 75
# Title : Sort Colors
# Difficulty : MEDIUM
# Acceptance_rate : 50.1%
# Runtime : 40 ms
# Memory : 14 MB
# Tags : Array , Two Pointers , Sort
# Language : python3
# Problem_link : https://leetcode.com/problems/sort-colors
# Premium : 0
# Notes : -
###

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = [0,0,0]
        for i in nums:
            l[i] += 1

        index = 0
        for i in range(3):
            for j in range(l[i]):
                nums[index] = i
                index += 1
