# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Insert duplicate nodes in between
        temp = head
        while temp:
            nn = RandomListNode(temp.label)   
            nn.next = temp.next
            temp.next = nn
            temp = nn.next

        # Step 2: Replicate the random pointers
        temp = head
        while temp:
            if temp.random:                   
                temp.next.random = temp.random.next
            temp = temp.next.next             

        # Step 3: Extract original and duplicate linked lists
        temp = head
        dup_head = head.next
        dtemp = dup_head
        while temp:
            temp.next = dtemp.next
            if dtemp.next:
                dtemp.next = dtemp.next.next
            temp = temp.next
            dtemp = dtemp.next

        return dup_head
