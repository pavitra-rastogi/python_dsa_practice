# Given a sorted linked list, delete all duplicates such that each element appears only once.
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
        if not A:
            
            return None
        
        temp = A
        while temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next   # skip duplicate
            else:
                temp = temp.next             # move forward if distinct
        return A
