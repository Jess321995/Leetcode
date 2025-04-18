# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative approach
    # Time complexity O(max(m,n))
    # Space complexity O(1) and output list is O(max(m, n))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ptr = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            ptr.next = ListNode((carry + v1 + v2) % 10)
            carry = (carry + v1 + v2) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            ptr = ptr.next

        return head.next