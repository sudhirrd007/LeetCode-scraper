# ID : 7
# Title : Reverse Integer
# Difficulty : EASY
# Acceptance_rate : 26.0%
# Runtime : 32 ms
# Memory : 13.8 MB
# Tags : Math
# Language : python3
# Problem_link : https://leetcode.com/problems/reverse-integer
# Premium : 0
# Notes : -
###

    def reverse(self, x: int) -> int:

        if(x >= 0):
            ans = int( str(x)[::-1] )
        else:
            ans = -int( str(x)[1:][::-1] )
        if(abs(ans) >= 2**31):
            return 0

        return ans
