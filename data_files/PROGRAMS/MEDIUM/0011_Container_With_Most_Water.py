# ID : 11
# Title : Container With Most Water
# Difficulty : MEDIUM
# Acceptance_rate : 53.0%
# Runtime : 136 ms
# Memory : 14.5 MB
# Tags : Array , Two Pointers
# Language : python3
# Problem_link : https://leetcode.com/problems/container-with-most-water
# Premium : 0
# Notes : -
###

    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        ans = j*min(height[i], height[j])
        while(i<j):
            if(height[i] < height[j]):
                i += 1
            elif(height[i] > height[j]):
                j -= 1
            else:
                i += 1
                j -= 1
            ans = max(ans, (j-i)*min(height[i], height[j]))
        return ans
