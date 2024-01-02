"""
# 3. problem

LINK: https://leetcode.com/problems/reverse-linked-list/
LEVEL: EASY
TITLE: Reverse Linked List

DESCRIPTION:
Given the head of a singly linked list, reverse the list, and return the reversed list.

 
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []


Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        previous = head
        current = head.next
        previous.next = None

        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        
        return previous
