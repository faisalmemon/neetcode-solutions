class Solution:
    def trap(self, height: List[int]) -> int:
        low_ptr = 0
        high_ptr = len(height) - 1
        total_water = 0
        highest_left = 0
        highest_right = 0

        while low_ptr < high_ptr:
            highest_left = max(highest_left, height[low_ptr])
            highest_right = max(highest_right, height[high_ptr])
            if highest_left < highest_right:
                total_water += highest_left - height[low_ptr]
                low_ptr += 1
            else:
                total_water += highest_right - height[high_ptr]
                high_ptr -= 1
        return total_water
