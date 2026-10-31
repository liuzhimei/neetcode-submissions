# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive method
        # base case
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 1
        # induction
        LeftDepth = 1 + self.maxDepth(root.left)
        RightDepth = 1 + self.maxDepth(root.right)
        return max(LeftDepth, RightDepth)