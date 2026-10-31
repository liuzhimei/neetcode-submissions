# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # -------- recursive DFS, T: O(n), S: O(n) --------
        # # base case
        # if not root:
        #     return 0
        # if root and not root.left and not root.right:
        #     return 1
        # # induction
        # LeftDepth = 1 + self.maxDepth(root.left)
        # RightDepth = 1 + self.maxDepth(root.right)
        # return max(LeftDepth, RightDepth)

        # # ----- iterative BFS ------
        # if not root:
        #     return 0
        # level = 0
        # q = deque([root])
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # --------- iterative DFS --------
        if not root:
            return 0
        stack = [[root, 1]] # [node, depth]
        result = 1
        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
            result = max(result, depth)
        return result
        
