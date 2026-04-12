class Solution:
    def pos(self,c):
        n = ord(c) - ord("A")
        y = n%6
        x = n//6
        return [x,y]
    
    def dist(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1] - pos2[1])

    def minimumDistance(self, word: str) -> int:

        d = dict()
        d2 = dict()
        alphabet = set()
        for x in word:
            alphabet.add(x)
        K = len(alphabet)
        K_range = range(K)

        count = 0
        for x in alphabet:
            d[x] = count
            d2[count] = x
            count += 1
        
        real = list()
        for x in word:
            real.append(d[x])

        positions = dict()
        for n in K_range:
            positions[n] = self.pos(d2[n])
        
        distances = list()
        for i in K_range:
            distances.append([0] * K)

        for i in K_range:
            for j in range(i + 1, K):
                distances[i][j] = self.dist(positions[i],positions[j])
                distances[j][i] = distances[i][j]

        last = [0] * K
        old = real[0]

        for i in range(1, len(word)):
            curr = real[i]
            cost_old = distances[curr][old]
            new = [x + cost_old for x in last]
            best = min(last[j] + distances[j][curr] for j in K_range)
            new[old] = min(new[old], best)
            last = new
            old = curr
        
        return min(last)
