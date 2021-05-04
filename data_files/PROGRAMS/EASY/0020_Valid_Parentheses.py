# ID : 20
# Title : Valid Parentheses
# Difficulty : EASY
# Acceptance_rate : 40.1%
# Runtime : 24 ms
# Memory : 13.8 MB
# Tags : String , Stack
# Language : python3
# Problem_link : https://leetcode.com/problems/valid-parentheses
# Premium : 0
# Notes : -
###

    def isValid(self, s: str) -> bool:

        if(len(s) % 2 != 0):
            return False
        if(s.count("(") != s.count(")") or
           s.count("]") != s.count("]") or
           s.count("{") != s.count("}")):
            return False
        stack_data = []
        open_b = ["(", "[", "{"]
        close_b = [")", "]", "}"]
        for curr in range(len(s)):
            if(curr > 0):
                if(s[curr] in close_b and s[curr-1] in open_b):
                    if(open_b.index(s[curr-1]) != close_b.index(s[curr])):
                        return False
                    else:
                        stack_data.pop()
                        continue
            if(s[curr] == "("):
                stack_data.append(")")
            elif(s[curr] == "["):
                stack_data.append("]")
            elif(s[curr] == "{"):
                stack_data.append("}")
            elif(s[curr] in close_b and len(stack_data) > 0):
                if(s[curr] != stack_data[-1]):
                    return False
                else:
