class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first flatten 2D matrix into 1D
        flattened = []
        for i in range(len(matrix)):
            flattened += matrix[i]
        # use binary search and two pointer
        l, r = 0, len(flattened) - 1
        while l <= r:
            m = int((l+r) / 2)
            if flattened[m] == target:
                return True
            elif flattened[m] > target:
                r = m-1
            else:
                l = m+1
        return False
