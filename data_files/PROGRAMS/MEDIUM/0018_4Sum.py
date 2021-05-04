# ID : 18
# Title : 4Sum
# Difficulty : MEDIUM
# Acceptance_rate : 35.2%
# Runtime : 72 ms
# Memory : 12.7 MB
# Tags : Array , Hash Table , Two Pointers
# Language : python3
# Problem_link : https://leetcode.com/problems/4sum
# Premium : 0
# Notes : -
###

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        L = len(nums)
        ans = []
        if(L > 2):
            last = nums[-1]
        else:
            return []
        for i in range(L-3):
            if(i>0 and nums[i]==nums[i-1] or nums[i] + 3*last < target):
                continue
            if(4*nums[i] > target):
                break
            for j in range(i+1, L-2):
                if(j>i+1 and nums[j] == nums[j-1] or nums[i]+nums[j]+2*last < target):
                    continue
                if(nums[i]+3*nums[j] > target):
                    break
                temp = nums[i] + nums[j]
                start,end = j+1, L-1

                while(start < end):
                    t = temp + nums[start] + nums[end]
                    if(t < target):
                        start += 1
                    elif(t > target):
                        end -= 1
                    else:
                        if([nums[i], nums[j], nums[end], t] not in ans):
                            ans.append([nums[i], nums[j], nums[start], nums[end]])
                        while(start < end and nums[start]==nums[start+1]):
                            start += 1
                        start += 1
                        end -= 1
        return ans
