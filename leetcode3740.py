class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        t = dict()
        count = 0
        minimum = (len(nums),-1)
        for x in nums:
            if x not in t.keys():
                t[x] = [count]
            elif len(t[x]) == 1:
                t[x].append(count)
            else:
                if (count - t[x][0]) < minimum[0]:
                    minimum = (count - t[x][0],(count - t[x][0])*2)
                t[x][0] = t[x][1]
                t[x][1] = count

            count += 1

        return minimum[1]
