import collections
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = collections.defaultdict(list)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        
        self.followees[userId].add(userId)

        for followeeId in self.followees[userId]:
            for post in self.posts[followeeId]:
                heapq.heappush_max(maxHeap, post)
        
        p = []
        i = 0
        while i < 10 and maxHeap:
            p.append(heapq.heappop_max(maxHeap)[1])
            i += 1

        return p

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followees[followerId].discard(followeeId)
