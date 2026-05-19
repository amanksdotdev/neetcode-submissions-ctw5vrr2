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

        old_to_new = dict()
        temp = head
        
        while temp:
            node = Node(temp.val)
            old_to_new[temp] = node
            temp = temp.next
        
        temp = head
        while temp:
            new_node = old_to_new[temp]
            new_node.next = old_to_new[temp.next] if temp.next else None
            new_node.random = old_to_new[temp.random] if temp.random else None
            temp = temp.next
        
        return old_to_new[head]
        

        

