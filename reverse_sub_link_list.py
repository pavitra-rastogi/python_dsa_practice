# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):
        detached_left = None
        detached_right = None
    
        if B > 1:
            temp = A
            for _ in range(1, B - 1):
                temp = temp.next
            detached_left = temp
            start = detached_left.next
        else:
            start = A
    
        temp = A
        for _ in range(C - 1):
            temp = temp.next
        detached_right = temp.next
        end = temp
    
        prev = None
        curr = start
        while prev != end:
            fwd = curr.next
            curr.next = prev
            prev = curr
            curr = fwd
    
        start.next = detached_right
        if detached_left:
            detached_left.next = end
    
        return A if B > 1 else end
