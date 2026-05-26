class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ["." * n for i in range(n)]

        def isValidPlacement(row, col):
            for r in range(n):
                if board[r][col] == 'Q':
                    return False
                    
                if board[row][r] == 'Q': # Using 'r' as the column index here
                    return False
                    
                diag1_col = col - (row - r)
                if 0 <= diag1_col < n and board[r][diag1_col] == 'Q':
                    return False
                    
                diag2_col = col + (row - r)
                if 0 <= diag2_col < n and board[r][diag2_col] == 'Q':
                    return False

            return True

        def backtrack(row):
            if row >= n:
                res.append(board.copy())
                return
            
            for col in range(n):
                if (isValidPlacement(row, col)):
                    board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                    backtrack(row + 1)
                    board[row] = "." * n
        
        backtrack(0)
        return res


