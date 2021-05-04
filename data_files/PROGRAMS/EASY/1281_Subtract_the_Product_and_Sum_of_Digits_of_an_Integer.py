# ID : 1281
# Title : Subtract the Product and Sum of Digits of an Integer
# Difficulty : EASY
# Acceptance_rate : 85.6%
# Runtime : 32 ms
# Memory : 13.9 MB
# Tags : Math
# Language : python3
# Problem_link : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
# Premium : 0
# Notes : -
###

    def subtractProductAndSum(self, n: int) -> int:

        sum, prod = 0, 1
        while n:
            n, digit = divmod(n, 10)
            sum += digit
            prod *= digit
        return prod - sum
