# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
# A: head
# B: integer to be inserted
# C: derired position of B in LL
class Solution:
    def solve(self, A, B, C):
        nn = ListNode(B)

        if A is None:
            return nn

        # Case 1: insert at head
        if C == 0:
            nn.next = A
            return nn

        temp = A

        # Move temp to (C-1)-th node, or stop early if we hit tail
        for _ in range(C-1):
            if temp.next is None:   # reached end before C-1
                break
            temp = temp.next

        # Insert node
        nn.next = temp.next
        temp.next = nn

        return A
