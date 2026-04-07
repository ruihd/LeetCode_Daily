class Robot:

    def __init__(self, width: int, height: int):
        self.dir = 0
        self.width = width
        self.height = height
        self.pos = 0
        self.total = width*2 + height *2 - 4
        self.first = True

    def step(self, num: int) -> None:
        real = (self.pos+num)%self.total
        self.pos = real
        if num != 0:
            self.first = False

    def getPos(self) -> List[int]:
        if self.pos < self.width:
            return [self.pos,0]
        elif self.pos < self.width + self.height - 1:
            return [self.width-1, (self.pos-self.width + 1)]
        elif self.pos < self.width * 2 + self.height - 2:
            return [self.width - (self.pos - self.width - self.height + 2)-1, self.height-1]
        else:
            return [0, self.width - (self.pos - self.width - self.height*2 + 3)-1]

    def getDir(self) -> str:
        if self.first:
            return "East"
        elif self.pos == 0:
            return "South"
        if self.pos < self.width:
            return "East"
        elif self.pos < self.width + self.height - 1:
            return "North"
        elif self.pos < self.width * 2 + self.height - 2:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
