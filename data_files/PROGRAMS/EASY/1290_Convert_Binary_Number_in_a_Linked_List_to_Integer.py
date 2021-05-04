# ID : 1290
# Title : Convert Binary Number in a Linked List to Integer
# Difficulty : EASY
# Acceptance_rate : 81.7%
# Runtime : 28 ms
# Memory : 12.7 MB
# Tags : Linked List , Bit Manipulation
# Language : python3
# Problem_link : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
# Premium : 0
# Notes : -
###

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        sum = []
        temp = head
        while(temp):
            sum.append(temp.val)
            temp = temp.next

        ans = 0
        for count,i in enumerate(sum[::-1]):
            ans += 2**count * i

        return ans
