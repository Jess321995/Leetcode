"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        og_p, og_q = p, q
        while p != q:
            p = p.parent if p else og_q
            q = q.parent if q else og_p
        return p