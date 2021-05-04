# ID : 1672
# Title : Richest Customer Wealth
# Difficulty : EASY
# Acceptance_rate : 88.1%
# Runtime : 48 ms
# Memory : 14.4 MB
# Tags : Array
# Language : python3
# Problem_link : https://leetcode.com/problems/richest-customer-wealth
# Premium : 0
# Notes : -
###

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            if(sum(i) > ans):
                ans = sum(i)
        return ans
