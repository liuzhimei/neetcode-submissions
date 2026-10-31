# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive method
        # base case
        if not root:
            return None
        if root and not root.left and not root.right: # at leaf node
            return root
        NewRoot = root
        if root.left or root.right:
            OldLeft = root.left
            OldRight = root.right

            root.left = self.invertTree(OldRight)
            root.right = self.invertTree(OldLeft)
        
        return NewRoot