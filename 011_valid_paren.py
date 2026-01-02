class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openSet = set(['(', '{', '['])

        for char in s:
            if char in openSet:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top_item = stack.pop()
                if top_item == '(' and char == ')':
                    continue
                if top_item == '[' and char == ']':
                    continue
                if top_item == '{' and char == '}':
                    continue
                return False
        all_matched = len(stack) == 0
        return all_matched
