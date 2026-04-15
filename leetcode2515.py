class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        m = float('inf')
        for i in range(len(words)):
            if words[i] == target:
                m = min(m, abs(i - startIndex), abs(len(words) - startIndex + i), abs(len(words) + startIndex - i))
        if m == float('inf'):
            return -1
        return m
