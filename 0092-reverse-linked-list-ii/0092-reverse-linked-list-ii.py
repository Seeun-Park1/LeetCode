class Solution(object):
    def reverseBetween(self, head, left, right):
        cur = head 
        for i in range(1, left): 
            cur = cur.next

        stack = []
        leftPtr = rightPtr = cur 

        for i in range(left, right+1):
            stack.append(rightPtr.val)
            rightPtr = rightPtr.next
        
        for i in range(left, right+1): 
            leftPtr.val = stack.pop()
            leftPtr = leftPtr.next

        return head