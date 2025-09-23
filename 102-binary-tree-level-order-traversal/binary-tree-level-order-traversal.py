# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we need to store the next levels in queue and also print them
        
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
                
            result.append(currentlevelvals)
            currentlevelvals = []
        
        return result
        