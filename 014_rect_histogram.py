class Solution:

    def dump_stack(self, stack, comment):
        print(comment)
        if stack:
            for i in range(len(stack)):
                print(f'index {i} has index {stack[i][0]} height {stack[i][1]}')
        else:
            print(f'Empty stack')
        print("End")

    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest = 0
        past = [] # (index, height) 

        for i, h in enumerate(heights):

            self.dump_stack(past, f'Start of main loop index {i}')
            early_start = i 
            # 1. THE TRIGGER: While the current height is shorter than the stack top
            while past and h < past[-1][1]:
                index, height = past.pop()
                # 2. CALCULATE: The bar we just popped is finished. 
                # Its width is from its start to the current index.
                biggest = max(biggest, height * (i - index))
                # 3. INHERIT: The current bar 'h' can reach back to 
                # the index of the taller bar it just replaced.
                early_start = index
            
            past.append((early_start, h))

        # 4. CLEANUP: For bars that lasted until the end
        for index, height in past:
            biggest = max(biggest, height * (len(heights) - index))
            
        return biggest



class SolutionGemini:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest = 0
        past = [] # (index, height) 

        for i, h in enumerate(heights):
            start = i 
            # 1. THE TRIGGER: While the current height is shorter than the stack top
            while past and past[-1][1] > h:
                index, height = past.pop()
                # 2. CALCULATE: The bar we just popped is finished. 
                # Its width is from its start to the current index.
                biggest = max(biggest, height * (i - index))
                # 3. INHERIT: The current bar 'h' can reach back to 
                # the index of the taller bar it just replaced.
                start = index
            
            past.append((start, h))

        # 4. CLEANUP: For bars that lasted until the end
        for index, height in past:
            biggest = max(biggest, height * (len(heights) - index))
            
        return biggest


class SolutionBroken0:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest = 0
        past = [] # (height,index) pairs
        for i in range(len(heights)):
            if i == 0:
                past.append((heights[i], i))
                biggest = heights[i]
            else:
                if heights[i] < past[-1][0]:
                    past.pop()
                    past.append((heights[i], i - 1))
        while past:
            top = past.pop()
            area = (i - top[1] +1) * top[0]
            if area > biggest:
                biggest = area
            i = top[1]
        return biggest   
