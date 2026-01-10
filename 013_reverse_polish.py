class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        working_memory = []
        for token in tokens:
            if token == "+":
                arg1 = working_memory.pop()
                arg2 = working_memory.pop()
                working_memory.append(arg2 + arg1)
            elif token == "-":
                arg1 = working_memory.pop()
                arg2 = working_memory.pop()
                working_memory.append(arg2 - arg1)
            elif token == "*":
                arg1 = working_memory.pop()
                arg2 = working_memory.pop()
                working_memory.append(arg2 * arg1)
            elif token == "/":
                arg1 = working_memory.pop()
                arg2 = working_memory.pop()
                working_memory.append(int(arg2 / arg1))
            else:
                working_memory.append(int(token))
        return working_memory[0]
