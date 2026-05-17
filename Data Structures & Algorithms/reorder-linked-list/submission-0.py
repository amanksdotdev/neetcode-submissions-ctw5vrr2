# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        part2 = mid.next
        mid.next = None

        # reverse p2
        prev = None
        while part2 and part2.next:
            nextNode = part2.next
            part2.next = prev
            prev = part2
            part2 = nextNode
        part2.next = prev

        part1 = head

        # merge
        while part1 and part2:
            p1next = part1.next
            p2next = part2.next
            part1.next = part2
            part2.next = p1next
            part1 = p1next
            part2 = p2next




        