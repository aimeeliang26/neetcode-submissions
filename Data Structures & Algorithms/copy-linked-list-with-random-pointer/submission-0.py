"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#TOPIC: HASHTABLE AND LINKEDLIST
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #two passes
        # 1st pass: we do deep copy to a hashmap, old maps to hashmap
        # 2nd pass: we set the pointers

        oldMap = {None : None} #account for when cur.next is null : null points to a null
        cur = head
        while cur:
            # hashmap will store the node 
            oldMap[cur] = Node(cur.val)
            cur = cur.next
        
        #second pass 
        cur = head
        while cur:
            oldMap[cur].next = oldMap[cur.next] # does oldMap[cur].next means a node's next, and oldMap[cur.next] is the actual node oldMap[cur].next should be pointing to? if thats the case, shouldnt oldMap[cur].next is actually a pointer, not a node? 
            oldMap[cur].random = oldMap[cur.random]
            cur = cur.next

        return oldMap[head]

#intuition: it is a good method becuase we are using hashmap's property that we can access the value by key, the key is every node in the original 
    

       
        



        