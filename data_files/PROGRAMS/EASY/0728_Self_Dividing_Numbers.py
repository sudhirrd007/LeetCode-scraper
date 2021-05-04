# ID : 728
# Title : Self Dividing Numbers
# Difficulty : EASY
# Acceptance_rate : 75.8%
# Runtime : 56 ms
# Memory : 14.5 MB
# Tags : Math
# Language : python3
# Problem_link : https://leetcode.com/problems/self-dividing-numbers
# Premium : 0
# Notes : -
###

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        all = list(range(left, right+1))
        final = []
        for i in all:
            if(i%10 != 0):
                final.append(i)
        ans = []
        def calculate(num):
            numbers = list(str(num))
            if("0" in numbers):
                return False
            for i in numbers:
                if(num%int(i) != 0):
                    return False
            return True
        l = [1,2,3,4,5,6,7,8,9]
        for i in final:
            if(i in l):
                ans.append(i)
            elif(calculate(i)):
                ans.append(i)
        return ans
