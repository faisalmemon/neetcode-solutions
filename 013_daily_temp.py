class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            print(f'Master index {i} temperature {t}')
            while stack and t > stack[-1][0]:
                print(f'Seen higher temperature {t} than tos {stack[-1][0]}')
                stackT,stackInd = stack.pop()
                print(f'Record result index {stackInd} has distance {i} - {stackInd} = {i-stackInd}')
                res[stackInd] = i - stackInd
            print(f'Appending t {t} i {i} to stack')
            stack.append((t,i))
        return res
