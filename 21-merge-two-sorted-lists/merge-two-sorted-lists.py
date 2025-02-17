# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not list1:
            return list2
        
        if not list2:
            return list1

        prev = ListNode(0, None)
        ans = prev

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                prev = prev.next
                list1 = list1.next
            if list1 and list2.val < list1.val:
                prev.next = list2
                prev = prev.next
                list2 = list2.next

        if list1:
            prev.next = list1
        else:
            prev.next = list2

        return ans.next