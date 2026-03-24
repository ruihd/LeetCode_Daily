class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        prefix = list()
        sufix = list()
        ret = list()
        last = None
        for l in grid:
            for x in l:
                if len(prefix) == 0:
                    prefix.append(1)
                else:
                    t = prefix[-1] * last
                    if t > 12345:
                        t %=12345
                    prefix.append(t)
                last = x
        
        for l in grid[::-1]:
            for x in l[::-1]:
                if len(sufix) == 0:
                    sufix.append(1)
                else:
                    t = sufix[-1] * last
                    if t > 12345:
                        t %=12345
                    sufix.append(t)
                last = x
        for i in range(n):
            ret.append(list())
            for j in range(m):
                ret[i].append(prefix[i*m + j]*sufix[n*m-1-(i*m + j)]%12345)
        
        return ret
        
