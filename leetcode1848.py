class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0
        l1 = list()
        l2 = list()
        if start != 0:
            l1 = nums[:start]
            l1 = l1[::-1]
        if start != len(nums)-1:
            l2 = nums[start+1:]
        for i in range(max(len(l1),len(l2))):
            if i < len(l1):
                if l1[i] == target:
                    return i + 1
            if i < len(l2):
                if l2[i] == target:
                    return i + 1
