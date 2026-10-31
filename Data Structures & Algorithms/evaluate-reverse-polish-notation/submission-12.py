class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # # use stack data structure
        # stack = []
        # operations = ["+", "-", "*", "/"]

        # for i in range(len(tokens)):
        #     # if tokens[i].isdigit(): # isdigit() only recognise positive integers
        #     #     stack.append(int(tokens[i]))
        #     if tokens[i] in operations:
        #         if tokens[i] == "+":
        #             result = stack[-2] + stack[-1]
        #         elif tokens[i] == "-":
        #             result = stack[-2] - stack[-1]
        #         elif tokens[i] == "*":
        #             result = stack[-2] * stack[-1]
        #         else:
        #             result = int(stack[-2] / stack[-1]) # truncation towards 0 (notice the difference between a // b)
        #         stack = stack[:-2] + [result]
        #     else:
        #         stack.append(int(tokens[i]))
        # return stack[0]

        # --------- make code more efficient ---------
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop()) # stack.pop() modifies stack in place
            elif c == "-":
                a, b = stack.pop(), stack.pop() # be careful with pop ordering
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]

