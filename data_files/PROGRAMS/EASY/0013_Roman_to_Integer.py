# ID : 13
# Title : Roman to Integer
# Difficulty : EASY
# Acceptance_rate : 57.1%
# Runtime : 52 ms
# Memory : 12.7 MB
# Tags : Math , String
# Language : python3
# Problem_link : https://leetcode.com/problems/roman-to-integer
# Premium : 0
# Notes : -
###

    def romanToInt(self, s: str) -> int:

        mapping = {"I":1, "X":10, "C":100, "M":1000,
                   "V":5, "L":50, "D":500}
        count = 0
        ans = 0

        while(count < len(s)):
            if(count < len(s)-1 and ((s[count], s[count+1]) in [("I", "V"), ("X", "L"), ("C", "D")])):
                ans += mapping[s[count+1]] - mapping[s[count]]
                count += 1
            elif(count < len(s)-1 and mapping[s[count]]*10 == mapping[s[count+1]]):
                ans += mapping[s[count+1]] - mapping[s[count]]
                count += 1
            else:
                ans += mapping[s[count]]
            count += 1
        return ans
