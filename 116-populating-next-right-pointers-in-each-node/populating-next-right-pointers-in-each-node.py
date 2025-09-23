"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #i just need to know when the level ends, when it does, push null, otherwise push next in queue node

        queue= []
        currentlevelvals = []

        if root is None:
            return None

        queue.append(root)

        while queue:
            currentLevelSize = len(queue)
            print(currentLevelSize) 

            for i in range(0, currentLevelSize):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == currentLevelSize - 1:
                    node.next = None
                else:
                    node.next = queue[0]
        
        return root
        