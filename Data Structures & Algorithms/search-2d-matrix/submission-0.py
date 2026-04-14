class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0;
        col = len(matrix[0]) - 1
    
        while row < len(matrix):
            i = matrix[row][0]
            j = matrix[row][col]
            if i <= target <= j:
                # bs in this row
                left = 0
                right = col
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[row][mid] > target:
                        right = mid - 1
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        return True
                break
            else:
                row += 1
        
        return False

        