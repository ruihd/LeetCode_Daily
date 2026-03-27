class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        t = 1
        s = len(mat[0])
        for i in range(len(mat)):
            for j in range(s):
                pos = j+t*k
                if pos >= s or pos < 0:
                    pos = pos%s
                if mat[i][pos] != mat[i][j]:
                    return False
            t*=-1
        return True

            
