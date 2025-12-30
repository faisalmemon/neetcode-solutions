class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_holes =  0
        total_product = 1
        for item in nums:
            if item == 0:
                num_holes += 1
            total_product *= item
        if num_holes >= 2:
            return [0] * len(nums)
        elif num_holes == 0:
            result = [total_product] * len(nums)
            for i in range(len(nums)):
                result[i] = int(result[i] / nums[i])
            return result
        else:
            result = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    product_non_holes = 1
                    for j in nums:
                        if j == 0:
                            continue
                        product_non_holes *= j
                    result[i] = product_non_holes
                    return result

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_holes =  0
        total_product = 1
        array_length = len(nums)
        result = [1] * array_length
        for index in range(array_length):
            if nums[index] == 0:
                num_holes += 1
            for subindex in range(array_length):
                if subindex != index:
                    result[subindex] *= nums[index]
        if num_holes == 0:
            return result
        elif num_holes == 2:
            result [0] * array_length
        else:
            for i in range(array_length):
                if nums[i] != 0:
                    result[i] = 0
        return result

class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product, post_fix_product = 1, 1
        length = len(nums)
        result = [1] * length
        for i in range(length):
            result[i] *= prefix_product
            prefix_product *= nums[i]
        for j in range(length - 1, -1, -1):
            result[j] *= post_fix_product
            post_fix_product *= nums[j]
        return result

class Solution4:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product, post_fix_product = 1, 1
        length = len(nums)
        result = [1] * length
        forward_pass_iteration = range(length)
        backward_pass_iteration = reversed(range(length))
        for i in forward_pass_iteration:
            result[i] *= prefix_product
            prefix_product *= nums[i]
        for j in backward_pass_iteration:
            result[j] *= post_fix_product
            post_fix_product *= nums[j]
        return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        forward_pass_iteration = range(length)
        backward_pass_iteration = reversed(forward_pass_iteration)
        for direction in [forward_pass_iteration, backward_pass_iteration]:
            precomputation = 1
            for i in direction:
                result[i] *= precomputation
                precomputation *= nums[i]
        return result
