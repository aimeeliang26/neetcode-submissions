# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy #so we can still have head 
        carry = 0
        while l1 or l2 or carry:
            #if l1 is null, v1 = 0; else, v1 = l1.val 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            #if l2 is null, v2 = 0, else, v2 = v2.val 
            
            val = v1 + v2 + carry #total val
            carry = val // 10 #how many whole slices 
            val = val % 10 #leftover

            cur.next = ListNode(val) # why is it not cur.next = Node(val)
            #update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next 

        