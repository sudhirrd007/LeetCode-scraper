# ID : 1431
# Title : Kids With the Greatest Number of Candies
# Difficulty : EASY
# Acceptance_rate : 88.1%
# Runtime : 36 ms
# Memory : 14 MB
# Tags : Array
# Language : python3
# Problem_link : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# Premium : 0
# Notes : -
###

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mvalue = max(candies)
        ans = []
        for c in candies:
            ans.append(c+extraCandies >= mvalue)
        return ans
