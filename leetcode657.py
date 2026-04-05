class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for k in moves:
            if k == "R":
                x+=1
            elif k == "L":
                x-=1
            elif k =="U":
                y+=1
            else:
                y-=1
        
        if x == 0 and y == 0:
            return True
        return False
