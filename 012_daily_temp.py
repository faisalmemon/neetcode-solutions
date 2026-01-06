class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 1):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res

class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # Stores indices

        for i, temp in enumerate(temperatures):
            # While the current temp is warmer than the temp at the stack's top index
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
            
        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        index_stack = [] # Stores indices

        for (index, current_temp) in enumerate(temperatures):
            while index_stack and current_temp > temperatures[index_stack[-1]]:
                previous_index = index_stack.pop()
                res[previous_index] = index - previous_index
            index_stack.append(index)
            
        return res
