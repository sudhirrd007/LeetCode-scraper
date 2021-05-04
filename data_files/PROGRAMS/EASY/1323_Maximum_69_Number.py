# ID : 1323
# Title : Maximum 69 Number
# Difficulty : EASY
# Acceptance_rate : 78.0%
# Runtime : 24 ms
# Memory : 13.9 MB
# Tags : Math
# Language : python3
# Problem_link : https://leetcode.com/problems/maximum-69-number
# Premium : 0
# Notes : -
###

    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if(num[i] == "6"):
                num = num[:i] + "9" + num[i+1:]
                break
        return num
