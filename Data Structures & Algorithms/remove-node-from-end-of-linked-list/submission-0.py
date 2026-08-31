# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     RETURN nth NODE FROM THE END!! END!!! END!!!
    #     [2,4,6,8]
    #     deltete 1 
    # r      l

    #     [2,4,6,8]

        dummy = ListNode(0, head)
        left = dummy 
        right = head 

        while n > 0:
            right = right.next 
            n -= 1
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

        