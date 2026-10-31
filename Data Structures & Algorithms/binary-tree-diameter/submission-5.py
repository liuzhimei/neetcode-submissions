# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # def depth(root):
        #     # use iterative DFS to determine the depth of a tree
        #     if not root:
        #         return 0
        #     stack = [[root, 1]]
        #     max_depth = 1
        #     while stack:
        #         node, depth = stack.pop()
        #         if node.left:
        #             stack.append([node.left, depth+1])
        #         if node.right:
        #             stack.append([node.right, depth+1])
        #         max_depth = max(max_depth, depth)
        #     return max_depth

        # use simpler recursive DFS for depth function
        def depth(root):
            if not root:
                return 0
            LeftDepth = depth(root.left) if root.left else 0
            RightDepth = depth(root.right) if root.right else 0
            return max(LeftDepth, RightDepth) + 1
        
        LeftDiameter = self.diameterOfBinaryTree(root.left) 
        RightDiameter = self.diameterOfBinaryTree(root.right) 
        LeftDepth = depth(root.left)
        RightDepth = depth(root.right)
        return max(LeftDiameter, RightDiameter, LeftDepth + RightDepth)
   