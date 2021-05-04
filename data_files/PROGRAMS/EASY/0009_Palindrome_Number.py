# ID : 9
# Title : Palindrome Number
# Difficulty : EASY
# Acceptance_rate : 50.2%
# Runtime : 80 ms
# Memory : 14.2 MB
# Tags : Math
# Language : python3
# Problem_link : https://leetcode.com/problems/palindrome-number
# Premium : 0
# Notes : -
###

    def isPalindrome(self, x: int) -> bool:

        if(x < 0):
            return False
        else:
            temp = x
            y = 0
            while(temp != 0):
                t = temp % 10
                y = y*10 + t
                temp //= 10
            if(x == y):
                return True
            else:
                return False
