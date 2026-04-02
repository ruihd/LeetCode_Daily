class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        dp = list()
        for i in range(len(coins)):
            dp.append(list())
            for _ in range(len(coins[0])):
                dp[i].append([0,0,0])
        for i in range(len(coins)):
            for j in range(len(coins[0])):
                if i != 0:
                    if j != 0:
                        dp[i][j][0] = max(dp[i-1][j][0] + coins[i][j],dp[i][j-1][0] + coins[i][j])
                        for k in range(1,3):
                            dp[i][j][k] = max(dp[i-1][j][k] + coins[i][j],dp[i][j-1][k] + coins[i][j], dp[i][j-1][k-1], dp[i-1][j][k-1])
                    
                    else:
                        dp[i][j][0] = dp[i-1][j][0] + coins[i][j]
                        for k in range(1,3):
                            dp[i][j][k] = max(dp[i-1][j][k] + coins[i][j], dp[i-1][j][k-1])
                else:
                    if j != 0:
                        dp[i][j][0] = dp[i][j-1][0] + coins[i][j]
                        for k in range(1,3):
                            dp[i][j][k] = max(dp[i][j-1][k] + coins[i][j], dp[i][j-1][k-1])
                    else:
                        dp[i][j][0] = coins[i][j]
        
        return max(dp[i][j])
