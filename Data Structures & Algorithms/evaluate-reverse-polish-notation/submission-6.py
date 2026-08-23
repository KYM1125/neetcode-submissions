class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+','-','*','/']
        stack = []

        for token in tokens:
            if token in op:
                right = int(stack.pop())
                left = int(stack.pop())
                
                if token == '+':
                    token = left + right
                elif token == '*':
                    token = left * right
                elif token == '-':
                    token = left - right
                else:
                    token = left / right
                
            stack.append(token)
            # print("stack = ", stack)
        # print("stack = ", stack)
        return int(stack.pop())

        