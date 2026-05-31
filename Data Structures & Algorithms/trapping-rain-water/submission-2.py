class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # max_left = [0] * n
        # max_right = [0] * n
        l_wall = r_wall = 0
        l, r = 0, n - 1

        # j = n - 1
        # for i in range(n):
        #     max_left[i] = l_wall
        #     max_right[j] = r_wall

        #     l_wall = max(l_wall, height[i])
        #     r_wall = max(r_wall, height[j])

        #     j -= 1

        total_water = 0
        while l <= r:
            if l_wall <= r_wall: # samller left side, process it
                total_water += max(l_wall - height[l], 0)
                l_wall = max(l_wall, height[l])
                l += 1
            else:
                total_water += max(r_wall - height[r], 0)
                r_wall = max(r_wall, height[r])
                r -= 1
        
        return total_water

        
        