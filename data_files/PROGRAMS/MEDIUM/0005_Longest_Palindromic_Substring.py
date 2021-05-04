# ID : 5
# Title : Longest Palindromic Substring
# Difficulty : MEDIUM
# Acceptance_rate : 30.7%
# Runtime : 8324 ms
# Memory : 14.1 MB
# Tags : String , Dynamic Programming
# Language : python3
# Problem_link : https://leetcode.com/problems/longest-palindromic-substring
# Premium : 0
# Notes : -
###

    def longestPalindrome(self, s: str) -> str:
        reverse = list(s).__reversed__()
        reverse = "".join(reverse)
        ans = []
        for main_index in range(s.__len__()):
            reverse_index = 0
            string_index = main_index
            flag = True
            while(flag):
                start_flag = None
                while(reverse_index <= s.__len__() - main_index - 1):
                    if(s[string_index] == reverse[reverse_index]):
                        if(start_flag is None):
                            start_flag = string_index
                        string_index += 1
                    else:
                        string_index = main_index
                        reverse_index += 1
                        flag = True
                        break
                    reverse_index += 1
                else:
                    flag = False
                    ans.append([start_flag,string_index-1])
        temp_ans = [(j-i+1) for i,j in ans]
        if(temp_ans != []):
            temp = ans[temp_ans.index(max(temp_ans))]
            temp = s[temp[0] : temp[1]+1]
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        s = reverse
        reverse = list(s).__reversed__()
        reverse = "".join(reverse)
        ans_1 = []
