# ID : 509
# Title : Fibonacci Number
# Difficulty : EASY
# Acceptance_rate : 67.9%
# Runtime : 32 ms
# Memory : 14.1 MB
# Tags : Array
# Language : python3
# Problem_link : https://leetcode.com/problems/fibonacci-number
# Premium : 0
# Notes : -
###

    def fib(self, n: int) -> int:
        i = 0
        j = 1
        for _ in range(int((n+2)/2) - 1):
            i = i + j
            j = i + j
        ans = j if(n%2!=0) else i
        return ans
