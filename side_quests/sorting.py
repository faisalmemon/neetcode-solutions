from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        print(f'freq_dict {freq_dict}')

        sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        print(f'sorted_items {sorted_items}')

        return [item[0] for item in sorted_items[:k]]

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print(f'Top {k} frequent elements: {result}')


