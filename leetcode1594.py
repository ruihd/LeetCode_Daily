class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = list()
        dp2 = list()
        for i in range(len(grid)):
            dp.append(list())
            dp2.append(list())
            for _ in range(len(grid[0])):
                dp[i].append(0)
                dp2[i].append(0)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maximum = None
                minimum = None
                if i != 0:
                    maximum = max(dp[i-1][j]*grid[i][j],dp2[i-1][j]*grid[i][j])
                    minimum = min(dp[i-1][j]*grid[i][j],dp2[i-1][j]*grid[i][j])
                if j != 0:
                    if maximum == None:
                        maximum = max(dp[i][j-1]*grid[i][j],dp2[i][j-1]*grid[i][j])
                        minimum = min(dp[i][j-1]*grid[i][j],dp2[i][j-1]*grid[i][j])
                    else:
                        if dp[i][j-1]*grid[i][j] > maximum:
                            maximum = grid[i][j]*dp[i][j-1]
                        if dp2[i][j-1]*grid[i][j] > maximum:
                            maximum = grid[i][j]*dp2[i][j-1]
                        if dp2[i][j-1]*grid[i][j] < minimum:
                            minimum = grid[i][j]*dp2[i][j-1]
                        if dp[i][j-1]*grid[i][j] < minimum:
                            minimum = grid[i][j]*dp[i][j-1]
                if maximum == None:
                    dp[i][j] = grid[i][j]
                    dp2[i][j] = grid[i][j]
                else:
                    dp[i][j] = maximum
                    dp2[i][j] = minimum
        if dp[-1][-1] < 0:
            return -1
        return dp[-1][-1]%(10**9+7)
