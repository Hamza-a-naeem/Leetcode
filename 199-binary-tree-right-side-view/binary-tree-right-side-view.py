# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we can just do a binary tree traversal level and store in resultant array
        #the last most element of the for loop (level)

        result = []
        queue= []
        currentlevelvals = []

        if root is None:
            return result

        queue.append(root)

        while queue:
            currentLevelSize = len(queue)

            for i in range(0, currentLevelSize):
                node = queue.pop(0)
                currentlevelvals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(currentlevelvals[currentLevelSize-1])
            currentlevelvals = []
        
        return result
        