# ID : 4
# Title : Median of Two Sorted Arrays
# Difficulty : HARD
# Acceptance_rate : 31.6%
# Runtime : 104 ms
# Memory : 13.8 MB
# Tags : Array , Binary Search , Divide and Conquer
# Language : python3
# Problem_link : https://leetcode.com/problems/median-of-two-sorted-arrays
# Premium : 0
# Notes : -
###

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted((nums1 + nums2))
        length = arr.__len__() - 1
        ans = float(( arr[int(length/2)] + arr[int((length+1)/2)] ) / 2)
        return ans
