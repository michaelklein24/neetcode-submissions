class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set() #(row, col)
        boardRowCount, boardColCount = len(board), len(board[0])
        found = False

        def search(row: int, col: int, wordI: int) -> bool:
            

            if wordI == len(word) - 1 and board[row][col] == word[wordI]:
                return True
            
            if board[row][col] != word[wordI]:
                return False
            
            visited.add((row, col))

            up, down, left, right = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)

            moveUp = row > 0 and up not in visited
            moveDown = row < boardRowCount - 1 and down not in visited
            moveLeft = col > 0 and left not in visited
            moveRight = col < boardColCount - 1 and right not in visited

            f = False

            if moveUp and not f:
                f = search(row - 1, col, wordI + 1)
            if moveDown and not f:
                f = search(row + 1, col, wordI + 1)
            if moveLeft and not f:
                f = search(row, col - 1, wordI + 1)
            if moveRight and not f:
                f = search(row, col + 1, wordI + 1)

            visited.remove((row, col))            
            return f

        for row in range(boardRowCount):
            for col in range(boardColCount):
                if board[row][col] == word[0]:
                    found = search(row, col, 0)
                if found:
                    return True

        return found

"""
["A","B","C","E"]
["S","F","C","S"]
["A","D","E","E"]
"""
