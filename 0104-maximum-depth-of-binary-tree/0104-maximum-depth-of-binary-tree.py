# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        res = 0
        stack = []
        if root:
            stack.append([root, 1])
            res += 1
        while stack:
            node, val = stack.pop()
            if node:
                if node.left:
                    stack.append([node.left, val+1])
                    res = max(res, val+1)
                if node.right:
                    stack.append([node.right, val+1])
                    res = max(res, val+1)
        return res