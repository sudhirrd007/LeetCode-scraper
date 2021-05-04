# ID : 925
# Title : Long Pressed Name
# Difficulty : EASY
# Acceptance_rate : 37.1%
# Runtime : 48 ms
# Memory : 14 MB
# Tags : Two Pointers , String
# Language : python3
# Problem_link : https://leetcode.com/problems/long-pressed-name
# Premium : 0
# Notes : -
###

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if(name[0] != typed[0] or name[-1] != typed[-1]):
            return False
        name = [(k, len(list(grp))) for k,grp in itertools.groupby(name)]
        typed = [(k, len(list(grp))) for k,grp in itertools.groupby(typed)]
        if(len(name) != len(typed)): # because both are list of tuples of characters
            return False
        return all(k1==k2 and v1<=v2 for (k1,v1),(k2,v2) in zip (name,typed))
