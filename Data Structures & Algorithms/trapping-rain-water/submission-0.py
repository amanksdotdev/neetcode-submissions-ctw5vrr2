class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        l_wall = r_wall = 0

        j = n - 1
        for i in range(n):
            max_left[i] = l_wall
            max_right[j] = r_wall

            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

            j -= 1

        total_water = 0
        for i in range(n):
            min_wall = min(max_left[i], max_right[i])
            total_water += max(min_wall - height[i], 0)
        
        return total_water
        
        