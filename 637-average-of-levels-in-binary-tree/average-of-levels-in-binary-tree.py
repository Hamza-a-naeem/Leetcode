# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []
        result = []
        currentLevelVals = []

        queue.append(root)
        result = root.val

        while queue:
            currentLevelSize = len(queue)
            levelSum = 0

            for i in range(currentLevelSize):
                node = queue.pop(0)
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            currentLevelVals.append(levelSum/currentLevelSize)

        return currentLevelVals