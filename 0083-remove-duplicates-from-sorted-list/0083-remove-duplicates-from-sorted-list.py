# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        first = head
        
        if head == None or head.next == None:
            return head
    
        temp = first.next

       

        while not temp == None:
            if first.val == temp.val:
                temp = temp.next
                first.next.next = None
                first.next = temp
            else:
                temp = temp.next
                first = first.next

        return head

        
        