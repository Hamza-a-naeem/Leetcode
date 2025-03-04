# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """

        queue = []
        queue.append(root)
        resultAvgValues = []
        avgLevels = 0.0

        while queue:
            currentNodes = len(queue)
            for i in range(currentNodes):
                node = queue.pop(0)
                avgLevels += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                
            print(avgLevels)
            resultAvgValues.append(avgLevels/currentNodes)
            avgLevels = 0.0
        
        return resultAvgValues

        