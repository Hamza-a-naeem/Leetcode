# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def findMiddleOfLL(head):
            slow = head
            fast = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow

        def reverseLL(head):
            prev = None
            curr = head

            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            return prev

        def compareLists(head1, head2):
            while head1 and head2:
                if head1.val != head2.val:
                    return False

                head1 = head1.next
                head2 = head2.next
            return True

        middleNode = findMiddleOfLL(head)
        reversedHalfList = reverseLL(middleNode)
        result = compareLists(head, reversedHalfList)

        return result



        
