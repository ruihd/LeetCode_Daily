class Solution:
    def reve(self, num):
        return int(str(num)[::-1])
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = {}
        minimum = float('inf')

        for i, num in reversed(list(enumerate(nums))):
            r = self.reve(num)
            if r in d:
                minimum = min(minimum, d[r] - i)

            d[num] = i

        return -1 if minimum == float("inf") else minimum
