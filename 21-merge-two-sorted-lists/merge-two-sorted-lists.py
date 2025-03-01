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

        temp1 = list1
        temp2 = list2

        curr = ListNode(0)
        result = curr

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                curr.next = temp1
                temp1 = temp1.next
            else:
                curr.next = temp2
                temp2 = temp2.next
            curr = curr.next


        if temp1:
            curr.next = temp1
        else:
            curr.next = temp2

        return result.next


        