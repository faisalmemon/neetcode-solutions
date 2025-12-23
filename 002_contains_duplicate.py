class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        items = len(nums)
        for i in range(items):
            current = nums[i]
            if i == items - 1:
                next = None
            else:
                next = nums[i+1]
            if current == next:
                return True
        return False
        
