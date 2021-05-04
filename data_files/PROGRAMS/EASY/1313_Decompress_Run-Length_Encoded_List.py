# ID : 1313
# Title : Decompress Run-Length Encoded List
# Difficulty : EASY
# Acceptance_rate : 85.4%
# Runtime : 68 ms
# Memory : 13 MB
# Tags : Array
# Language : python3
# Problem_link : https://leetcode.com/problems/decompress-run-length-encoded-list
# Premium : 0
# Notes : -
###

    def decompressRLElist(self, nums: List[int]) -> List[int]:

        ans = []
        for i in range(len(nums))[::2]:
            ans.extend(nums[i]*[nums[i+1]])

        return ans
