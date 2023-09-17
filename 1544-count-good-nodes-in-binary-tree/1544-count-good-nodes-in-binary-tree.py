# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Iterative DFS
        good = 0
        if root:
            stack = [(root, root.val)]
        while stack:
            node, maxVal = stack.pop()
            if node.val >= maxVal:
                good += 1

            if node.right:
                stack.append((node.right, max(node.val, maxVal)))
            if node.left:
                stack.append((node.left, max(node.val, maxVal)))
        return good