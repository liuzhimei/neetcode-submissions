class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for i in range(len(board)):
        #     row_list = board[i]
        #     dedup_set = set()
        #     for char in row_list:
        #         if char.isdigit():
        #             if char not in dedup_set:
        #                 dedup_set.add(char)
        #             else:
        #                 return False
        # for i in range(len(board)):
        #     column_list = [row[i] for row in board]
        #     dedup_set = set()
        #     for char in column_list:
        #         if char.isdigit():
        #             if char not in dedup_set:
        #                 dedup_set.add(char)
        #             else:
        #                 return False
        # for i in range(3):
        #     for j in range(3):
        #         target_rows = board[3*i : 3*i+3]
        #         block_set = set()
        #         for row in target_rows:
        #             if row[3*j].isdigit():
        #                 if row[3*j] not in block_set:
        #                     block_set.add(row[3*j])
        #                 else:
        #                     return False
        #             if row[3*j+1].isdigit():
        #                 if row[3*j+1] not in block_set:
        #                     block_set.add(row[3*j+1])
        #                 else:
        #                     return False
        #             if row[3*j+2].isdigit():
        #                 if row[3*j+2] not in block_set:
        #                     block_set.add(row[3*j+2])
        #                 else:
        #                     return False
        # return True
        # # we assume all the numbers are in {1,2,3,4,5,6,7,8,9}

        cols = collections.defaultdict(set) # key: col idx
        rows = collections.defaultdict(set) # key: row idx
        squares = collections.defaultdict(set) # key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
