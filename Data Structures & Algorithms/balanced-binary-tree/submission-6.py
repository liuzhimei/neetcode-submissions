# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # ----- Method 1: nested recursive DFS, T: O(n^2), not optimal -----
        # First use recursive DFS to construct the depth function
        def depth(root):
            if not root:
                return 0
            LeftDepth = depth(root.left)
            RightDepth = depth(root.right)
            return max(LeftDepth, RightDepth) + 1
        
        if not root:
            return True
        # if root and not root.left and not root.right:
        #     return True
        # if root.left and not root.right:
        #     if depth(root.left) == 1:
        #         return True
        #     else:
        #         return False
        # if root.right and not root.left:
        #     if depth(root.right) == 1:
        #         return True
        #     else:
        #         return False
        # if root.left and root.right:
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        if abs(depth(root.left) - depth(root.right)) <= 1:
            return True
        else:
            return False
        
        # # ------- Method 2: nested recursive function, DFS applied only once -------
        # # since we run recursive algorithm once, T: O(n)
        # def dfs(root):
        #     if not root:
        #         return [True, 0] # [balanced, height]
        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        #     return [balanced, max(left[1], right[1]) + 1]
        # return dfs(root)[0]




