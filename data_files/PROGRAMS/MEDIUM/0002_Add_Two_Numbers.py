# ID : 2
# Title : Add Two Numbers
# Difficulty : MEDIUM
# Acceptance_rate : 35.9%
# Runtime : 68 ms
# Memory : 13.8 MB
# Tags : Linked List , Math , Recursion
# Language : python3
# Problem_link : https://leetcode.com/problems/add-two-numbers
# Premium : 0
# Notes : -
###

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ans = t = ListNode()
        carry = 0
        while(l1 or l2):
            s = 0
            if(l1):
                s += l1.val
                l1 = l1.next
            if(l2):
                s += l2.val
                l2 = l2.next
            s += carry
            t.next = ListNode(s%10)
            t = t.next
            carry = s//10

        if(carry):
            t.next = ListNode(carry)

        return ans.next
