class Solution(object):
    def deleteDuplicates(self, head):
        current = head 
        while current != None and current.next != None: 
            while current.val == current.next.val: 
                current.next = current.next.next 
                if current.next == None : 
                    break 
            current = current.next 
        return head 