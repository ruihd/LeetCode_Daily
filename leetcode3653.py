class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            idx = q[0]
            while idx <= q[1]:
                nums[idx] = (nums[idx]*q[3]) % (10**9 + 7)
                idx += q[2]
        res = nums[0]
        for x in nums[1::]:
            res ^= x
        return res
