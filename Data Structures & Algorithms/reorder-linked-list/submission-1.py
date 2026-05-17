# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # return if list length < 3
        if not head.next or not head.next.next:
            return
        
        mid = end = head

        # split in two
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        
        part1 = head
        part2 = mid.next
        mid.next = None

        # reverse the part2
        prev = None
        while part2:
            nextNode = part2.next
            part2.next = prev
            prev = part2
            part2 = nextNode
        
        # merge the two parts
        part2 = prev
        while part1 and part2:
            p1next = part1.next
            p2next = part2.next
            part1.next = part2
            part2.next = p1next
            part1 = p1next
            part2 = p2next




        




        