# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        first,second=head,head.next
        while second:
            if first.val==second.val:
                second=second.next
            else:
                first=first.next
                first.val,second.val=second.val,first.val
                second=second.next
        first.next=None
        return head