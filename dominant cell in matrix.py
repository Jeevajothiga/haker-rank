"""Given a grid of integers (a matrix), find how many cells are dominant. A dominant cell is one where the value of the cell is strictly greater than all of its neighbors. Neighbors are the cells that share a side or a corner. The matrix has 
𝑛
n rows and 
𝑚
m columns."""
def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            is_dominant = True
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[i][j] <= grid[ni][nj]:
                        is_dominant = False
                        break
            if is_dominant:
                count += 1
    
    return count
