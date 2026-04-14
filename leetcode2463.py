class Solution:
    def get_dist(self, robot, factory):
        return abs(robot - factory)


    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        f = list()
        for x in factory:
            for _ in range(x[1]):
                f.append(x[0])

        dp = list()


        for i in range(len(robot)):
            dp.append(list())
            for j in range(len(f)):
                dp[i].append(float('inf'))
        

        for i in range(len(robot)):
            for j in range(len(f)):
                dp[i][j] = self.get_dist(robot[i],f[j])
                if i > j:
                    dp[i][j] = float('inf')
                else:
                    if i != 0:
                        dp[i][j] += dp[i-1][j]
                    if j != 0:
                        if i != 0:
                            dp[i][j] = min(dp[i][j-1], self.get_dist(robot[i],f[j]) + dp[i-1][j-1])
                        else:
                            dp[i][j] = min(dp[i][j-1], self.get_dist(robot[i],f[j]))
        return dp[-1][-1]
                    
