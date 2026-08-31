# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

    #    example: [2,8,4,6]
        def rec(root:ListNode, cur: ListNode) -> ListNode:
            if not cur: # it has reached the end of the array, starts binding/pop off recursive functions
                return root

            root = rec(root, cur.next)

            if not root: #keep binding because list is reordered, hence return None
                return None #IMPORTANT this sits before if else, bc if starts return None, it keeps return None before reaching the if else below -- list is reordered 
            temp = None
            # two cases:  # even or odd
            if cur == root or root.next == cur:
                cur.next = None
            else:
                #re link
                # [2,4,6,8]
                # r. t    c
                temp = root.next #4
                root.next = cur #   2-> 8
                cur.next = temp    #2->8->4->6->8->4->6->..
            return temp #***the point: controls the reorder RANGE, gets smaller and so will eventually hit root.next == cur or root == cur to make cur.next = None, return None too since temp = None from this case onwards 
        head = rec(head, head.next)


# TC: O(n), n is the number of ele in ListNode
# WRONG ANSWER: SC: O(1), not creating new array
# CORRECT ANSWER: SC: O(n), because of call stack of n elements