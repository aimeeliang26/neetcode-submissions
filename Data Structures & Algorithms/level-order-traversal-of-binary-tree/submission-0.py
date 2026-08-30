# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # flag that shows whether its the same level
        #  queue, first in, first out !! Breadth first search 

        q = collections.deque()
        q.append(root)
        res = [] #stores final result

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

        
        # use stack, the order matters 

        # stack.append(node.val)
        # stack.pop()
        # stack.append(node.left, node.right)
        # curr = 2
        # stack[expanding] = 3, 4, 5

        
        # if(stack.isEmpty)
        #     res.append(curr)
        #     curr.pop()