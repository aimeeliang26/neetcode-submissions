class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # take the middle row, middle column, compare the first item, 
        # if target is smaller, go to the middle of the prev row, 
        # if target is larger, go to the middle of the current row 

        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows* cols - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // cols, m % cols
            if target > matrix [row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True 
        return False 