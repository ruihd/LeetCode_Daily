class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mults = list()
        for _ in nums:
            mults.append(1)
        
        th = len(nums) ** 0.5

        groups = dict()

        for q in queries:
            if th >= q[2]:
                if (q[2], q[0] % q[2]) not in groups.keys():
                    groups[(q[2], q[0] % q[2])] = list()
                X = (q[0] - q[0] % q[2])//q[2]
                Y = (q[1] - q[0] % q[2])//q[2] + 1
                groups[(q[2], q[0] % q[2])].append((X, Y, q[3]))
            else:
                idx = q[0]
                while idx <= q[1]:
                    nums[idx] = (nums[idx] * q[3]) % (10**9 + 7)
                    idx += q[2]

        a = q[2]
        b = q[0] % q[2]


        for (a, b), up in groups.items():
            size = ((len(nums) - 1 - b) // a) + 1
            arr = [1] * size
            for X, Y, val in up:
                arr[X] = (arr[X] * val) % (10**9 + 7)
                if Y < size:
                    inv = pow(val, -1, (10**9 + 7))
                    arr[Y] = (arr[Y] * inv) % (10**9 + 7)
            for i in range(1, size):
                arr[i] = (arr[i] * arr[i - 1]) % (10**9 + 7)
            for i in range(size):
                o = b + i * a
                if o < len(nums):
                    nums[o] = (nums[o] * arr[i]) % (10**9 + 7)


        ret = nums[0]
        for i in range(1,len(nums)):    
            ret ^= nums[i]
        return ret
