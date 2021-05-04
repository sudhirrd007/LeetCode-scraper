# ID : 1470
# Title : Shuffle the Array
# Difficulty : EASY
# Acceptance_rate : 88.1%
# Runtime : 56 ms
# Memory : 14.5 MB
# Tags : Array
# Language : python3
# Problem_link : https://leetcode.com/problems/shuffle-the-array
# Premium : 0
# Notes : -
###

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i,j in zip(nums[:n], nums[n:]):
            ans.extend([i,j])
        return ans
