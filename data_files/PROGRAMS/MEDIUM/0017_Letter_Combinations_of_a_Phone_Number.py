# ID : 17
# Title : Letter Combinations of a Phone Number
# Difficulty : MEDIUM
# Acceptance_rate : 50.1%
# Runtime : 28 ms
# Memory : 12.6 MB
# Tags : String , Backtracking , Depth-first Search , Recursion
# Language : python3
# Problem_link : https://leetcode.com/problems/letter-combinations-of-a-phone-number
# Premium : 0
# Notes : -
###

    def letterCombinations(self, digits: str) -> List[str]:

        d = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'],


        digits = list(map(int,digits))
        if(len(digits) == 0):
            return []
        if(len(digits) == 1):
            return d[digits[0]]
        ans = d[digits[0]] + []

        for i in range(1,len(digits)):
            L = len(ans)
            for j in range(L):
                for k in d[digits[i]]:
                    ans.append(ans[j]+k)
            ans = ans[L:]
        return ans
