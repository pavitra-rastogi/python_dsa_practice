# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
        prev=None
        fwd=None
        curr=A

        while curr!=None:
            fwd=curr.next
            curr.next=prev
            prev=curr
            curr=fwd
        A=prev
        return A
