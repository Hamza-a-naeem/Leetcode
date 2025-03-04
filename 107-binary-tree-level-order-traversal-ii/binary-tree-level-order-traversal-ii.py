class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []
        
        queue = []
        result = []
        currentLevelvals = []

        queue.append(root)

        while queue:
            currentLevelSize = len(queue)

            for i in range(currentLevelSize):
                node = queue.pop(0)
                currentLevelvals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(currentLevelvals)
            currentLevelvals = []
        
        result = result[::-1]
        return result