class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num = 0

        def dfs(row,col):
            if (
                row < 0 or
                row >= rows or
                col < 0 or
                col >= cols
            ):
                return
            if grid[row][col] != "1":
                return
            grid[row][col] = "0"
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row,col-1)


        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    num += 1
        return num