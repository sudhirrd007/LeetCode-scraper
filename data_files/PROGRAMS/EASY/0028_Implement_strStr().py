# ID : 28
# Title : Implement strStr()
# Difficulty : EASY
# Acceptance_rate : 35.4%
# Runtime : 28 ms
# Memory : 14.2 MB
# Tags : Two Pointers , String
# Language : python3
# Problem_link : https://leetcode.com/problems/implement-strstr
# Premium : 0
# Notes : -
###

    def strStr(self, haystack: str, needle: str) -> int:
        if(needle == ""):
            return 0
        if(len(haystack) < len(needle)):
            return -1
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            if(haystack[i:i+l] == needle):
                return i
        else:
            return -1
