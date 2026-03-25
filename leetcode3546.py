class Solution:
    def split(self, row):
        prefix = list()
        prefix.append(row[0])
        for x in row[1:]:
            prefix.append(prefix[-1] + x)
        for i in range(len(prefix)-1):
            if prefix[-1] - prefix[i] == prefix[i]:
                return True
        return False
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = list()
        cols = list()

        for x in grid:
            rows.append(0)
        for x in grid[0]:
            cols.append(0)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        
        return self.split(rows) or self.split(cols)

