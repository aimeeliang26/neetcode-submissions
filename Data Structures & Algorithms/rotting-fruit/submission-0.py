class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #if the map has a unrotten fruit that is not ajacent to any on the map
        minutes = 0
        q = deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def addCells(r,c):
            nonlocal fresh
            if(0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1):
                grid[r][c] = 2 # make it rotten 
                fresh -= 1
                q.append([r,c])
            return 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0: #early return
            return 0
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addCells(r+1, c)
                addCells(r-1, c)
                addCells(r, c+1)
                addCells(r, c-1)
            minutes += 1
        return minutes if fresh == 0 else -1
 

