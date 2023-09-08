# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def helper(root):
            if root == None:
                return 0
            nonlocal res
            left = helper(root.left)
            right = helper(root.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            temp = max(left, right) + root.val
            res = max(root.val + left + right, res)
            return temp
            
        helper(root)
        return res