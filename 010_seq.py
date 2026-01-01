class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        set_of_nums = set(nums)
        list_of_nums = list(set_of_nums)
        list_of_nums.sort()
        low_ptr = list_of_nums[0]
        high_ptr = low_ptr
        biggest_range_so_far = 0
        for item in list_of_nums:
            if item == low_ptr:
                continue
            if item == high_ptr + 1:
                high_ptr = item
                continue
            if item > high_ptr + 1:
                if high_ptr - low_ptr > biggest_range_so_far:
                    biggest_range_so_far = high_ptr - low_ptr
                low_ptr = item
                high_ptr = item
        if high_ptr - low_ptr > biggest_range_so_far:
            biggest_range_so_far = high_ptr - low_ptr
        return biggest_range_so_far + 1
        
