# ID : 21
# Title : Merge Two Sorted Lists
# Difficulty : EASY
# Acceptance_rate : 56.6%
# Runtime : 40 ms
# Memory : 14.4 MB
# Tags : Linked List , Recursion
# Language : python3
# Problem_link : https://leetcode.com/problems/merge-two-sorted-lists
# Premium : 0
# Notes : -
###

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lists = [l1,l2]
        def myFunc(val):
            return val[0]
        self.nodes = []
        for l in lists:
            while l:
                self.nodes.append([l.val, l])
                l = l.next

        self.nodes.sort(key=myFunc)

        for index, (val,l) in enumerate(self.nodes[:-1]):
            l.next = self.nodes[index+1][1]

        if(self.nodes):
            return self.nodes[0][1]
        else:
            return ListNode(0).next
