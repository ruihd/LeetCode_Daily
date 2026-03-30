class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        even1 = list()
        even2 = list()
        odd1 = list()
        odd2 = list()

        for _ in range(26):
            even1.append(0)
            even2.append(0)
            odd1.append(0)
            odd2.append(0)

        for i in range(len(s1)):
            if i%2 == 0:
                even1[ord(s1[i])-ord("a")] += 1
                even2[ord(s2[i])-ord("a")] += 1
            else:
                odd1[ord(s1[i])-ord("a")] += 1
                odd2[ord(s2[i])-ord("a")] += 1
        
        for i in range(26):
            if even1[i] != even2[i] or odd1[i] != odd2[i]:
                return False
        
        return True

        
        
