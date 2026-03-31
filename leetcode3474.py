class Solution:
    def same(self, str1, str2, avoid):
        last = -1
        for i in range(len(str1)):
            if str1[i] == "_":
                if str2[i] != "a" or str2[i] in avoid[i]:
                    return (False, -2)
                last = i
            elif str1[i] != str2[i]:
                return (False, -1)
        return (True, last)

    def lowestNot(self, notstr):
        for i in range(ord("a"),ord("z")+1):
            if chr(i) not in notstr:
                return chr(i)
        return False

    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        st = list()

        musts = list()
        avoid = list()

        for _ in range(n+m-1):
            st.append("_")
            musts.append(set())
            avoid.append(set())
        
        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    musts[i+j].add(str2[j])
        for i in range(n+m-1):
            if len(musts[i]) > 1:
                return ""
            if len(musts[i]) != 0:
                st[i] = musts[i].pop()

        for i in range(m-1):
            if st[i] == "_":
                st[i] = "a"
        for i in range(n):
            if str1[i] == "F":
                test = self.same(st[i:i+m],str2,avoid[i:i+m])
                if test[0]:
                    if test[1] == -1:
                        return ""
                    avoid[test[1]+i].add(str2[test[1]])
                if st[i] == "_":
                    st[i] = self.lowestNot(avoid[i])

        for i in range(1,m):
            if st[i+n-1] == "_":
                st[i+n-1] = self.lowestNot(avoid[i+n-1])

        ret = ""
        for x in st:
            ret += x
        return ret

        



        
