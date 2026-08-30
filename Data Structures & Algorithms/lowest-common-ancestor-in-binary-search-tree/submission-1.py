# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #cases of LCA 

        #easiest case: 
        # 1. when p, q in the same side of the tree, 
        # and root.left == p, root.right == q, they are on the same level 

        # 2. on the same level, on diff branch: root.left == p, root.right == q
        # 3. on the diff level, same branch, root == p || root == q, root.left == p || root.right == p || root.left == q || root.right == q
        #     if i find 1 node, the other one is not found, the node itself will be the ancestor 

        # 4. when they backtracks to a node they share 

        # 1. p,q both < node.val, search left subtree 
        # 2. p,q both > node.val, search right subtree 
        # 3. p > node.val && q < node.val, whenever node == p || node == q,
        # if not root:
        #     returm 
        # if(root == p || root == q)
        #     return 
        # if p > node.val, search right sub tree 
        #     LCA(root.right)
        # if q
        #     LCA(root.left)

        #     LCA(root.right)

        if not root or not p or not q:
            return None 
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root