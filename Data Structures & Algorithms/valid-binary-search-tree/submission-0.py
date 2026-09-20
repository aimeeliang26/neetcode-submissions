# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if root is null:
        #     return True  #reaches end of BST
        
        # if root.left is not null:
        #     root.left.val < root.val :
        #     return True 
        #     #meet the condition 
        # if root.right is not null:
        #     root.right.val > root.val:
        #     return True
        # isValidBST(root.left) #take the left side of node
        # isValidBSt(root.right)

        def isValid(node,left,right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return (isValid(node.left, left, node.val) and 
            isValid(node.right, node.val, right))
            
        return isValid(root, float("-inf"), float("inf"))
     

        

        

        