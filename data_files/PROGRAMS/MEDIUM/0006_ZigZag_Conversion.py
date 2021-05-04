# ID : 6
# Title : ZigZag Conversion
# Difficulty : MEDIUM
# Acceptance_rate : 38.4%
# Runtime : 1128 ms
# Memory : 15 MB
# Tags : String
# Language : python3
# Problem_link : https://leetcode.com/problems/zigzag-conversion
# Premium : 0
# Notes : -
###

    def convert(self, s: str, numRows: int) -> str:
        length = s.__len__()
        li = [[] for _ in range(numRows)]
        count = 0
        while (count < length):
            for i in range(numRows):
                if (count < length):
                    li[i].append(s[count])
                    count += 1
                else:
                    break
            for j in range(numRows - 2, 0, -1):
                if (count < length):
                    li[j].append(s[count])
                    count += 1
                    temp_len = li[0].__len__()
                    for k in range(numRows):
                        if (li[k].__len__() is temp_len):
                            li[k].append(" ")
                else:
                    break
        ans = [val for temp in li for val in temp if val is not " "]
        ans = "".join(ans)
        return ans
