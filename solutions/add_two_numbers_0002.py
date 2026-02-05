try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
        ) -> ListNode | None:
        """Add two numbers represented by linked lists."""
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next
