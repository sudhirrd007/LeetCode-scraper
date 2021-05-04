# ID : 22
# Title : Generate Parentheses
# Difficulty : MEDIUM
# Acceptance_rate : 66.0%
# Runtime : 44 ms
# Memory : 14.7 MB
# Tags : String , Backtracking
# Language : python3
# Problem_link : https://leetcode.com/problems/generate-parentheses
# Premium : 0
# Notes : -
###

    def generateParenthesis(self, n: int) -> List[str]:
        from itertools import combinations
        numbers = [val for val in range(1,n*2)]
        combs = [l for l in combinations(numbers, n)]
        ans = []
        for i in combs:
            check = 0
            index = 1
            for j in range(1, n*2+1):
                if(check < 0):
                    check = -2
                    break
                if(j in i):
                    check += 1
                else:
                    check -= 1
            if(check != -2):
                string = ""
                for j in range(1,n*2+1):
                    if(j in i):
                        string += "("
                    else:
                        string += ")"
                ans.append(string)
        return ans
