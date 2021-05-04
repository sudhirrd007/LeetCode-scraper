# ID : 14
# Title : Longest Common Prefix
# Difficulty : EASY
# Acceptance_rate : 36.3%
# Runtime : 28 ms
# Memory : 12.8 MB
# Tags : String
# Language : python3
# Problem_link : https://leetcode.com/problems/longest-common-prefix
# Premium : 0
# Notes : -
###

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        strs.sort()
        ans = strs[0]
        for i in strs:
            if(ans == ""):
                return ""
            else:
                for j in range(len(ans)):
                    if(ans[j] != i[j]):
                        ans = ans[:j]
                        break
        return ans
