# ID : 12
# Title : Integer to Roman
# Difficulty : MEDIUM
# Acceptance_rate : 57.2%
# Runtime : 40 ms
# Memory : 12.8 MB
# Tags : Math , String
# Language : python3
# Problem_link : https://leetcode.com/problems/integer-to-roman
# Premium : 0
# Notes : -
###

    def intToRoman(self, num: int) -> str:

        mapping = {1:"I", 5:"V",




        num = str(num)
        length = len(num)
        ans = ""

        for i in num:
            if(int(i)%5 == 0):
                if(int(i) !=0):
                    ans += mapping[length*5]
            elif(int(i)%5 == 4):
                if(int(i) == 4):
                    ans += mapping[length*1] + mapping[length*5]
                else:
                    ans += mapping[length] + mapping[length+1]
            else:
                if(int(i) in [1,2,3]):
                    ans += mapping[length]*int(i)
                else:
                    ans += mapping[length*5] + mapping[length]*(int(i)%5)
            length -= 1

        return ans
