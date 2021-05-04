# ID : 8
# Title : String to Integer (atoi)
# Difficulty : MEDIUM
# Acceptance_rate : 15.8%
# Runtime : 40 ms
# Memory : 13.9 MB
# Tags : Math , String
# Language : python3
# Problem_link : https://leetcode.com/problems/string-to-integer-atoi
# Premium : 0
# Notes : -
###

    def myAtoi(self, str: str) -> int:
        str = str.strip()
        temp = [val for val in "0123456789"]
        negative = False
        if(str):
            if(str[0] == "-"):
                negative = True
                str = str[1:]
            elif(str[0] == "+"):
                str = str[1:]
        else:
            return 0
        ans = 0
        for c in str:
            if c not in temp:
                break
            ans = ans*10 + int(c)
        if(negative):
            ans *= -1
        ans = max( min(ans,2**31-1), -2**31)
        return ans
