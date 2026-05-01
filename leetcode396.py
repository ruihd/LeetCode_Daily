class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        tot = sum(nums)
        l = len(nums)
        ini = 0
        for i in range(len(nums)):
            ini += i*nums[i]
        

        maximum = ini
        for j in range(len(nums)):
            ini += tot - l*nums[l-j-1]
            maximum = max(maximum,ini)

        return maximum
