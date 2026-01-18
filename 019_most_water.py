class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_seen = 0
        low = 0
        high = len(heights) - 1
        while low < high:
            width = high - low
            least_height = min(heights[low], heights[high])
            area_seen = max(area_seen, least_height * width)
            if heights[low] < heights[high]:
                low += 1
            elif heights[low] >= heights[high]:
                high -= 1
        return area_seen
