"""
LINK: https://leetcode.com/problems/middle-of-the-linked-list/
LEVEL: EASY
TITLE: Middle of the Linked List

DESCRIPTION:
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 
Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

 
Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        len_head = head
        while len_head:
            len_head = len_head.next
            length += 1

        index = 0
        middle_node = None
        while index <= length / 2:
            if middle_node is None:
                middle_node = head
            else:
                middle_node = middle_node.next
            index += 1
        return middle_node
