class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []
        
        queue = []
        result = []
        currentLevelvals = []
        iterator = 1
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

            if iterator % 2 == 0:
                currentLevelvals = currentLevelvals[::-1]
            iterator += 1
            result.append(currentLevelvals)
            currentLevelvals = []
        
        return result