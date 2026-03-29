class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(0,2):
            f1 = set([s1[i],s1[2+i]])
            f2 = set([s2[i],s2[2+i]])
            if s1[i] not in f2 or s1[2+i] not in f2 or s2[i] not in f1 or s2[i+2] not in f1:
                return False
        return True
