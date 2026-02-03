class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        count = [0] * (size + 1)
        for row in grid:
            for val in row:
                count[val] += 1
        rep= mis= -1
        for i in range(1, size + 1):
            if count[i] == 2:
                rep = i
            elif count[i] == 0:
                mis= i
        
        return [rep, mis]
                