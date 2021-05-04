# ID : 23
# Title : Merge k Sorted Lists
# Difficulty : HARD
# Acceptance_rate : 43.2%
# Runtime : 88 ms
# Memory : 17.9 MB
# Tags : Linked List , Divide and Conquer , Heap
# Language : python3
# Problem_link : https://leetcode.com/problems/merge-k-sorted-lists
# Premium : 0
# Notes : -
###

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
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
