class Solution:
    def isValid(self, s: str) -> bool:
        """
        Using a stack we can put the chars in order
        if we see a closing one pop from the stack if not the right one return false
        return false if len(stack) not 0
        return true only if len of stack = 0
        """
        stack = []
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        closing = mapping.keys()
        for char in s:
            print(char)
            if char in closing:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True
