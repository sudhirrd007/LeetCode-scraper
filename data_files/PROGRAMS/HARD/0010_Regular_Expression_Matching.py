# ID : 10
# Title : Regular Expression Matching
# Difficulty : HARD
# Acceptance_rate : 27.5%
# Runtime : N/A
# Memory : N/A
# Tags : String , Dynamic Programming , Backtracking
# Language : python3
# Problem_link : https://leetcode.com/problems/regular-expression-matching
# Premium : 0
# Notes : -
###

    def isMatch(self, s: str, p: str) -> bool:

        temp = ""
        for i in p:
            if(i == "*"):
                temp = temp[:-1]
                break
            temp += i
        if(temp != "" and len(s) != 0):
            for v1,v2 in zip(temp, s[:len(temp)]):
                if(v1 != v2 or v1 != "." ):
                    return False
            else:
                p = p[len(temp):]
                s = s[len(temp):]

        cmp = [[True if i==0 and j==0 else False for j in range(len(p)+1)] for i in range(len(s)+1)]

        for l in range(1,len(p)+1):
            if(p[l-1] == "*"):
                cmp[0][l] = cmp[0][l-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if(s[i-1] == p[j-1] or p[j-1] == "."):
                    cmp[i][j] = cmp[i-1][j-1]
                elif(p[j-1] == "*"):
                    cmp[i][j] = cmp[i][j-2]
                    if(s[i-1] == p[j-1-1] or p[j-1-1] == "."):
                        cmp[i][j] = cmp[i][j] or cmp[i-1][j]
                else:
                    cmp[i][j] = False
