class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        result = dummy
        carry = 0
        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            carry, digit = divmod(sum_val, 10)
            result.next = ListNode(digit)
            result = result.next
        return dummy.next
