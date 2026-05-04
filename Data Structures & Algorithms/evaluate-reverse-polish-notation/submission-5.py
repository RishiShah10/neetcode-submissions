import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        pop two if 
        add numbers to a stack 
        pop last two once get to a symbol
        keep a running value thing
        """
        
        stack = []
        valid = ["+", "-", "*", "/"]
        
        for i in range(0,len(tokens)):
            val = tokens[i]
            if val in valid:
                print(val)
                one = int(stack.pop())
                two = int(stack.pop())
                print(one,two)
                if val == "+":
                    two += one
                elif val == "-":
                    two -= one
                elif val == "*":
                    two *= one
                elif val == "/":
                    two = int(two / one)
                stack.append(two)
            else:
                stack.append(int(val))
        return stack[0]
        