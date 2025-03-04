"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return None

        queue = []
        queue.append(root)

        while queue:
            currentLevelSize = len(queue)
            for i in range(currentLevelSize):
                node = queue.pop(0)
                if i == currentLevelSize-1:
                    node.next = None
                else:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root