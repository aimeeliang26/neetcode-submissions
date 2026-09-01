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

        #initialize dummy node 
        dummy = ListNode(0, head) #ensure the head is the next pointer of dummy
        left = dummy
        right = head

        while n > 0 and right:    
            right = right.next
            n -= 1
        while right:
            right = right.next 
            left = left.next 
        
        # left is one off from being deleted 
        left.next = left.next.next 

        return dummy.next
        # dummy = ListNode(0, head) #why do we initialize it as dummy = ListNode(0, head) while the other one we initalize it was dummy = ListNode()? ANSWER: bc we want dummy points to head 

#TC: O(n)
#SC:O(1)

        