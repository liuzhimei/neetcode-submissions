class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use stack data structure
        stack = []
        operations = ["+", "-", "*", "/"]

        for i in range(len(tokens)):
            # if tokens[i].isdigit(): # isdigit() only recognise positive integers
            #     stack.append(int(tokens[i]))
            if tokens[i] in operations:
                if tokens[i] == "+":
                    result = stack[-2] + stack[-1]
                elif tokens[i] == "-":
                    result = stack[-2] - stack[-1]
                elif tokens[i] == "*":
                    result = stack[-2] * stack[-1]
                else:
                    result = int(stack[-2] / stack[-1])
                stack = stack[:-2] + [result]
            else:
                stack.append(int(tokens[i]))
        return stack[0]