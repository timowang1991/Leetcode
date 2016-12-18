# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddTail = None

        evenHead = None
        evenTail = None

        try:
            oddTail = head
            evenHead = head.next
            evenTail = evenHead
        except Exception as e:
            return head

        while True:
            try:
                nextOdd = evenTail.next
                nextEven = nextOdd.next if nextOdd != None else None

                nextOdd.next = evenHead
                oddTail.next = nextOdd
                oddTail = nextOdd

                evenTail.next = nextEven
                evenTail = nextEven

            except Exception as e:
                break;

        return head