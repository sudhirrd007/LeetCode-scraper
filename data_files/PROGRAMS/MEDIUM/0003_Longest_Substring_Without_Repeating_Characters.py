# ID : 3
# Title : Longest Substring Without Repeating Characters
# Difficulty : MEDIUM
# Acceptance_rate : 31.6%
# Runtime : 1888 ms
# Memory : 14 MB
# Tags : Hash Table , Two Pointers , String , Sliding Window
# Language : python3
# Problem_link : https://leetcode.com/problems/longest-substring-without-repeating-characters
# Premium : 0
# Notes : -
###

    def lengthOfLongestSubstring(self, s):
        ans = dict()
        for n in range(s.__len__()):
            temp = ""
            temp_dict = []
            for val in range(n, s.__len__()):
                if(s[val] in temp_dict):
                    ans[temp] = temp.__len__()
                    break
                temp += s[val]
                temp_dict.append(s[val])
            else:
                ans[temp] = temp.__len__()
        ans = sorted(ans.items(), key=lambda num:num[1], reverse=True)

        if(bool(ans)):
            return ans[0][1]
        elif(s.__len__() > 0):
            return 1
        else:
            return 0
