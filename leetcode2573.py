class Solution:
    def get_zeros(self,lcp):
        non_zeros = list()
        
        for j in range(len(lcp)):
            for i in range(0,j+1):
                if lcp[i][j] != 0:
                    non_zeros.append(i)
                    break
        
        count = 0
        dit = dict()
        for x in non_zeros:
            if x not in dit.keys():
                dit[x] = count
                count += 1

        for i in range(len(non_zeros)):
            non_zeros[i] = dit[non_zeros[i]]
            if non_zeros[i] > ord("z") - ord("a"):
                return list()

        return non_zeros
    def findTheString(self, lcp: List[List[int]]) -> str:
        non_zeros = self.get_zeros(lcp)
        ret = ""
        if len(non_zeros) != len(lcp):
            return ""
        for x in non_zeros:
            ret += chr(ord("a") + x)

        new_lcp = list()
        for i in range(len(lcp)):
            new_lcp.append(list())
            for _ in range(len(lcp[0])):
                new_lcp[i].append(0)
        
        for i in reversed(range(0,len(lcp))):
            for j in reversed(range(0,len(lcp))):
                if i != len(lcp)-1:
                    if j != len(lcp)-1:
                        if ret[i] == ret[j]:
                            new_lcp[i][j] = new_lcp[i+1][j+1] + 1
                    else:
                        if ret[i] == ret[j]:
                            new_lcp[i][j] = 1
                else:
                    if ret[i] == ret[j]:
                        new_lcp[i][j] = 1
        
        for i in range(len(lcp)):
            for j in range(len(lcp)):
                if new_lcp[i][j] != lcp[i][j]:
                    return ""
        return ret


