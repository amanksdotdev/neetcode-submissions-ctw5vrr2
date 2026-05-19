"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Pass 1: Interleave copies A->A'->B->B'->C->C'->D->D'
        orig = head
        while orig:
            copy = Node(orig.val)
            copy.next = orig.next
            orig.next = copy
            orig = copy.next

        # Pass 2: Set random pointers
        orig = head
        while orig:
            copy = orig.next
            if orig.random:
                copy.random = orig.random.next
            orig = orig.next.next
       

        # Pass 3: Separate the lists
        orig = head
        new_head = head.next
        while orig:
            copy = orig.next
            orig.next = orig.next.next if orig.next else None
            copy.next = copy.next.next if copy.next else None
            orig = orig.next
        
        return new_head
        
        

        

