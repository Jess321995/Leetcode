# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ptr = ListNode(0)
        carry = 0
        while l1 and l2:
            ptr.next = ListNode((carry + l1.val + l2.val) % 10)
            carry = (carry + l1.val + l2.val) // 10
            l1, l2, ptr = l1.next, l2.next, ptr.next
            
        while l1:
            ptr.next = ListNode((carry + l1.val) % 10)
            carry = (carry + l1.val) // 10
            l1, ptr = l1.next, ptr.next

        while l2:
            ptr.next = ListNode((carry + l2.val) % 10)
            carry = (carry + l2.val) // 10
            l2, ptr = l2.next, ptr.next

        if carry != 0:
            ptr.next = ListNode(carry)

        return head.next