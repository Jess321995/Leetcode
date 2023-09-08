# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            if root == None:
                return 0
            nonlocal res
            left = helper(root.left)
            right = helper(root.right)
            temp = max(left, right) + 1
            res = max(1 + left + right, res)
            return temp
            
        helper(root)
        return res - 1