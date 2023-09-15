# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # O(min(p, q)) time complexity
        # O(min(h1, h2)) space complexity
        # Both are None
        if not p and not q:
            return True
        # Either is None
        if not p or not q:
            return False
        # Values don't match
        if p.val != q.val:
            return False
        # Compare left and right subtrees
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        