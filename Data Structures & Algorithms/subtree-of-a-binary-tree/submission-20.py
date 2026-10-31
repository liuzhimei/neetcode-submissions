# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
                return False
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False 
        if isSameTree(root, subRoot):
            return True
        
        # try BFS
        q = deque([root])
        while q:
            node = q.popleft()
            if isSameTree(node.left, subRoot) or isSameTree(node.right, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

