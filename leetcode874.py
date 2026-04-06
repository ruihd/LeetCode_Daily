class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for x in obstacles:
            obs.add((x[0],x[1]))
        pos = [0,0]
        dir = 0
        maximum = 0
        for x in commands:
            if x == -2:
                dir+=1
                dir = dir%4
            if x == -1:
                dir -= 1
                if dir < 0:
                    dir = 3
            else:
                if dir == 0:
                    for i in range(x):
                        if (pos[0],pos[1]+1) not in obs:
                            pos = [pos[0],pos[1]+1]
                        else:
                            break
                elif dir == 2:
                    for i in range(x):
                        if (pos[0],pos[1]-1) not in obs:
                            pos = [pos[0],pos[1]-1]
                        else:
                            break
                elif dir == 1:
                    for i in range(x):
                        if (pos[0]-1,pos[1]) not in obs:
                            pos = [pos[0]-1,pos[1]]
                        else:
                            break
                else:
                    for i in range(x):
                        if (pos[0]+1,pos[1]) not in obs:
                            pos = [pos[0]+1,pos[1]]
                        else:
                            break
                if pos[0]**2+pos[1]**2 > maximum:
                    maximum = pos[0]**2+pos[1]**2
        return maximum
            
