# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive DFS
        # We are maintaining the max value we have seen so far from the root

        def dfs(node, maxVal):
            if not node:
                return 0
            res = 0
            if node.val >= maxVal:
                res += 1
            res += dfs(node.left, max(maxVal, node.val))
            res += dfs(node.right, max(maxVal, node.val))
            return res
        return dfs(root, root.val)