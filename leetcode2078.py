class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = None
        s1 = 0
        for i in reversed(range(len(colors))):
            if colors[s1] != colors[i]:
                l = i-s1
                break
        s1 = len(colors) - 1
        for i in range(len(colors)):
            if colors[s1] != colors[i]:
                return max(l,s1 - i)
