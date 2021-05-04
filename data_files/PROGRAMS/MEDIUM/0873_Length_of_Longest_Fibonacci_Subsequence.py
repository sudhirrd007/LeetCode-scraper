# ID : 873
# Title : Length of Longest Fibonacci Subsequence
# Difficulty : MEDIUM
# Acceptance_rate : 48.2%
# Runtime : 652 ms
# Memory : 14.6 MB
# Tags : Array , Dynamic Programming
# Language : python3
# Problem_link : https://leetcode.com/problems/length-of-longest-fibonacci-subsequence
# Premium : 0
# Notes : -
###

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        longest = collections.defaultdict(lambda: 2)
        ans = 0
        for k, z in enumerate(arr):
            for j in range(k):
                i = index.get(z - arr[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0
