class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Space complexity O(1)
        # Time complexity O(n)
        low_ptr = 0
        high_ptr = len(numbers) - 1

        while low_ptr < high_ptr:
            total = numbers[low_ptr] + numbers[high_ptr]
            if total > target:
                high_ptr -= 1
            elif total < target:
                low_ptr += 1
            else:
                return [low_ptr+1, high_ptr+1]
        raise Exception("Error")
