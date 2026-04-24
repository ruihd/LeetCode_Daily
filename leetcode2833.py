class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        maximum = 0
        count = 0
        t = 0
        for i in range(len(moves)):
            if moves[i] == '_':
                count += 1
            elif moves[i] == 'L':
                t -= 1
            else:
                t += 1
            
            
        
        return abs(t) + count
