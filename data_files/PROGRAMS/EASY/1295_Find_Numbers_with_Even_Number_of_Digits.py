# ID : 1295
# Title : Find Numbers with Even Number of Digits
# Difficulty : EASY
# Acceptance_rate : 78.6%
# Runtime : 52 ms
# Memory : 12.9 MB
# Tags : Array
# Language : python3
# Problem_link : https://leetcode.com/problems/find-numbers-with-even-number-of-digits
# Premium : 0
# Notes : -
###

    def findNumbers(self, nums: List[int]) -> int:

        return len([1 for i in nums if len(str(i))%2==0])
