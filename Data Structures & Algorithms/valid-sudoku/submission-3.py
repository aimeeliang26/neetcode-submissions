class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
    #     row - 1-9 
    #     col - 1-9 
    #     each of the nine 3x3 must contain 1-9 
    #     j  
    # i   1 2 3
    #     4 5 6
    #     7 8 9
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True
        
# time complexity: m elements in row, m elements in col
# O(m^2) since you are iterating through element on a mxm board

# space complexity: 3 hashsets, m*m, m*m, m*m, 3*m^2 = O(m^2)


