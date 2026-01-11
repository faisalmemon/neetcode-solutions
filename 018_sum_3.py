class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        data = sorted(nums)
        result = []
        items = len(data)
        for i in range(items - 2):
            if i > 0 and data[i] == data[i - 1]:
                continue
            target = data[i] * -1
            low_ptr = i + 1
            high_ptr = items -1
            while low_ptr < high_ptr:
                candidate_sum = data[low_ptr] + data[high_ptr]
                if candidate_sum > target:
                    high_ptr -= 1
                elif candidate_sum < target:
                    low_ptr += 1
                else:
                    result.append([-target, data[low_ptr], data[high_ptr]])
                    high_ptr -= 1
                    low_ptr += 1
                    while data[low_ptr] == data[low_ptr - 1] and low_ptr < high_ptr:
                        low_ptr += 1
        return result
