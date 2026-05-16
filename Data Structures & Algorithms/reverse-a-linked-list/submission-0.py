# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = None
        j = head

        if head == None or head.next == None:
            return head

        while j.next != None:
            nxt = j.next
            j.next = i
            i = j
            j = nxt


        j.next = i

        return j
        

        