class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0;
        col = len(matrix[0]) - 1
        top = 0
        down = len(matrix) - 1
        while top <= down:
            mid_of_row = (top + down) // 2
            i = matrix[mid_of_row][0]
            j = matrix[mid_of_row][col]
            if i <= target <= j:
                # bs in this row
                left = 0
                right = col
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[mid_of_row][mid] > target:
                        right = mid - 1
                    elif matrix[mid_of_row][mid] < target:
                        left = mid + 1
                    else:
                        return True
                break
            elif i > target:
                down = mid_of_row - 1
            elif j < target:
                top = mid_of_row + 1
        
        return False

        