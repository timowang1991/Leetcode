# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr1 = head
        ptr2 = ptr1.next if ptr1 != None else None
        ptr3 = ptr2.next if ptr2 != None else None

        if ptr1 != None:
            ptr1.next = None

        while ptr2 != None:
            ptr2.next = ptr1

            ptr1 = ptr2
            ptr2 = ptr3
            ptr3 = ptr3.next if ptr3 != None else None

        return ptr1