from collections import defaultdict
from typing import List

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {} # dict number -> frequency
        for candidate in nums:
            if candidate in freq_list:
                freq_list[candidate] += 1
            else:
                freq_list[candidate] = 1
        all_values = freq_list.values()
        top_items = list(reversed(all_values))[0:k]
        overall_result = []
        for item in freq_list.keys():
            if freq_list[item] in top_items:
                overall_result.append(item)
        return overall_result

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {} # dict number -> frequency
        for candidate in nums:
            if candidate in freq_list:
                freq_list[candidate] += 1
            else:
                freq_list[candidate] = 1
        print(f'freq_list {freq_list}')
        all_values_sorted = sorted(list(freq_list.values()))
        print(f'all_values_sorted {all_values_sorted}')
        print(f'reversed all_values {list(reversed(all_values_sorted))}')
        top_items = list(reversed(all_values_sorted))[0:k]
        print(f'top_items {top_items}')
        overall_result = []
        for item in freq_list.keys():
            if freq_list[item] in top_items:
                overall_result.append(item)
        return overall_result
    


class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        print(f'freq_dict {freq_dict}')

        sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        print(f'sorted_items {sorted_items}')

        return [item[0] for item in sorted_items[:k]]
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # key number, value occurrences
        bucket = [[] for i in range(len(nums) + 1)] # ith list has freq i
        for item in nums:
            count[item] += 1
        for key,v in count.items():
            bucket[v].append(key)
        
        result = []

        for item in bucket[::-1]:
            for num in item:
                result.append(num)
                if len(result) == k:
                    return result
        
        raise ValueError("result has wrong number of items")