# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        first,second=head,head.next
        while second:
            first=first.next
            second=second.next
            if second:
                second=second.next
        return first