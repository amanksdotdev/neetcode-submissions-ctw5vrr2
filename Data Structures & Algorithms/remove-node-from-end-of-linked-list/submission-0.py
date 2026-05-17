# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        counter = head
        while counter:
            counter = counter.next
            length += 1
        
        to_remove = length - n

        if to_remove == -1:
            return head
        
        if to_remove == 0:
            return head.next

        count = 0
        temp = head
        while count < to_remove - 1:
            temp = temp.next
            count += 1
        
        temp.next = temp.next.next

        return head


        