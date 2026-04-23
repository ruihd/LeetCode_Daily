class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = dict()
        arr = [0] * len(nums)
        count = 0
        for x in nums:
            if x in d.keys():
                d[x].append(count)
            else:
                d[x] = [count]
            count += 1

        for k in d.keys():
            l = d[k]
            le = -len(l)
            if le != -1:
                count1 = sum(l)
                last = 0
                for x in l:
                    count1 += (x - last) * le
                    arr[x] = count1
                    le += 2
                    last = x
    
        return arr
