# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : positon of node to deleted
    # @return the head node in the linked list
    def solve(self, A, B):
        if B==0:
            A=A.next
            return A
        temp = A
        for _ in range(B-1):
            temp = temp.next

        # Delete the Bth node
        temp.next = temp.next.next

        return A
