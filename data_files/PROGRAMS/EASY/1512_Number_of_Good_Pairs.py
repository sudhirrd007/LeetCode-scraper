# ID : 1512
# Title : Number of Good Pairs
# Difficulty : EASY
# Acceptance_rate : 87.6%
# Runtime : 32 ms
# Memory : 14.2 MB
# Tags : Array , Hash Table , Math
# Language : python3
# Problem_link : https://leetcode.com/problems/number-of-good-pairs
# Premium : 0
# Notes : -
###

    def numIdenticalPairs(self, nums: List[int]) -> int:
        import collections

        ans = 0
        for i in collections.Counter(nums).values():
            if(i > 1):
                ans += (i*(i-1))/2
        return int(ans)
