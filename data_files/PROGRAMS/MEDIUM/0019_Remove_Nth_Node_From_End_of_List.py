# ID : 19
# Title : Remove Nth Node From End of List
# Difficulty : MEDIUM
# Acceptance_rate : 36.2%
# Runtime : 36 ms
# Memory : 13.7 MB
# Tags : Linked List , Two Pointers
# Language : python3
# Problem_link : https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Premium : 0
# Notes : -
###

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        curr = head
        count = 0
        while(curr):
            curr = curr.next
            count += 1
        if(count == 1):
            return ;
        curr = head
        L = (count-n) - int(1/n)
        for v in range(L):
            curr = curr.next

        if(n >= 2):
            curr.val = curr.next.val
            curr.next = curr.next.next
        else:
            curr.next = None
        return head
