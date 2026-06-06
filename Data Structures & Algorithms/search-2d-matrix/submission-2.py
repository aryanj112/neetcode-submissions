class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row_len = len(matrix[0])

        array_index = 0
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][row_len - 1] < target:
                l = m + 1
            else:
                array_index = m
                break
        
        print(array_index)
        
        l, r = 0, len(matrix[array_index]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[array_index][m] > target:
                r = m - 1
            elif matrix[array_index][m] < target:
                l = m + 1
            else:
                return True
        
        return False
