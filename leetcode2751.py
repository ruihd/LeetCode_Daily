class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        new_order = list()
        for i in range(len(positions)):
            new_order.append([i,positions[i],healths[i],directions[i]])
        
        new_order.sort(key = lambda x: x[1])

        healths = list()
        directions = list()
        for x in new_order:
            healths.append(x[2])
            directions.append(x[3])

        q = list()
        for i in range(len(positions)):
            if directions[i] == "L" and len(q) != 0:
                while len(q) > 0:
                    if healths[i] > q[-1][1]:
                        healths[i] -= 1
                        healths[q[-1][0]] = 0
                        q.pop()
                    elif healths[i] < q[-1][1]:
                        healths[i] = 0
                        healths[q[-1][0]] -= 1
                        q[-1][1] -= 1
                        break
                    else:
                        healths[i] = 0
                        healths[q[-1][0]] = 0
                        q.pop()
                        break

            if directions[i] == "R":
                q.append([i,healths[i]])
        
        ret = list()
        for _ in healths:
            ret.append(0)
        
        for i in range(len(healths)):
            if healths[i] != 0:
                ret[new_order[i][0]] = healths[i]
        
        ret2 = list()
        for x in ret:
            if x != 0:
                ret2.append(x)

        return ret2
            


