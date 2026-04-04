class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if len(encodedText) == 0:
            return ""
        s = len(encodedText)//rows
        mat = list()
        for i in range(rows):
            mat.append(list())
            for j in range(s):
                mat[i].append(encodedText[i*s+j])
        

        ret = ""
        for j in range(s - rows + 1):
            for i in range(rows):
                ret += mat[i][j+i]
        
        last = -1
        for i in range(rows-1):
            if mat[i][s - rows + 1+i] != " ":
                last = i
        
        for i in range(last+1):
            ret += mat[i][s - rows + 1+i]

        return ret
