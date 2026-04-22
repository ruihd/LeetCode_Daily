class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maximum = 0

        s1 = 0
        s2 = 0

        while s1 != len(nums1) and s2 != len(nums2):
            if nums1[s1] <= nums2[s2]:
                if s2-s1 > maximum:
                    maximum = s2-s1
                s2+= 1
            else:
                s1+=1
        
        return maximum
