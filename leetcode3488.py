class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = dict()
        keys = set()
        d1 = list()

        for i in range(len(nums)):
            if nums[i] not in keys:
                keys.add(nums[i])
                d[nums[i]] = [i]
                d1.append(0)
            else:
                d[nums[i]].append(i)
                d1.append(len(d[nums[i]])-1)
        
        res = list()



        for q in queries:
            l = d[nums[q]]
            if len(l) == 1:
                res.append(-1)
            else:
                j = d1[q]
                if j < len(l)-1 and j > 0:
                    res.append(min(abs(l[j]-l[j+1]),abs(l[j]-l[j-1])))
                elif j == 0:
                    res.append(min(abs(l[j]-l[j+1]),len(nums) - abs(l[j]-l[j-1])))
                else:
                    res.append(min(len(nums) - abs(l[j]-l[0]),abs(l[j]-l[j-1])))
        return res
            
