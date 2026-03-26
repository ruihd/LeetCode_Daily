class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        up = 0
        rows_set = set()
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += grid[i][j]

        for i in range(len(grid)):
            if i != 0:
                if up == total - up or up - total + up in rows_set:
                    if (i == 1 or len(grid[0]) == 1) and not up == total - up:
                        if i == 1:
                            if grid[0][0] == up - total + up or grid[0][-1] == up - total + up:
                                return True
                        else:
                            if grid[0][0] == up - total + up or grid[i-1][0] == up - total + up:
                                return True
                    else:
                        return True
            for j in range(len(grid[0])):
                rows_set.add(grid[i][j])
                up += grid[i][j]
        #Faltam os cantos for n = 1
        up = 0
        rows_set = set()
        for i in reversed(range(0,len(grid))):
            if i != len(grid)-1:
                if up == total - up or up - total + up in rows_set:
                    if (i == len(grid)-2 or len(grid) == 1) and not up == total - up:
                        if i == len(grid)-2:
                            if grid[-1][0] == up - total + up or grid[-1][-1] == up - total + up:
                                return True
                        else:
                            if grid[-1][0] == up - total + up or grid[i][0] == up - total + up:
                                return True
                    else:
                        return True
            for j in range(len(grid[0])):
                rows_set.add(grid[i][j])
                up += grid[i][j]
        #Faltam os cantos for n = 1
        print("Cols")
        up = 0
        rows_set = set()
        for j in range(len(grid[0])):
            if j != 0:
                if up == total - up or up - total + up in rows_set:
                    if (j == 1 or len(grid) == 1) and not up == total - up:
                        if j == 1:
                            if grid[0][0] == up - total + up or grid[-1][0] == up - total + up:
                                return True
                        else:
                            if grid[0][0] == up - total + up or grid[0][j-1] == up - total + up:
                                return True
                    else:
                        return True
            for i in range(len(grid)):
                rows_set.add(grid[i][j])
                up += grid[i][j]
        #Faltam os cantos for n = 1
        up = 0
        rows_set = set()
        for j in reversed(range(0,len(grid[0]))):
            if j != len(grid[0])-1:
                if up == total - up or up - total + up in rows_set:
                    if (j == len(grid[0])-2 or len(grid) == 1) and not up == total - up:
                        if j == len(grid[0])-2:
                            if grid[-1][-1] == up - total + up or grid[0][-1] == up - total + up:
                                return True
                        else:
                            if grid[0][-1] == up - total + up or grid[0][j] == up - total + up:
                                return True
                    else:
                        return True
            for i in range(len(grid)):
                rows_set.add(grid[i][j])
                up += grid[i][j]
        #Faltam os cantos for n = 1


        return False

