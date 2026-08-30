# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxTotal = 0
    # if I give node a, node b  , it can cal len and chooses the longest between these two 

    # if there's a longest path between any two nodes 
    #return condition is when it's root return 0 
    #the max sum of left side and right side 
    #recursion, left or right side 
    #rule at each level: left+right len compare with maxLen
        def dfs(root):
            nonlocal maxTotal
            if not root:
                return 0
            leftCur = dfs(root.left)
            rightCur = dfs(root.right)
            total = leftCur + rightCur
            maxTotal = max(total, maxTotal)

            return 1 + max(leftCur, rightCur) #dfs returns the height, not diameter
        dfs(root)
        return maxTotal

    