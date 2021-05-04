# ID : 15
# Title : 3Sum
# Difficulty : MEDIUM
# Acceptance_rate : 28.4%
# Runtime : 724 ms
# Memory : 16.2 MB
# Tags : Array , Two Pointers
# Language : python3
# Problem_link : https://leetcode.com/problems/3sum
# Premium : 0
# Notes : -
###

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if(nums[i] > 0):
                break

            if(nums[i] + 2*nums[-1] < 0):
                continue
            if(i>0 and nums[i]==nums[i-1]):
                continue
            start, end = i+1, len(nums)-1
            while(start < end):
                sum = nums[i] + nums[start] + nums[end]
                if(sum < 0):
                    start += 1
                elif(sum > 0):
                    end -= 1
                else:
                    ans.append([nums[i], nums[start], nums[end]])
                    while(start < end and nums[start] == nums[start+1]):
                        start += 1
                    while(start < end and nums[end] ==  nums[end-1]):
                        end -= 1
                    start += 1
                    end -= 1
        return ans
