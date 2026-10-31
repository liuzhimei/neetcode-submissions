class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_list = board[i]
            dedup_set = set()
            for char in row_list:
                if char.isdigit():
                    if char not in dedup_set:
                        dedup_set.add(char)
                    else:
                        return False
        for i in range(len(board)):
            column_list = [row[i] for row in board]
            dedup_set = set()
            for char in column_list:
                if char.isdigit():
                    if char not in dedup_set:
                        dedup_set.add(char)
                    else:
                        return False
        for i in range(3):
            for j in range(3):
                target_rows = board[3*i : 3*i+3]
                block_set = set()
                for row in target_rows:
                    if row[3*j].isdigit():
                        if row[3*j] not in block_set:
                            block_set.add(row[3*j])
                        else:
                            return False
                    if row[3*j+1].isdigit():
                        if row[3*j+1] not in block_set:
                            block_set.add(row[3*j+1])
                        else:
                            return False
                    if row[3*j+2].isdigit():
                        if row[3*j+2] not in block_set:
                            block_set.add(row[3*j+2])
                        else:
                            return False

        return True