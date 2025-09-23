# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue= []
        currentlevelvals = []
        flag = True

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
            
            if flag == False:
                reversed_ = currentlevelvals[::-1]
                flag = True
                result.append(reversed_)
            else:
                result.append(currentlevelvals)
                flag = False

            currentlevelvals = []
        
        return result