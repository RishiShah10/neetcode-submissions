from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        """
        user to tweet map
        user to follow map
        """
        self.userToTweet = defaultdict(list)
        self.userToFollower = defaultdict(set)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToTweet[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []
        followers = self.userToFollower[userId]

        for follower in followers:
            for time, tweet in self.userToTweet[follower]:
                heapq.heappush(heap, (-time, tweet))

        if userId not in followers:
            for time, tweet in self.userToTweet[userId]:
                heapq.heappush(heap, (-time, tweet))

        for _ in range(min(10, len(heap))):
            time, tweet = heapq.heappop(heap)
            result.append(tweet)

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userToFollower[followerId].discard(followeeId)
        
