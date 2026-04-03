class Solution:
    def lower_bound(self, arr, t):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < t:
                left = mid + 1
            else:
                right = mid

        if left < len(arr) and arr[left] == t:
            return left
        return left - 1 if left > 0 else -1

    def upper_bound(self, arr, t):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= t:
                left = mid + 1
            else:
                right = mid

        if left > 0 and arr[left - 1] == t:
            return left - 1
        return left if left < len(arr) else -1


    def interval(self, dist, start, walls):
        left = 0
        right = len(walls) - 1

        if dist > 0:
            s = self.upper_bound(walls,start)
            t = self.lower_bound(walls,start + dist)
            if s < 0 or s > t:
                return 0
            else:
                return t-s+1
        else:
            t = self.upper_bound(walls,start + dist)
            s = self.lower_bound(walls,start)
            if t < 0 or s < t:
                return 0
            else:
                return s-t+1

    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:

        rob = list()
        for i in range(len(robots)):
            rob.append([robots[i],distance[i]])

        rob.sort(key = lambda x: x[0])
        walls.sort()

        print(walls)

        left = [0,0]
        right = [0,0]

        for i in range(len(rob)):
            left1 = [-1,-1]
            dl = max(-rob[i][1], left[1]-rob[i][0])
            left1[0] = left[0] + self.interval(dl, rob[i][0],walls)
            left1[1] = rob[i][0] + 1


            left2 = [-1,-1]
            dl = max(-rob[i][1], right[1]-rob[i][0])
            left2[0] = right[0] + self.interval(dl, rob[i][0],walls)
            left2[1] = rob[i][0] + 1


            right1 = [-1,-1]
            dr = rob[i][1]
            if i != len(rob)-1:
                if rob[i][1] >= rob[i+1][0] - rob[i][0]:
                    dr = rob[i+1][0] - rob[i][0] -1
            right1[0] = max(left[0],right[0]) + self.interval(dr, rob[i][0],walls)
            right1[1] = rob[i][0] + dr + 1

            right = right1
            left[0] = max(left2[0],left1[0])
            left[1] = left1[1]


        
        return max(left[0],right[0])
            

