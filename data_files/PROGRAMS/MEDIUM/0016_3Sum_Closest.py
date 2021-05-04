# ID : 16
# Title : 3Sum Closest
# Difficulty : MEDIUM
# Acceptance_rate : 46.4%
# Runtime : 52 ms
# Memory : 12.9 MB
# Tags : Array , Two Pointers
# Language : python3
# Problem_link : https://leetcode.com/problems/3sum-closest
# Premium : 0
# Notes : -
###

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans = []
        L = len(nums)
        for index,i in enumerate(nums[:-2]):
            start, end = index+1, L-1
            if(i + nums[start] + nums[start+1] > target):
                ans.append(i + nums[start] + nums[start+1])
            elif(i + nums[end-1] + nums[end] < target):
                ans.append(i + nums[end-1] + nums[end])
            else:
                while(start < end):
                    ans.append(i + nums[start] + nums[end])
                    if(i + nums[start] + nums[end] < target):
                        start += 1
                    elif(i + nums[start] + nums[end] > target):
                        end -= 1
                    else:
                        return target
        ans.sort(key=lambda x:abs(x-target))
        return ans[0]
