class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        add each asteroid to stack
        if stack and last thing is oppsite sign as you then see which blows up 
        """
        stack = []
        def will_collide(a, b):
            # a is the new asteroid, b is the top of stack
            return b > 0 and a < 0
        for a in asteroids:
            stack.append(a)
            while len(stack) >= 2 and will_collide(stack[-1],stack[-2]):
                one,two = stack.pop(),stack.pop()
                print(one,two)
                if abs(one) > abs(two):
                    stack.append(one)
                elif abs(one) < abs(two):
                    stack.append(two)
        return stack