class Twitter:

    def __init__(self):
        self.time = 0
        self.userToFollowers = defaultdict(set) # list of people who user follows
        self.userToPosts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToPosts[userId].append([-self.time,tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        self.follow(userId, userId)
        for follower in self.userToFollowers[userId]:
            for post in self.userToPosts[follower]:
                maxHeap.append(post)
        heapq.heapify(maxHeap)

        res = []
        for _ in range(10):
            if not maxHeap:
                return res
            time, postId = heapq.heappop(maxHeap)
            res.append(postId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollowers[followerId]:
            self.userToFollowers[followerId].remove(followeeId)
