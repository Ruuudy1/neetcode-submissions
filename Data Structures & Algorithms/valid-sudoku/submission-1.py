class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count_row = defaultdict(set)
        count_col = defaultdict(set)
        count_square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (
                    board[r][c] in count_row[r] or 
                    board[r][c] in count_col[c] or 
                    board[r][c] in count_square[(r//3, c//3)]
                ):
                    return False
                count_row[r].add(board[r][c])
                count_col[c].add(board[r][c])
                count_square[(r//3, c//3)].add(board[r][c])
        return True 