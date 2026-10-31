# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case
        if not root:
            return True

        def MaxMin(root):
            # assume root is not None
            if root and not root.left and not root.right:
                return [root.val, root.val, True] # [min, max, bool]
            if root.left and root.right:
                left, right = MaxMin(root.left), MaxMin(root.right)
                leftMin, leftMax = left[0], left[1]
                rightMin, rightMax = right[0], right[1]
                validBST = (leftMax < root.val) and (root.val < rightMin) and left[2] and right[2]
                return [leftMin, rightMax, validBST]
            if root.left and not root.right:
                left = MaxMin(root.left)
                leftMin, leftMax = left[0], left[1]
                validBST = (left[2] and leftMax < root.val)
                return [leftMin, root.val, validBST]
            if root.right and not root.left:
                right = MaxMin(root.right)
                rightMin, rightMax = right[0], right[1]
                validBST = (right[2] and root.val < rightMin)
                return[root.val, rightMax, validBST]
            
        return MaxMin(root)[2]

                