import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        sort the cars from closest to target to not
        we will go in order of cars closest to target see how long they take
        add it to a stack if the one coming up is smaller than we dont add it because itll catch up
        then return length of our stack

        """
        paired = list(zip(position, speed))
        paired.sort(reverse=True) 
        position, speed = zip(*paired)
        fleets = 0
        lastTime = 0
        for i in range(len(position)):
            timeToTarget = (target - position[i])/speed[i]
            if timeToTarget > lastTime:
                fleets += 1
                lastTime = timeToTarget

        return fleets
