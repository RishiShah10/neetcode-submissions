class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            '[': ']',
            '(': ')',
            '{': '}'
        }
        print("started")
        stack = []
        keys = mappings.keys()
        vals = mappings.values()
        for c in s:
            if c not in keys and c not in vals:
                continue
            if c in vals:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                print(c,top)
                if mappings[top] != c:
                    return False
                stack.pop()
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        return True


        