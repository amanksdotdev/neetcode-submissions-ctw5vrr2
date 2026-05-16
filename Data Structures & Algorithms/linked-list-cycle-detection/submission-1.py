# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single_jumper = head
        double_jumper = head

        while double_jumper and double_jumper.next and single_jumper:
            single_jumper = single_jumper.next
            double_jumper = double_jumper.next.next

            if single_jumper is double_jumper:
                return True
            
        
        return False