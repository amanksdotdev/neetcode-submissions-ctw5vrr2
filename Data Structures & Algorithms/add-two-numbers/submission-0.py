# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        temp = l1
        while temp:
            num1 = num1 + str(temp.val)
            temp = temp.next
        
        temp = l2
        while temp:
            num2 += str(temp.val)
            temp = temp.next

        s = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        print(s)

        dummy = ListNode()
        temp = dummy
        for c in s:
            temp.next = ListNode(int(c))
            temp = temp.next
        
        return dummy.next
        