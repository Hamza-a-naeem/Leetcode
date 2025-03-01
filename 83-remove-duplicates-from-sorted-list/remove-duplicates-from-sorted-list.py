# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp = head
        
        while temp and temp.next:
            nextNode = temp.next
            while nextNode and nextNode.val == temp.val:
                nextNode = nextNode.next
            temp.next = nextNode
            temp = temp.next

        return head
                


        