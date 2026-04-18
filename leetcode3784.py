class Solution:
    def reve(self, num):
        return int(str(num)[::-1])
    def mirrorDistance(self, n: int) -> int:
        n1 = self.reve(n)
        return abs(n- n1)
