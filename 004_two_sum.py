class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ValToIndex = {}
        for (first_index,first_value) in enumerate(nums):
            ValToIndex[first_value] = first_index
        nums.sort()
        low_pointer = 0
        high_pointer = len(nums) - 1
        while nums[low_pointer] + nums[high_pointer] != target:
            if nums[low_pointer] + nums[high_pointer] > target:
                high_pointer -= 1
            if nums[low_pointer] + nums[high_pointer] < target:
                low_pointer += 1
        
        return [ValToIndex[nums[low_pointer]], ValToIndex[nums[high_pointer]]]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = copy.copy(nums)  
        nums.sort()
        low_pointer = 0
        high_pointer = len(nums) - 1
        while nums[low_pointer] + nums[high_pointer] != target:
            if nums[low_pointer] + nums[high_pointer] > target:
                high_pointer -= 1
            if nums[low_pointer] + nums[high_pointer] < target:
                low_pointer += 1

        print(f'nums low pointer {nums[low_pointer]}')
        print(f'nums high pointer {nums[high_pointer]}')
        
        first_index = None
        second_index = None
        for i in range(len(saved)):
            if saved[i] == nums[low_pointer]:
                first_index = i
                break
        
        for j in range(len(saved) - 1, -1, -1):
            if saved[j] == nums[high_pointer]:
                second_index = j
                break
        
        if first_index < second_index:
            return [first_index, second_index]
        else:
            return [second_index, first_index]

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for (i,n) in enumerate(nums):
            difference = target - n
            if difference in hash_map:
                return [hash_map[difference], i]
            else:
                hash_map[n] = i
