# ID : 1480
# Title : Running Sum of 1d Array
# Difficulty : EASY
# Acceptance_rate : 88.9%
# Runtime : 32 ms
# Memory : 14.4 MB
# Tags : Array
# Language : python3
# Problem_link : https://leetcode.com/problems/running-sum-of-1d-array
# Premium : 0
# Notes : -
###

    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in nums[1:]:
            ans.append(ans[-1]+i)
        return ans
